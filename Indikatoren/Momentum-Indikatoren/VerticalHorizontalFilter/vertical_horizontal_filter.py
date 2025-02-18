import backtrader as bt
import numpy as np

class VerticalHorizontalFilter(bt.Indicator):
    """
    Vertical Horizontal Filter (VHF)
    
    Ein Indikator, der zwischen trendenden und seitwärts
    gerichteten Märkten unterscheidet.
    
    Features:
    - Trend vs. Range Erkennung
    - Adaptive Glättung
    - Trendstärke-Analyse
    - Marktphasen-Erkennung
    - Signal-Validierung
    
    Parameter:
    - period (28): Basisperiode
    - smooth_period (5): Glättungsperiode
    - trend_threshold (0.4): Trendschwelle
    """
    
    lines = ('vhf', 'smoothed_vhf',
             'trend_strength', 'market_phase',
             'upper', 'lower',
             'buy_signal', 'sell_signal')
             
    params = (
        ('period', 28),
        ('smooth_period', 5),
        ('trend_threshold', 0.4),
        ('upper_threshold', 0.6),
        ('lower_threshold', 0.2)
    )
    
    plotlines = dict(
        vhf=dict(color='blue', _name='VHF'),
        smoothed_vhf=dict(color='red', _name='Smoothed VHF'),
        trend_strength=dict(color='purple', _name='Trend Strength'),
        market_phase=dict(color='orange', _name='Market Phase'),
        upper=dict(color='gray', _name='Upper'),
        lower=dict(color='gray', _name='Lower'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(VerticalHorizontalFilter, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Historie
        self.vhf_history = []
        self.price_history = []
        self.phase_history = []
        
    def calculate_vhf(self):
        """
        Berechnet den VHF-Wert.
        """
        if len(self.price_history) < self.p.period:
            return 0
            
        # Höchster und niedrigster Preis
        highest = max(self.price_history[-self.p.period:])
        lowest = min(self.price_history[-self.p.period:])
        
        # Vertikale Bewegung
        vertical_movement = highest - lowest
        
        # Horizontale Bewegung (Summe der absoluten Preisänderungen)
        horizontal_movement = sum(
            abs(self.price_history[i] - self.price_history[i-1])
            for i in range(len(self.price_history)-1,
                         len(self.price_history)-self.p.period,
                         -1)
        )
        
        if horizontal_movement == 0:
            return 0
            
        return vertical_movement / horizontal_movement
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.vhf_history) < 2:
            return 0
            
        # VHF-Momentum
        momentum = self.vhf_history[-1] - self.vhf_history[-2]
        
        # Relative Stärke
        strength = abs(momentum)
        if self.data[0] != 0:
            strength = strength / self.data[0]
            
        return min(1.0, strength)
        
    def identify_market_phase(self):
        """
        Identifiziert die Marktphase.
        """
        if len(self.vhf_history) < self.p.smooth_period:
            return 0
            
        # Durchschnittlicher VHF
        avg_vhf = np.mean(self.vhf_history[-self.p.smooth_period:])
        
        # Trend vs. Range
        if avg_vhf > self.p.trend_threshold:
            # Aufwärtstrend oder Abwärtstrend
            if self.data[0] > self.data[-self.p.smooth_period]:
                return 1  # Aufwärtstrend
            else:
                return -1  # Abwärtstrend
        else:
            return 0  # Seitwärtsbewegung
            
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.data[0])
        
        # VHF berechnen
        self.lines.vhf[0] = self.calculate_vhf()
        self.vhf_history.append(self.lines.vhf[0])
        
        # Geglätteter VHF
        self.lines.smoothed_vhf[0] = bt.indicators.SMA(
            self.lines.vhf, period=self.p.smooth_period
        )[0]
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Marktphase
        self.lines.market_phase[0] = self.identify_market_phase()
        self.phase_history.append(self.lines.market_phase[0])
        
        # Bänder
        self.lines.upper[0] = self.p.upper_threshold
        self.lines.lower[0] = self.p.lower_threshold
        
        # Historie begrenzen
        max_period = max(self.p.period, self.p.smooth_period)
        for hist in [self.vhf_history, self.price_history, self.phase_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_vhf[0] > self.p.trend_threshold and
            self.lines.market_phase[0] > 0 and
            self.lines.trend_strength[0] > 0.3):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_vhf[0] > self.p.trend_threshold and
            self.lines.market_phase[0] < 0 and
            self.lines.trend_strength[0] > 0.3):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'filter': {
                'vhf': self.lines.vhf[0],
                'smoothed': self.lines.smoothed_vhf[0],
                'trend_strength': self.lines.trend_strength[0],
                'market_phase': (
                    'uptrend' if self.lines.market_phase[0] > 0
                    else 'downtrend' if self.lines.market_phase[0] < 0
                    else 'ranging'
                )
            },
            'trend': {
                'direction': self.lines.market_phase[0],
                'strength': self.lines.trend_strength[0],
                'consistency': (
                    np.mean([
                        1 if p == self.lines.market_phase[0]
                        else 0
                        for p in self.phase_history[-5:]
                    ]) if len(self.phase_history) >= 5
                    else 0
                )
            },
            'market': {
                'condition': (
                    'trending' if self.lines.smoothed_vhf[0] > self.p.trend_threshold
                    else 'ranging'
                ),
                'strength': abs(self.lines.smoothed_vhf[0]),
                'phase_stability': (
                    np.std(self.phase_history)
                    if len(self.phase_history) > 1
                    else 0
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    self.lines.trend_strength[0] *
                    abs(self.lines.market_phase[0]) *
                    self.lines.smoothed_vhf[0]
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'vhf_stability': (
                    np.std(self.vhf_history)
                    if len(self.vhf_history) > 1
                    else 0
                ),
                'phase_changes': (
                    sum(
                        1 if self.phase_history[i] != self.phase_history[i-1]
                        else 0
                        for i in range(1, len(self.phase_history))
                    ) if len(self.phase_history) > 1
                    else 0
                )
            }
        }
