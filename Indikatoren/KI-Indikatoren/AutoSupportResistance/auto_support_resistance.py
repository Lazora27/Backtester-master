import backtrader as bt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from collections import defaultdict

class AutoSupportResistance(bt.Indicator):
    """
    Auto Support & Resistance Finder
    
    Ein KI-basierter Indikator zur automatischen
    Erkennung von Support- und Resistanzzonen.
    
    Features:
    - KI-gestützte Zonenerkennung
    - Dynamische Levelanpassung
    - Stärkeanalyse
    - Signalgenerierung
    
    Parameter:
    - zone_period (50): Zonenperiode
    - n_levels (5): Anzahl der Levels
    - strength_threshold (0.7): Stärkeschwelle
    """
    
    lines = ('support_level', 'resistance_level',
             'zone_strength', 'zone_quality',
             'signal')
             
    params = (
        ('zone_period', 50),
        ('n_levels', 5),
        ('strength_threshold', 0.7)
    )
    
    plotlines = dict(
        support_level=dict(color='green', _name='Support Level'),
        resistance_level=dict(color='red', _name='Resistance Level'),
        zone_strength=dict(color='blue', _name='Zone Strength'),
        zone_quality=dict(color='purple', _name='Zone Quality'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(AutoSupportResistance, self).__init__()
        
        # KI-Komponenten
        self.scaler = StandardScaler()
        self.clusterer = KMeans(
            n_clusters=self.p.n_levels
        )
        
        # Level Tracking
        self.price_history = []
        self.volume_history = []
        self.level_history = []
        self.strength_history = []
        
    def find_levels(self):
        """
        Findet Support- und Resistanzlevel.
        """
        if len(self.price_history) < self.p.zone_period:
            return [], 0
            
        # Preisdaten vorbereiten
        prices = np.array(self.price_history).reshape(-1, 1)
        prices_scaled = self.scaler.fit_transform(prices)
        
        # Clustering durchführen
        clusters = self.clusterer.fit_predict(prices_scaled)
        centers = self.scaler.inverse_transform(
            self.clusterer.cluster_centers_
        )
        
        # Level sortieren
        levels = sorted(centers.flatten())
        
        # Qualität berechnen
        inertia = self.clusterer.inertia_
        quality = 1 / (1 + inertia)
        
        return levels, quality
        
    def calculate_zone_strength(self, levels):
        """
        Berechnet die Stärke der Zonen.
        """
        if not levels:
            return 0
            
        current_price = self.price_history[-1]
        
        # Nächste Level finden
        distances = [abs(level - current_price)
                    for level in levels]
        closest_idx = np.argmin(distances)
        
        # Stärke basierend auf Distanz und Volumen
        strength = 1 / (1 + min(distances))
        if self.volume_history:
            volume_factor = (
                self.volume_history[-1] /
                np.mean(self.volume_history)
            )
            strength *= volume_factor
            
        self.strength_history.append(strength)
        return strength
        
    def find_support_resistance(self, levels, current_price):
        """
        Findet aktuelle Support- und Resistanzlevel.
        """
        if not levels:
            return current_price, current_price
            
        # Level unter und über aktuellem Preis
        support_levels = [l for l in levels if l < current_price]
        resistance_levels = [l for l in levels if l > current_price]
        
        support = max(support_levels) if support_levels else current_price
        resistance = min(resistance_levels) if resistance_levels else current_price
        
        return support, resistance
        
    def calculate_zone_quality(self, quality):
        """
        Berechnet die Qualität der Zonen.
        """
        if not self.strength_history:
            return quality
            
        # Qualität basierend auf Historie
        historical_strength = np.mean(
            self.strength_history[-self.p.n_levels:]
        )
        return (quality + historical_strength) / 2
        
    def next(self):
        # Preis und Volumen speichern
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        self.price_history.append(price)
        self.volume_history.append(volume)
        
        # Level finden
        levels, base_quality = self.find_levels()
        
        if levels:
            # Support und Resistanz bestimmen
            support, resistance = self.find_support_resistance(
                levels, price
            )
            
            # Stärke und Qualität berechnen
            zone_strength = self.calculate_zone_strength(levels)
            zone_quality = self.calculate_zone_quality(base_quality)
            
            # Level speichern
            self.level_history.append({
                'support': support,
                'resistance': resistance,
                'strength': zone_strength,
                'quality': zone_quality
            })
            
            # Linien aktualisieren
            self.lines.support_level[0] = support
            self.lines.resistance_level[0] = resistance
            self.lines.zone_strength[0] = zone_strength
            self.lines.zone_quality[0] = zone_quality
            
            # Signal
            if zone_strength > self.p.strength_threshold:
                if (price <= support * 1.01 and
                    zone_quality > 0.5):
                    self.lines.signal[0] = 1  # Kaufsignal
                elif (price >= resistance * 0.99 and
                      zone_quality > 0.5):
                    self.lines.signal[0] = -1  # Verkaufssignal
                else:
                    self.lines.signal[0] = 0
            else:
                self.lines.signal[0] = 0
        else:
            # Standardwerte
            self.lines.support_level[0] = price
            self.lines.resistance_level[0] = price
            self.lines.zone_strength[0] = 0
            self.lines.zone_quality[0] = 0
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_length = max(
            self.p.zone_period,
            len(self.data)
        )
        for hist in [self.price_history,
                    self.volume_history,
                    self.strength_history]:
            if len(hist) > max_length:
                hist.pop(0)
                
        if len(self.level_history) > max_length:
            self.level_history.pop(0)
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'zone_metrics': {
                'support': self.lines.support_level[0],
                'resistance': self.lines.resistance_level[0],
                'strength': self.lines.zone_strength[0],
                'quality': self.lines.zone_quality[0]
            },
            'level_analysis': {
                'support_distance': (
                    self.data.close[0] -
                    self.lines.support_level[0]
                ),
                'resistance_distance': (
                    self.lines.resistance_level[0] -
                    self.data.close[0]
                ),
                'zone_width': (
                    self.lines.resistance_level[0] -
                    self.lines.support_level[0]
                )
            },
            'strength_analysis': {
                'current': self.lines.zone_strength[0],
                'trend': (
                    'increasing'
                    if len(self.strength_history) > 1 and
                    self.strength_history[-1] >
                    self.strength_history[-2]
                    else 'decreasing'
                ),
                'stability': (
                    'stable'
                    if len(self.strength_history) > 1 and
                    np.std(self.strength_history[-5:]) < 0.2
                    else 'volatile'
                )
            },
            'quality_analysis': {
                'level': (
                    'high'
                    if self.lines.zone_quality[0] > 0.7
                    else 'moderate'
                    if self.lines.zone_quality[0] > 0.4
                    else 'low'
                ),
                'consistency': (
                    'consistent'
                    if len(self.level_history) > 1 and
                    all(abs(l['quality'] -
                           self.lines.zone_quality[0]) < 0.2
                        for l in self.level_history[-3:])
                    else 'inconsistent'
                ),
                'reliability': (
                    self.lines.zone_quality[0] *
                    self.lines.zone_strength[0]
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
                    self.lines.zone_quality[0] *
                    self.lines.zone_strength[0]
                )
            },
            'market_conditions': {
                'zone_quality': (
                    'high'
                    if self.lines.zone_quality[0] > 0.7
                    else 'moderate'
                    if self.lines.zone_quality[0] > 0.4
                    else 'low'
                ),
                'level_clarity': (
                    'clear'
                    if self.lines.zone_strength[0] >
                       self.p.strength_threshold
                    else 'unclear'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.zone_strength[0] >
                        self.p.strength_threshold and
                        self.lines.zone_quality[0] > 0.5)
                    else 'unfavorable'
                )
            }
        }
