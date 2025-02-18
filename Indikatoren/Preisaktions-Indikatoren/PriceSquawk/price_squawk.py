import backtrader as bt
import numpy as np
from collections import defaultdict

class PriceSquawk(bt.Indicator):
    """
    Price Squawk Indicator
    
    Ein fortgeschrittener Indikator zur Analyse von
    Preisbewegungen und deren Bedeutung.
    
    Features:
    - Preisbewegungsanalyse
    - Volatilitätserkennung
    - Preismuster-Identifikation
    - Signalgenerierung
    
    Parameter:
    - squawk_period (20): Squawk-Berechnungsperiode
    - volatility_threshold (0.002): Volatilitätsschwelle
    - pattern_length (5): Musterlänge
    """
    
    lines = ('price_activity', 'volatility_state',
             'pattern_strength', 'market_noise',
             'signal')
             
    params = (
        ('squawk_period', 20),
        ('volatility_threshold', 0.002),
        ('pattern_length', 5)
    )
    
    plotlines = dict(
        price_activity=dict(color='blue', _name='Price Activity'),
        volatility_state=dict(color='red', _name='Volatility State'),
        pattern_strength=dict(color='green', _name='Pattern Strength'),
        market_noise=dict(color='purple', _name='Market Noise'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(PriceSquawk, self).__init__()
        
        # Squawk Tracking
        self.price_history = []
        self.volatility_history = []
        self.pattern_history = []
        self.activity_levels = defaultdict(float)
        
    def calculate_price_activity(self):
        """
        Berechnet die Preisaktivität.
        """
        if len(self.price_history) < 2:
            return 0
            
        # Aktivität basierend auf Preisänderungen
        recent_changes = [
            abs(p2 - p1)
            for p1, p2 in zip(
                self.price_history[-self.p.squawk_period:],
                self.price_history[-self.p.squawk_period + 1:]
            )
        ]
        
        if not recent_changes:
            return 0
            
        return sum(recent_changes) / len(recent_changes)
        
    def calculate_volatility_state(self):
        """
        Berechnet den Volatilitätszustand.
        """
        if len(self.price_history) < self.p.pattern_length:
            return 0
            
        # Volatilität über Musterlänge
        prices = np.array(
            self.price_history[-self.p.pattern_length:]
        )
        returns = np.diff(prices) / prices[:-1]
        
        volatility = np.std(returns)
        self.volatility_history.append(volatility)
        
        # Normalisierte Volatilität
        if len(self.volatility_history) > 1:
            avg_volatility = np.mean(
                self.volatility_history[-self.p.squawk_period:]
            )
            if avg_volatility > 0:
                return volatility / avg_volatility
                
        return volatility / self.p.volatility_threshold
        
    def detect_price_pattern(self):
        """
        Erkennt Preismuster.
        """
        if len(self.price_history) < self.p.pattern_length:
            return 0
            
        # Muster der letzten n Perioden
        pattern = np.diff(
            self.price_history[-self.p.pattern_length:]
        )
        pattern = np.sign(pattern)
        
        # Muster-Stärke berechnen
        consecutive = 0
        max_consecutive = 0
        current_sign = pattern[0]
        
        for sign in pattern:
            if sign == current_sign:
                consecutive += 1
                max_consecutive = max(
                    max_consecutive,
                    consecutive
                )
            else:
                consecutive = 1
                current_sign = sign
                
        return max_consecutive / len(pattern)
        
    def calculate_market_noise(self):
        """
        Berechnet das Marktrauschen.
        """
        if len(self.price_history) < self.p.squawk_period:
            return 0
            
        prices = np.array(
            self.price_history[-self.p.squawk_period:]
        )
        
        # Trendlinie berechnen
        x = np.arange(len(prices))
        z = np.polyfit(x, prices, 1)
        trend = np.poly1d(z)(x)
        
        # Abweichung von Trendlinie
        noise = np.mean(np.abs(prices - trend))
        return noise / np.mean(prices)
        
    def next(self):
        # Preis speichern
        price = self.data.close[0]
        self.price_history.append(price)
        
        # Metriken berechnen
        price_activity = self.calculate_price_activity()
        volatility_state = self.calculate_volatility_state()
        pattern_strength = self.detect_price_pattern()
        market_noise = self.calculate_market_noise()
        
        # Aktivitätslevel aktualisieren
        time_bucket = len(self.data) // 5
        self.activity_levels[time_bucket] = price_activity
        
        # Linien aktualisieren
        self.lines.price_activity[0] = price_activity
        self.lines.volatility_state[0] = volatility_state
        self.lines.pattern_strength[0] = pattern_strength
        self.lines.market_noise[0] = market_noise
        
        # Signal
        if volatility_state > 1.0:
            if (pattern_strength > 0.6 and
                market_noise < 0.3):
                if price_activity > 0:
                    self.lines.signal[0] = 1  # Kaufsignal
                else:
                    self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.squawk_period,
            self.p.pattern_length
        )
        if len(self.price_history) > max_period:
            self.price_history.pop(0)
            
        if len(self.volatility_history) > max_period:
            self.volatility_history.pop(0)
            
        # Aktivitätslevel bereinigen
        current_bucket = len(self.data) // 5
        self.activity_levels = defaultdict(
            float,
            {k: v for k, v in self.activity_levels.items()
             if k >= current_bucket - 4}
        )
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'price_state': {
                'activity': self.lines.price_activity[0],
                'volatility': self.lines.volatility_state[0],
                'pattern': self.lines.pattern_strength[0],
                'noise': self.lines.market_noise[0]
            },
            'volatility_analysis': {
                'state': (
                    'high'
                    if self.lines.volatility_state[0] > 1.2
                    else 'normal'
                    if self.lines.volatility_state[0] > 0.8
                    else 'low'
                ),
                'trend': (
                    'increasing'
                    if len(self.volatility_history) > 1 and
                    self.volatility_history[-1] >
                    self.volatility_history[-2]
                    else 'decreasing'
                ),
                'stability': (
                    'stable'
                    if self.lines.market_noise[0] < 0.2
                    else 'unstable'
                )
            },
            'pattern_analysis': {
                'strength': self.lines.pattern_strength[0],
                'quality': (
                    'strong'
                    if self.lines.pattern_strength[0] > 0.7
                    else 'moderate'
                    if self.lines.pattern_strength[0] > 0.4
                    else 'weak'
                ),
                'context': (
                    'trending'
                    if self.lines.market_noise[0] < 0.25
                    else 'choppy'
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
                    self.lines.pattern_strength[0] *
                    (1 - self.lines.market_noise[0])
                )
            },
            'market_conditions': {
                'activity_quality': (
                    'high'
                    if self.lines.price_activity[0] >
                       self.p.volatility_threshold
                    else 'low'
                ),
                'pattern_quality': (
                    'clear'
                    if self.lines.pattern_strength[0] > 0.6
                    else 'unclear'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.volatility_state[0] > 1.0 and
                        self.lines.pattern_strength[0] > 0.5 and
                        self.lines.market_noise[0] < 0.3)
                    else 'unfavorable'
                )
            }
        }
