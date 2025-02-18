import backtrader as bt
import numpy as np

class KlingerVolumeOscillator(bt.Indicator):
    """
    Klinger Volume Oscillator (KVO)
    
    Ein Indikator, der Volumen und Preistrends kombiniert,
    um Trendwenden und Divergenzen zu identifizieren.
    
    Features:
    - Trend-Volumen-Integration
    - Divergenzanalyse
    - Signallinienkreuzungen
    - Trendstärkeberechnung
    - Signal-Validierung
    
    Parameter:
    - fast_period (34): Schnelle EMA-Periode
    - slow_period (55): Langsame EMA-Periode
    - signal_period (13): Signallinie-Periode
    """
    
    lines = ('kvo', 'signal',
             'trend_force', 'volume_force',
             'divergence', 'buy_signal',
             'sell_signal')
             
    params = (
        ('fast_period', 34),
        ('slow_period', 55),
        ('signal_period', 13),
        ('min_trend_strength', 0.3)
    )
    
    plotlines = dict(
        kvo=dict(color='blue', _name='KVO'),
        signal=dict(color='red', _name='Signal'),
        trend_force=dict(color='purple', _name='Trend Force'),
        volume_force=dict(color='orange', _name='Volume Force'),
        divergence=dict(color='green', _name='Divergence'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(KlingerVolumeOscillator, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.fast_period)
        self.vol = bt.indicators.StdDev(period=self.p.fast_period)
        
        # Historie
        self.kvo_history = []
        self.price_history = []
        self.trend_history = []
        
    def calculate_trend_force(self):
        """
        Berechnet die Trendkraft.
        """
        if len(self.data) < 2:
            return 0
            
        # Typischer Preis
        hlc3 = (self.data.high[0] + self.data.low[0] +
                self.data.close[0]) / 3
        prev_hlc3 = (self.data.high[-1] + self.data.low[-1] +
                     self.data.close[-1]) / 3
                     
        # Trendrichtung
        trend = 1 if hlc3 > prev_hlc3 else -1
        
        # Volumengewichtung
        force = trend * self.data.volume[0]
        
        return force
        
    def calculate_volume_force(self):
        """
        Berechnet die Volumenkraft.
        """
        if len(self.data) < self.p.fast_period:
            return 0
            
        # Durchschnittliches Volumen
        avg_volume = np.mean([
            self.data.volume.get(ago=-i, size=1)[0]
            for i in range(self.p.fast_period)
        ])
        
        if avg_volume == 0:
            return 0
            
        # Relative Volumenkraft
        force = self.data.volume[0] / avg_volume - 1
        
        return force
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und KVO.
        """
        if len(self.kvo_history) < self.p.slow_period or len(self.price_history) < self.p.slow_period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.slow_period:])
        price_low = min(self.price_history[-self.p.slow_period:])
        
        # KVO-Hochs/-Tiefs
        kvo_high = max(self.kvo_history[-self.p.slow_period:])
        kvo_low = min(self.kvo_history[-self.p.slow_period:])
        
        # Bullische Divergenz
        if price_low < price_high and kvo_low > kvo_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and kvo_low < kvo_high:
            return -1
            
        return 0
        
    def next(self):
        # Trendkraft berechnen
        trend_force = self.calculate_trend_force()
        self.lines.trend_force[0] = trend_force
        
        # Volumenkraft berechnen
        volume_force = self.calculate_volume_force()
        self.lines.volume_force[0] = volume_force
        
        # KVO berechnen
        fast_ema = bt.indicators.EMA(
            trend_force, period=self.p.fast_period
        )[0]
        slow_ema = bt.indicators.EMA(
            trend_force, period=self.p.slow_period
        )[0]
        
        self.lines.kvo[0] = fast_ema - slow_ema
        self.kvo_history.append(self.lines.kvo[0])
        
        # Signallinie
        self.lines.signal[0] = bt.indicators.EMA(
            self.lines.kvo, period=self.p.signal_period
        )[0]
        
        # Historie aktualisieren
        self.price_history.append(self.data[0])
        self.trend_history.append(trend_force)
        
        # Divergenz erkennen
        self.lines.divergence[0] = self.detect_divergence()
        
        # Historie begrenzen
        max_period = max(
            self.p.fast_period,
            self.p.slow_period,
            self.p.signal_period
        )
        for hist in [self.kvo_history, self.price_history,
                    self.trend_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.kvo[0] > self.lines.signal[0] and
            self.lines.kvo[-1] <= self.lines.signal[-1] and
            self.lines.volume_force[0] > 0 and
            abs(self.lines.trend_force[0]) > self.p.min_trend_strength):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.kvo[0] < self.lines.signal[0] and
            self.lines.kvo[-1] >= self.lines.signal[-1] and
            self.lines.volume_force[0] > 0 and
            abs(self.lines.trend_force[0]) > self.p.min_trend_strength):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'oscillator': {
                'kvo': self.lines.kvo[0],
                'signal': self.lines.signal[0],
                'difference': self.lines.kvo[0] - self.lines.signal[0],
                'momentum': (
                    self.lines.kvo[0] - self.kvo_history[-2]
                    if len(self.kvo_history) > 1
                    else 0
                )
            },
            'force': {
                'trend': self.lines.trend_force[0],
                'volume': self.lines.volume_force[0],
                'combined': (
                    self.lines.trend_force[0] *
                    self.lines.volume_force[0]
                )
            },
            'divergence': {
                'type': (
                    'bullish' if self.lines.divergence[0] > 0
                    else 'bearish' if self.lines.divergence[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.divergence[0]),
                'validation': (
                    self.lines.volume_force[0] > 0 and
                    abs(self.lines.trend_force[0]) > self.p.min_trend_strength
                )
            },
            'trend': {
                'direction': np.sign(self.lines.kvo[0]),
                'strength': abs(self.lines.trend_force[0]),
                'persistence': (
                    np.mean([
                        1 if trend > 0
                        else -1 if trend < 0
                        else 0
                        for trend in self.trend_history[-5:]
                    ]) if len(self.trend_history) >= 5
                    else 0
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(self.lines.trend_force[0]),
                'reliability': (
                    abs(self.lines.trend_force[0]) *
                    abs(self.lines.volume_force[0]) *
                    (1 + abs(self.lines.divergence[0]))
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'kvo_stability': (
                    np.std(self.kvo_history)
                    if len(self.kvo_history) > 1
                    else 0
                ),
                'trend_stability': (
                    np.std(self.trend_history)
                    if len(self.trend_history) > 1
                    else 0
                )
            }
        }
