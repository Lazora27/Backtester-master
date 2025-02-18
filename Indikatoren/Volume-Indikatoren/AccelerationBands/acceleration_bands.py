import backtrader as bt
import numpy as np

class AccelerationBands(bt.Indicator):
    """
    Acceleration Bands
    
    Ein Indikator, der Preisbeschleunigung und potenzielle
    Trendwenden basierend auf Volatilität identifiziert.
    
    Features:
    - Volatilitätsbasierte Bänder
    - Beschleunigungsmessung
    - Trendstärkeanalyse
    - Adaptiver Multiplikator
    - Signal-Validierung
    
    Parameter:
    - period (20): Basisperiode
    - multiplier (2): Band-Multiplikator
    - volume_factor (1.0): Volumenfaktor
    """
    
    lines = ('upper', 'middle', 'lower',
             'acceleration', 'trend_strength',
             'volume_impact', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 20),
        ('multiplier', 2),
        ('volume_factor', 1.0),
        ('min_trend_strength', 0.3)
    )
    
    plotlines = dict(
        upper=dict(color='lightgray', _name='Upper Band'),
        middle=dict(color='gray', _name='Middle Band'),
        lower=dict(color='lightgray', _name='Lower Band'),
        acceleration=dict(color='blue', _name='Acceleration'),
        trend_strength=dict(color='purple', _name='Trend Strength'),
        volume_impact=dict(color='green', _name='Volume Impact'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(AccelerationBands, self).__init__()
        
        # Technische Indikatoren
        self.sma = bt.indicators.SMA(period=self.p.period)
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.price_history = []
        self.volume_history = []
        self.acceleration_history = []
        
    def calculate_bands(self):
        """
        Berechnet die Beschleunigungsbänder.
        """
        # Mittleres Band (SMA)
        middle = self.sma[0]
        
        # Volatilitätskomponente
        volatility = self.atr[0] * self.p.multiplier
        
        # Volumeneinfluss
        volume_impact = 1.0
        if len(self.volume_history) >= self.p.period:
            avg_volume = np.mean(self.volume_history[-self.p.period:])
            if avg_volume > 0:
                volume_impact = (self.data.volume[0] / avg_volume) ** self.p.volume_factor
                
        # Bandbreite anpassen
        band_width = volatility * volume_impact
        
        # Bänder berechnen
        upper = middle + band_width
        lower = middle - band_width
        
        return upper, middle, lower
        
    def calculate_acceleration(self):
        """
        Berechnet die Preisbeschleunigung.
        """
        if len(self.price_history) < 3:
            return 0
            
        # Erste Ableitung (Geschwindigkeit)
        velocity_current = self.price_history[-1] - self.price_history[-2]
        velocity_previous = self.price_history[-2] - self.price_history[-3]
        
        # Zweite Ableitung (Beschleunigung)
        acceleration = velocity_current - velocity_previous
        
        # Normalisierung
        if self.data[0] != 0:
            acceleration = acceleration / self.data[0]
            
        return acceleration
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.acceleration_history) < self.p.period:
            return 0
            
        # Durchschnittliche Beschleunigung
        avg_acceleration = np.mean(self.acceleration_history[-self.p.period:])
        
        # Beschleunigungskonsistenz
        acceleration_consistency = np.sum(
            1 if (acc > 0 and avg_acceleration > 0) or
               (acc < 0 and avg_acceleration < 0)
            else 0
            for acc in self.acceleration_history[-self.p.period:]
        ) / self.p.period
        
        return acceleration_consistency
        
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.data[0])
        self.volume_history.append(self.data.volume[0])
        
        # Bänder berechnen
        upper, middle, lower = self.calculate_bands()
        self.lines.upper[0] = upper
        self.lines.middle[0] = middle
        self.lines.lower[0] = lower
        
        # Beschleunigung berechnen
        acceleration = self.calculate_acceleration()
        self.lines.acceleration[0] = acceleration
        self.acceleration_history.append(acceleration)
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volumeneinfluss
        if len(self.volume_history) >= self.p.period:
            avg_volume = np.mean(self.volume_history[-self.p.period:])
            if avg_volume > 0:
                self.lines.volume_impact[0] = (
                    self.data.volume[0] / avg_volume
                )
        else:
            self.lines.volume_impact[0] = 1.0
            
        # Historie begrenzen
        max_period = max(self.p.period, 3)
        for hist in [self.price_history, self.volume_history,
                    self.acceleration_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.data[0] <= self.lines.lower[0] and
            self.lines.acceleration[0] > 0 and
            self.lines.trend_strength[0] > self.p.min_trend_strength and
            self.lines.volume_impact[0] > 1.0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.data[0] >= self.lines.upper[0] and
            self.lines.acceleration[0] < 0 and
            self.lines.trend_strength[0] > self.p.min_trend_strength and
            self.lines.volume_impact[0] > 1.0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'bands': {
                'upper': self.lines.upper[0],
                'middle': self.lines.middle[0],
                'lower': self.lines.lower[0],
                'width': self.lines.upper[0] - self.lines.lower[0]
            },
            'acceleration': {
                'current': self.lines.acceleration[0],
                'average': (
                    np.mean(self.acceleration_history)
                    if self.acceleration_history
                    else 0
                ),
                'trend': (
                    'accelerating' if self.lines.acceleration[0] > 0
                    else 'decelerating'
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'consistency': (
                    np.mean([
                        1 if acc > 0
                        else -1 if acc < 0
                        else 0
                        for acc in self.acceleration_history[-5:]
                    ]) if len(self.acceleration_history) >= 5
                    else 0
                )
            },
            'volume': {
                'impact': self.lines.volume_impact[0],
                'trend': (
                    'increasing' if self.lines.volume_impact[0] > 1
                    else 'decreasing'
                ),
                'significance': abs(self.lines.volume_impact[0] - 1)
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    self.lines.trend_strength[0] *
                    abs(self.lines.acceleration[0]) *
                    self.lines.volume_impact[0]
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'band_stability': (
                    np.std([
                        self.lines.upper[0] - self.lines.lower[0]
                        for _ in range(min(5, len(self.price_history)))
                    ]) if len(self.price_history) > 0
                    else 0
                ),
                'acceleration_stability': (
                    np.std(self.acceleration_history)
                    if len(self.acceleration_history) > 1
                    else 0
                )
            }
        }
