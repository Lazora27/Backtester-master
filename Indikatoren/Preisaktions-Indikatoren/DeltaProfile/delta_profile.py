import backtrader as bt
import numpy as np
from collections import defaultdict

class DeltaProfile(bt.Indicator):
    """
    Delta Profile Indicator
    
    Ein fortgeschrittener Indikator zur Analyse der
    Preisebenen-spezifischen Volumendeltas.
    
    Features:
    - Preisniveau-Analyse
    - Delta-Profil-Erstellung
    - Volumencluster-Erkennung
    - Signalgenerierung
    
    Parameter:
    - price_levels (50): Anzahl der Preisebenen
    - volume_threshold (1000): Volumenschwelle
    - profile_period (20): Profilperiode
    """
    
    lines = ('delta_value', 'profile_strength',
             'level_imbalance', 'volume_cluster',
             'signal')
             
    params = (
        ('price_levels', 50),
        ('volume_threshold', 1000),
        ('profile_period', 20)
    )
    
    plotlines = dict(
        delta_value=dict(color='blue', _name='Delta Value'),
        profile_strength=dict(color='red', _name='Profile Strength'),
        level_imbalance=dict(color='green', _name='Level Imbalance'),
        volume_cluster=dict(color='purple', _name='Volume Cluster'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(DeltaProfile, self).__init__()
        
        # Historie
        self.price_history = []
        self.volume_history = []
        self.delta_profiles = []
        
        # Level-Tracking
        self.level_volumes = defaultdict(float)
        self.level_deltas = defaultdict(float)
        
    def get_price_level(self, price):
        """
        Ordnet einen Preis einer Preisebene zu.
        """
        if not self.price_history:
            return 0
            
        price_range = max(self.price_history) - min(self.price_history)
        if price_range == 0:
            return 0
            
        level_size = price_range / self.p.price_levels
        return int((price - min(self.price_history)) / level_size)
        
    def update_level_data(self, price, volume, is_buying):
        """
        Aktualisiert die Level-Daten.
        """
        level = self.get_price_level(price)
        
        # Volumen und Delta aktualisieren
        self.level_volumes[level] += volume
        self.level_deltas[level] += (
            volume if is_buying else -volume
        )
        
    def calculate_profile_strength(self):
        """
        Berechnet die Profilstärke.
        """
        if not self.level_volumes:
            return 0
            
        # Durchschnittliches Level-Volumen
        avg_volume = (
            sum(self.level_volumes.values()) /
            len(self.level_volumes)
        )
        
        if avg_volume == 0:
            return 0
            
        # Standardabweichung der Level-Volumen
        variance = sum(
            (v - avg_volume) ** 2
            for v in self.level_volumes.values()
        ) / len(self.level_volumes)
        
        return np.sqrt(variance) / avg_volume
        
    def calculate_level_imbalance(self):
        """
        Berechnet das Level-Ungleichgewicht.
        """
        if not self.level_deltas:
            return 0
            
        current_level = self.get_price_level(
            self.price_history[-1]
        )
        
        # Delta des aktuellen Levels
        current_delta = self.level_deltas.get(
            current_level,
            0
        )
        
        if current_delta == 0:
            return 0
            
        # Verhältnis zum Gesamtvolumen
        total_volume = self.level_volumes.get(
            current_level,
            1
        )
        
        return current_delta / total_volume
        
    def find_volume_cluster(self):
        """
        Findet Volumencluster.
        """
        if not self.level_volumes:
            return 0
            
        current_level = self.get_price_level(
            self.price_history[-1]
        )
        
        # Cluster-Stärke berechnen
        cluster_strength = 0
        for level in range(
            current_level - 2,
            current_level + 3
        ):
            cluster_strength += self.level_volumes.get(
                level,
                0
            )
            
        return cluster_strength / self.p.volume_threshold
        
    def next(self):
        # Preis und Volumen speichern
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        self.price_history.append(price)
        self.volume_history.append(volume)
        
        # Level-Daten aktualisieren
        is_buying = price > self.price_history[-2] if len(self.price_history) > 1 else True
        self.update_level_data(price, volume, is_buying)
        
        # Metriken berechnen
        profile_strength = self.calculate_profile_strength()
        level_imbalance = self.calculate_level_imbalance()
        volume_cluster = self.find_volume_cluster()
        
        # Delta-Wert
        delta_value = level_imbalance * profile_strength
        
        # Linien aktualisieren
        self.lines.delta_value[0] = delta_value
        self.lines.profile_strength[0] = profile_strength
        self.lines.level_imbalance[0] = level_imbalance
        self.lines.volume_cluster[0] = volume_cluster
        
        # Signal
        if volume_cluster > 1.0:
            if level_imbalance > 0.2:
                self.lines.signal[0] = 1  # Kaufsignal
            elif level_imbalance < -0.2:
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        if len(self.price_history) > self.p.profile_period:
            self.price_history.pop(0)
            self.volume_history.pop(0)
            
            # Level-Daten zurücksetzen
            if len(self.price_history) % 10 == 0:
                self.level_volumes.clear()
                self.level_deltas.clear()
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'profile': {
                'delta': self.lines.delta_value[0],
                'strength': self.lines.profile_strength[0],
                'imbalance': self.lines.level_imbalance[0],
                'cluster': self.lines.volume_cluster[0]
            },
            'level_analysis': {
                'current_level': self.get_price_level(
                    self.price_history[-1]
                ),
                'volume_distribution': {
                    str(level): volume
                    for level, volume
                    in self.level_volumes.items()
                },
                'delta_distribution': {
                    str(level): delta
                    for level, delta
                    in self.level_deltas.items()
                }
            },
            'cluster_analysis': {
                'strength': self.lines.volume_cluster[0],
                'significance': (
                    'significant'
                    if self.lines.volume_cluster[0] > 1.2
                    else 'moderate'
                    if self.lines.volume_cluster[0] > 0.8
                    else 'weak'
                ),
                'context': (
                    'accumulation'
                    if self.lines.level_imbalance[0] > 0.1
                    else 'distribution'
                    if self.lines.level_imbalance[0] < -0.1
                    else 'neutral'
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
                    self.lines.volume_cluster[0] *
                    abs(self.lines.level_imbalance[0])
                )
            },
            'market_conditions': {
                'profile_quality': (
                    'high'
                    if self.lines.profile_strength[0] > 0.5
                    else 'low'
                ),
                'level_activity': (
                    'active'
                    if self.lines.volume_cluster[0] > 1.0
                    else 'inactive'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.volume_cluster[0] > 1.0 and
                        abs(self.lines.level_imbalance[0]) > 0.15)
                    else 'unfavorable'
                )
            }
        }
