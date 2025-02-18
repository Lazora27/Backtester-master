import backtrader as bt
import numpy as np

class ParabolicTimePrice(bt.Indicator):
    """
    Parabolic Time Price Indicator
    
    Ein fortgeschrittener Indikator, der parabolische Zeitpreismuster
    identifiziert und analysiert.
    
    Features:
    - Parabolische Zeitpreisanalyse
    - Adaptive Beschleunigungsberechnung
    - Trendwechselerkennung
    - Signalgenerierung
    
    Parameter:
    - acceleration (0.02): Beschleunigungsfaktor
    - max_acceleration (0.2): Maximaler Beschleunigungsfaktor
    - time_period (20): Zeitperiode
    """
    
    lines = ('parabolic', 'acceleration',
             'trend', 'reversal_points',
             'signal')
             
    params = (
        ('acceleration', 0.02),
        ('max_acceleration', 0.2),
        ('time_period', 20)
    )
    
    plotlines = dict(
        parabolic=dict(color='blue', _name='Parabolic'),
        acceleration=dict(color='red', _name='Acceleration'),
        trend=dict(color='green', _name='Trend'),
        reversal_points=dict(color='purple', _name='Reversal Points'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(ParabolicTimePrice, self).__init__()
        
        # Historie
        self.price_history = []
        self.parabolic_history = []
        self.acceleration_factor = self.p.acceleration
        
        # Extreme Punkte
        self.extreme_point = self.data.close[0]
        self.is_long = True
        
    def calculate_parabolic(self):
        """
        Berechnet den parabolischen Wert.
        """
        if len(self.price_history) < 2:
            return self.data.close[0]
            
        prev_sar = self.parabolic_history[-1]
        current_price = self.price_history[-1]
        
        if self.is_long:
            sar = prev_sar + self.acceleration_factor * (
                self.extreme_point - prev_sar
            )
            # SAR kann nicht über dem Low liegen
            sar = min(sar, min(
                self.data.low.get(ago=-1, size=2)
            ))
        else:
            sar = prev_sar - self.acceleration_factor * (
                prev_sar - self.extreme_point
            )
            # SAR kann nicht unter dem High liegen
            sar = max(sar, max(
                self.data.high.get(ago=-1, size=2)
            ))
            
        return sar
        
    def update_acceleration(self):
        """
        Aktualisiert den Beschleunigungsfaktor.
        """
        if self.is_long:
            if self.data.high[0] > self.extreme_point:
                self.extreme_point = self.data.high[0]
                self.acceleration_factor = min(
                    self.acceleration_factor +
                    self.p.acceleration,
                    self.p.max_acceleration
                )
        else:
            if self.data.low[0] < self.extreme_point:
                self.extreme_point = self.data.low[0]
                self.acceleration_factor = min(
                    self.acceleration_factor +
                    self.p.acceleration,
                    self.p.max_acceleration
                )
                
    def check_reversal(self, sar):
        """
        Überprüft auf Trendumkehr.
        """
        if self.is_long:
            if self.data.low[0] < sar:
                self.is_long = False
                self.acceleration_factor = self.p.acceleration
                self.extreme_point = self.data.low[0]
                return True
        else:
            if self.data.high[0] > sar:
                self.is_long = True
                self.acceleration_factor = self.p.acceleration
                self.extreme_point = self.data.high[0]
                return True
        return False
        
    def next(self):
        # Preis speichern
        self.price_history.append(self.data.close[0])
        
        # Parabolischen Wert berechnen
        if self.parabolic_history:
            parabolic = self.calculate_parabolic()
        else:
            parabolic = self.data.close[0]
            
        self.parabolic_history.append(parabolic)
        
        # Beschleunigung aktualisieren
        self.update_acceleration()
        
        # Trendumkehr prüfen
        reversal = self.check_reversal(parabolic)
        
        # Linien aktualisieren
        self.lines.parabolic[0] = parabolic
        self.lines.acceleration[0] = self.acceleration_factor
        self.lines.trend[0] = 1 if self.is_long else -1
        self.lines.reversal_points[0] = (
            self.data.close[0] if reversal else None
        )
        
        # Signal
        if reversal:
            self.lines.signal[0] = (
                1 if self.is_long else -1
            )
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = self.p.time_period
        for hist in [self.price_history,
                    self.parabolic_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'parabolic': {
                'value': self.lines.parabolic[0],
                'acceleration': self.lines.acceleration[0],
                'trend': (
                    'up' if self.is_long else 'down'
                ),
                'extreme_point': self.extreme_point
            },
            'trend_state': {
                'direction': (
                    'long' if self.is_long else 'short'
                ),
                'strength': (
                    self.acceleration_factor /
                    self.p.max_acceleration
                ),
                'momentum': (
                    'increasing'
                    if self.acceleration_factor >
                       self.p.acceleration
                    else 'stable'
                )
            },
            'reversal': {
                'occurred': bool(
                    self.lines.reversal_points[0]
                ),
                'price': (
                    self.lines.reversal_points[0]
                    if self.lines.reversal_points[0]
                    else None
                ),
                'significance': (
                    'high'
                    if (self.acceleration_factor >
                        self.p.max_acceleration / 2)
                    else 'low'
                )
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'reliability': (
                    self.acceleration_factor /
                    self.p.max_acceleration
                )
            },
            'market_conditions': {
                'trend_quality': (
                    'strong'
                    if self.acceleration_factor >
                       self.p.max_acceleration / 2
                    else 'weak'
                ),
                'volatility': (
                    'high'
                    if len(self.price_history) >= 2 and
                       abs(self.price_history[-1] -
                           self.price_history[-2]) >
                       0.01 * self.price_history[-1]
                    else 'low'
                ),
                'trading_conditions': (
                    'favorable'
                    if (self.acceleration_factor >
                        self.p.max_acceleration / 3 and
                        not self.lines.reversal_points[0])
                    else 'unfavorable'
                )
            }
        }
