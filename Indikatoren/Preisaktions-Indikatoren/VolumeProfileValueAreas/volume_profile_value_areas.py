import backtrader as bt
import numpy as np
from collections import defaultdict

class VolumeProfileValueAreas(bt.Indicator):
    """
    Volume Profile Value Areas Indicator
    
    Ein fortgeschrittener Indikator zur Analyse der
    Wertbereiche im Volumprofil.
    
    Features:
    - Value Area Analyse
    - Bereichsidentifikation
    - Volumenverteilung
    - Signalgenerierung
    
    Parameter:
    - value_period (50): Wertbereichsperiode
    - area_threshold (0.7): Bereichsschwelle
    - distribution_levels (20): Verteilungsebenen
    """
    
    lines = ('value_high', 'value_low',
             'value_distribution', 'area_strength',
             'signal')
             
    params = (
        ('value_period', 50),
        ('area_threshold', 0.7),
        ('distribution_levels', 20)
    )
    
    plotlines = dict(
        value_high=dict(color='red', _name='Value High'),
        value_low=dict(color='green', _name='Value Low'),
        value_distribution=dict(color='blue', _name='Value Distribution'),
        area_strength=dict(color='purple', _name='Area Strength'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(VolumeProfileValueAreas, self).__init__()
        
        # Value Area Tracking
        self.price_levels = defaultdict(float)
        self.volume_profile = defaultdict(list)
        self.area_history = []
        self.distribution_history = []
        
    def update_value_area(self, price, volume):
        """
        Aktualisiert den Wertbereich.
        """
        level = self.get_price_level(price)
        
        # Volumen zum Level hinzufügen
        self.price_levels[level] += volume
        self.volume_profile[level].append(volume)
        
    def get_price_level(self, price):
        """
        Ordnet einen Preis einer Preisebene zu.
        """
        return round(price, 2)
        
    def calculate_value_area(self):
        """
        Berechnet den Wertbereich.
        """
        if not self.price_levels:
            return 0, 0
            
        total_volume = sum(self.price_levels.values())
        target_volume = total_volume * self.p.area_threshold
        
        # Sortierte Levels nach Volumen
        sorted_levels = sorted(
            self.price_levels.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        # Value Area Grenzen finden
        cumulative_volume = 0
        included_levels = []
        
        for level, volume in sorted_levels:
            cumulative_volume += volume
            included_levels.append(level)
            
            if cumulative_volume >= target_volume:
                break
                
        value_area = {
            'high': max(included_levels),
            'low': min(included_levels),
            'levels': included_levels
        }
        
        self.area_history.append(value_area)
        return value_area['high'], value_area['low']
        
    def calculate_value_distribution(self):
        """
        Berechnet die Wertverteilung.
        """
        if not self.price_levels:
            return 0
            
        total_volume = sum(self.price_levels.values())
        if total_volume == 0:
            return 0
            
        # Verteilung über Levels
        distribution = []
        sorted_levels = sorted(self.price_levels.keys())
        
        for i in range(len(sorted_levels) - 1):
            current_level = sorted_levels[i]
            next_level = sorted_levels[i + 1]
            
            level_volume = (
                self.price_levels[current_level] +
                self.price_levels[next_level]
            )
            distribution.append(level_volume / total_volume)
            
        self.distribution_history.append(distribution)
        return np.mean(distribution) if distribution else 0
        
    def calculate_area_strength(self):
        """
        Berechnet die Bereichsstärke.
        """
        if not self.area_history:
            return 0
            
        current_area = self.area_history[-1]
        area_volume = sum(
            self.price_levels[level]
            for level in current_area['levels']
        )
        
        total_volume = sum(self.price_levels.values())
        if total_volume == 0:
            return 0
            
        return area_volume / total_volume
        
    def next(self):
        # Preis und Volumen speichern
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        # Wertbereich aktualisieren
        self.update_value_area(price, volume)
        
        # Bereichs-Metriken berechnen
        value_high, value_low = self.calculate_value_area()
        value_distribution = self.calculate_value_distribution()
        area_strength = self.calculate_area_strength()
        
        # Linien aktualisieren
        self.lines.value_high[0] = value_high
        self.lines.value_low[0] = value_low
        self.lines.value_distribution[0] = value_distribution
        self.lines.area_strength[0] = area_strength
        
        # Signal
        if area_strength > self.p.area_threshold:
            if (price < value_low and
                value_distribution > 0.5):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (price > value_high and
                  value_distribution > 0.5):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        if len(self.area_history) > self.p.value_period:
            self.area_history.pop(0)
            
        if len(self.distribution_history) > self.p.value_period:
            self.distribution_history.pop(0)
            
        # Alte Levels entfernen
        for level in list(self.volume_profile.keys()):
            while (len(self.volume_profile[level]) >
                   self.p.value_period):
                old_volume = self.volume_profile[level].pop(0)
                self.price_levels[level] -= old_volume
                
                if self.price_levels[level] <= 0:
                    del self.price_levels[level]
                    del self.volume_profile[level]
                    
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'value_area': {
                'high': self.lines.value_high[0],
                'low': self.lines.value_low[0],
                'width': (
                    self.lines.value_high[0] -
                    self.lines.value_low[0]
                ),
                'strength': self.lines.area_strength[0]
            },
            'distribution_analysis': {
                'current': self.lines.value_distribution[0],
                'levels': len(self.price_levels),
                'concentration': (
                    'high'
                    if len(self.price_levels) <
                       self.p.distribution_levels // 2
                    else 'moderate'
                    if len(self.price_levels) <
                       self.p.distribution_levels
                    else 'low'
                )
            },
            'area_analysis': {
                'structure': (
                    'defined'
                    if self.lines.area_strength[0] >
                       self.p.area_threshold
                    else 'undefined'
                ),
                'stability': (
                    'stable'
                    if len(self.area_history) > 1 and
                    all(a['high'] == self.area_history[-1]['high']
                        and a['low'] == self.area_history[-1]['low']
                        for a in self.area_history[-3:])
                    else 'volatile'
                ),
                'distribution': (
                    'even'
                    if self.lines.value_distribution[0] > 0.5
                    else 'uneven'
                )
            },
            'level_analysis': {
                'active_levels': len(self.price_levels),
                'value_levels': (
                    len(self.area_history[-1]['levels'])
                    if self.area_history else 0
                ),
                'distribution_quality': (
                    'high'
                    if self.lines.value_distribution[0] > 0.7
                    else 'moderate'
                    if self.lines.value_distribution[0] > 0.4
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
                    self.lines.area_strength[0] *
                    self.lines.value_distribution[0]
                )
            },
            'market_conditions': {
                'area_quality': (
                    'high'
                    if self.lines.area_strength[0] >
                       self.p.area_threshold
                    else 'low'
                ),
                'distribution_state': (
                    'favorable'
                    if self.lines.value_distribution[0] > 0.5
                    else 'unfavorable'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.area_strength[0] >
                        self.p.area_threshold and
                        self.lines.value_distribution[0] > 0.5)
                    else 'unfavorable'
                )
            }
        }
