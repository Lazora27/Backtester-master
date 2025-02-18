import backtrader as bt
import numpy as np

class CCITurbo(bt.Indicator):
    """
    CCI Turbo Indicator
    
    Eine erweiterte Version des Commodity Channel Index (CCI)
    mit zusätzlichen Momentum- und Trendanalysen.
    
    Features:
    - Erweiterte CCI-Berechnung
    - Momentum-Analyse
    - Trendstärkeberechnung
    - Signalgenerierung
    
    Parameter:
    - period (20): CCI Periode
    - factor (0.015): CCI Faktor
    - turbo_factor (2.0): Turbo-Beschleunigungsfaktor
    - smooth_period (10): Glättungsperiode
    """
    
    lines = ('cci', 'turbo_cci',
             'trend_strength', 'momentum',
             'signal')
             
    params = (
        ('period', 20),
        ('factor', 0.015),
        ('turbo_factor', 2.0),
        ('smooth_period', 10)
    )
    
    plotlines = dict(
        cci=dict(color='blue', _name='CCI'),
        turbo_cci=dict(color='red', _name='Turbo CCI'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        momentum=dict(color='purple', _name='Momentum'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(CCITurbo, self).__init__()
        
        # Historie
        self.cci_history = []
        self.price_history = []
        
    def calculate_typical_price(self):
        """
        Berechnet den typischen Preis.
        """
        return (
            self.data.high[0] +
            self.data.low[0] +
            self.data.close[0]
        ) / 3
        
    def calculate_cci(self):
        """
        Berechnet den CCI.
        """
        if len(self.data) < self.p.period:
            return 0
            
        typical_prices = [
            (self.data.high[-i] +
             self.data.low[-i] +
             self.data.close[-i]) / 3
            for i in range(self.p.period)
        ]
        
        sma = np.mean(typical_prices)
        mean_deviation = np.mean([
            abs(price - sma)
            for price in typical_prices
        ])
        
        if mean_deviation == 0:
            return 0
            
        return (
            (typical_prices[0] - sma) /
            (self.p.factor * mean_deviation)
        )
        
    def calculate_turbo_cci(self, cci):
        """
        Berechnet den Turbo-CCI.
        """
        if len(self.cci_history) < 2:
            return cci
            
        momentum = (
            cci -
            self.cci_history[-1]
        )
        
        return (
            cci +
            momentum * self.p.turbo_factor
        )
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.cci_history) < 2:
            return 0
            
        return (
            self.cci_history[-1] -
            self.cci_history[-2]
        )
        
    def calculate_momentum(self):
        """
        Berechnet das Momentum.
        """
        if len(self.price_history) < self.p.period:
            return 0
            
        return (
            self.price_history[-1] -
            self.price_history[-self.p.period]
        )
        
    def next(self):
        # CCI berechnen
        cci = self.calculate_cci()
        self.cci_history.append(cci)
        self.lines.cci[0] = cci
        
        # Preis speichern
        self.price_history.append(self.data.close[0])
        
        # Turbo CCI
        self.lines.turbo_cci[0] = self.calculate_turbo_cci(cci)
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Momentum
        self.lines.momentum[0] = self.calculate_momentum()
        
        # Signal
        if abs(self.lines.turbo_cci[0]) > 100:
            if (self.lines.turbo_cci[0] > 100 and
                self.lines.trend_strength[0] > 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (self.lines.turbo_cci[0] < -100 and
                  self.lines.trend_strength[0] < 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.smooth_period
        )
        for hist in [self.cci_history,
                    self.price_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'cci': {
                'value': self.lines.cci[0],
                'turbo': self.lines.turbo_cci[0],
                'state': (
                    'overbought'
                    if self.lines.turbo_cci[0] > 100
                    else 'oversold'
                    if self.lines.turbo_cci[0] < -100
                    else 'neutral'
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': (
                    'up' if self.lines.trend_strength[0] > 0
                    else 'down'
                ),
                'quality': (
                    abs(self.lines.trend_strength[0])
                    if abs(self.lines.trend_strength[0]) <= 1
                    else 1
                )
            },
            'momentum': {
                'value': self.lines.momentum[0],
                'direction': (
                    'up' if self.lines.momentum[0] > 0
                    else 'down'
                ),
                'strength': abs(self.lines.momentum[0])
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'reliability': (
                    abs(self.lines.trend_strength[0]) *
                    abs(self.lines.momentum[0])
                    if abs(self.lines.momentum[0]) <= 1
                    else abs(self.lines.trend_strength[0])
                )
            },
            'market_state': {
                'cci_condition': (
                    'extreme_high'
                    if self.lines.turbo_cci[0] > 200
                    else 'extreme_low'
                    if self.lines.turbo_cci[0] < -200
                    else 'high'
                    if self.lines.turbo_cci[0] > 100
                    else 'low'
                    if self.lines.turbo_cci[0] < -100
                    else 'normal'
                ),
                'trend_confirmation': (
                    'confirmed'
                    if (self.lines.trend_strength[0] > 0 and
                        self.lines.momentum[0] > 0) or
                       (self.lines.trend_strength[0] < 0 and
                        self.lines.momentum[0] < 0)
                    else 'divergent'
                ),
                'market_strength': (
                    'strong'
                    if abs(self.lines.turbo_cci[0]) > 150
                    else 'weak'
                )
            }
        }
