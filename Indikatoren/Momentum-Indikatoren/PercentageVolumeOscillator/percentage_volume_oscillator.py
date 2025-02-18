import backtrader as bt
import numpy as np

class PercentageVolumeOscillator(bt.Indicator):
    """
    Percentage Volume Oscillator (PVO)
    
    Ein Momentum-Indikator, der die prozentuale Differenz zwischen
    zwei exponentiellen gleitenden Durchschnitten des Volumens berechnet.
    
    Features:
    - Prozentuale Volumenoszillation
    - Signallinie und Histogramm
    - Volumentrend-Analyse
    - Divergenz-Erkennung
    - Signal-Validierung
    
    Parameter:
    - fast_period (12): Schnelle EMA Periode
    - slow_period (26): Langsame EMA Periode
    - signal_period (9): Signal EMA Periode
    - upper_threshold (25.0): Obere Schwelle
    - lower_threshold (-25.0): Untere Schwelle
    """
    
    lines = ('pvo', 'signal', 'histogram',
             'volume_trend', 'divergence',
             'upper', 'lower',
             'buy_signal', 'sell_signal')
             
    params = (
        ('fast_period', 12),
        ('slow_period', 26),
        ('signal_period', 9),
        ('upper_threshold', 25.0),
        ('lower_threshold', -25.0)
    )
    
    plotlines = dict(
        pvo=dict(color='blue', _name='PVO'),
        signal=dict(color='red', _name='Signal'),
        histogram=dict(color='green', _name='Histogram'),
        volume_trend=dict(color='purple', _name='Volume Trend'),
        divergence=dict(color='orange', _name='Divergence'),
        upper=dict(color='gray', _name='Upper'),
        lower=dict(color='gray', _name='Lower'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(PercentageVolumeOscillator, self).__init__()
        
        # EMAs für Volumen
        self.fast_ma = bt.indicators.EMA(self.data.volume, period=self.p.fast_period)
        self.slow_ma = bt.indicators.EMA(self.data.volume, period=self.p.slow_period)
        
        # Technische Indikatoren
        self.volume_std = bt.indicators.StdDev(self.data.volume, period=20)
        self.price_std = bt.indicators.StdDev(period=20)
        
        # Historie
        self.pvo_history = []
        self.volume_history = []
        self.price_history = []
        self.histogram_history = []
        
    def calculate_pvo(self):
        """
        Berechnet den PVO-Wert.
        """
        if self.slow_ma[0] == 0:
            return 0
            
        return (
            (self.fast_ma[0] - self.slow_ma[0]) /
            self.slow_ma[0] * 100
        )
        
    def calculate_volume_trend(self):
        """
        Analysiert den Volumentrend.
        """
        if len(self.volume_history) < self.p.signal_period:
            return 0
            
        # Volumentrend über Signal-Periode
        trend = sum(
            1 if v > self.volume_history[i-1] else -1
            for i, v in enumerate(self.volume_history[-self.p.signal_period:])
            if i > 0
        )
        
        return trend / (self.p.signal_period - 1)
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und Volumen.
        """
        if len(self.price_history) < self.p.signal_period or len(self.pvo_history) < self.p.signal_period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.signal_period:])
        price_low = min(self.price_history[-self.p.signal_period:])
        
        # PVO-Hochs/-Tiefs
        pvo_high = max(self.pvo_history[-self.p.signal_period:])
        pvo_low = min(self.pvo_history[-self.p.signal_period:])
        
        # Bullische Divergenz
        if price_low < price_high and pvo_low > pvo_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and pvo_low < pvo_high:
            return -1
            
        return 0
        
    def next(self):
        # PVO berechnen
        self.lines.pvo[0] = self.calculate_pvo()
        
        # Signal-Linie
        self.lines.signal[0] = bt.indicators.EMA(
            self.lines.pvo, period=self.p.signal_period
        )[0]
        
        # Histogramm
        self.lines.histogram[0] = (
            self.lines.pvo[0] - self.lines.signal[0]
        )
        
        # Historie aktualisieren
        self.pvo_history.append(self.lines.pvo[0])
        self.volume_history.append(self.data.volume[0])
        self.price_history.append(self.data[0])
        self.histogram_history.append(self.lines.histogram[0])
        
        # Volumentrend
        self.lines.volume_trend[0] = self.calculate_volume_trend()
        
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Bänder
        self.lines.upper[0] = self.p.upper_threshold
        self.lines.lower[0] = self.p.lower_threshold
        
        # Historie begrenzen
        max_period = max(self.p.slow_period, self.p.signal_period)
        for hist in [self.pvo_history, self.volume_history, self.price_history, self.histogram_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.pvo[0] < self.p.lower_threshold and
            self.lines.histogram[0] > 0 and
            self.lines.volume_trend[0] > 0 and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.pvo[0] > self.p.upper_threshold and
            self.lines.histogram[0] < 0 and
            self.lines.volume_trend[0] < 0 and
            self.lines.divergence[0] <= 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'oscillator': {
                'pvo': self.lines.pvo[0],
                'signal': self.lines.signal[0],
                'histogram': self.lines.histogram[0],
                'volume_trend': self.lines.volume_trend[0]
            },
            'volume': {
                'trend': self.lines.volume_trend[0],
                'strength': abs(self.lines.volume_trend[0]),
                'momentum': (
                    self.volume_history[-1] - self.volume_history[-2]
                    if len(self.volume_history) > 1
                    else 0
                )
            },
            'divergence': {
                'type': (
                    'bullish' if self.lines.divergence[0] > 0
                    else 'bearish' if self.lines.divergence[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.divergence[0])
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(self.lines.volume_trend[0]),
                'reliability': (
                    abs(self.lines.volume_trend[0]) *
                    (1 + abs(self.lines.divergence[0])) *
                    abs(self.lines.histogram[0])
                )
            },
            'risk': {
                'volume_volatility': (
                    self.volume_std[0] / self.data.volume[0]
                    if self.data.volume[0] != 0
                    else 0
                ),
                'price_volatility': (
                    self.price_std[0] / self.data[0]
                    if self.data[0] != 0
                    else 0
                ),
                'trend_consistency': (
                    np.mean([
                        1 if np.sign(h) == np.sign(self.lines.histogram[0])
                        else 0
                        for h in self.histogram_history[-5:]
                    ]) if len(self.histogram_history) >= 5
                    else 0
                )
            }
        }
