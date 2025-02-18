import backtrader as bt
import numpy as np
from collections import defaultdict

class MarketDepthHeatmap(bt.Indicator):
    """
    Market Depth Heatmap Indicator
    
    Ein fortgeschrittener Indikator zur Visualisierung
    und Analyse der Markttiefe als Heatmap.
    
    Features:
    - Heatmap-Generierung
    - Tiefenanalyse
    - Hotspot-Erkennung
    - Signalgenerierung
    
    Parameter:
    - price_levels (20): Anzahl der Preisebenen
    - heat_threshold (2000): Wärmeschwelle
    - update_period (10): Aktualisierungsperiode
    """
    
    lines = ('heat_intensity', 'depth_concentration',
             'hotspot_strength', 'level_activity',
             'signal')
             
    params = (
        ('price_levels', 20),
        ('heat_threshold', 2000),
        ('update_period', 10)
    )
    
    plotlines = dict(
        heat_intensity=dict(color='blue', _name='Heat Intensity'),
        depth_concentration=dict(color='red', _name='Depth Concentration'),
        hotspot_strength=dict(color='green', _name='Hotspot Strength'),
        level_activity=dict(color='purple', _name='Level Activity'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(MarketDepthHeatmap, self).__init__()
        
        # Heatmap-Daten
        self.level_heat = defaultdict(float)
        self.level_volume = defaultdict(float)
        self.price_history = []
        self.hotspots = []
        
    def update_heatmap(self, price, volume):
        """
        Aktualisiert die Heatmap-Daten.
        """
        level = self.get_price_level(price)
        
        # Wärme und Volumen aktualisieren
        self.level_heat[level] += volume
        self.level_volume[level] += volume
        
        # Benachbarte Levels beeinflussen
        decay = 0.5
        for i in range(1, 3):
            self.level_heat[level + i] += volume * decay
            self.level_heat[level - i] += volume * decay
            decay *= 0.5
            
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
        
    def calculate_heat_intensity(self):
        """
        Berechnet die Wärmeintensität.
        """
        if not self.level_heat:
            return 0
            
        current_level = self.get_price_level(
            self.price_history[-1]
        )
        
        # Gewichtete Wärme um aktuellen Level
        weighted_heat = 0
        total_weight = 0
        
        for level, heat in self.level_heat.items():
            weight = 1 / (1 + abs(level - current_level))
            weighted_heat += heat * weight
            total_weight += weight
            
        return (
            weighted_heat /
            (total_weight * self.p.heat_threshold)
        )
        
    def calculate_depth_concentration(self):
        """
        Berechnet die Tiefenkonzentration.
        """
        if not self.level_volume:
            return 0
            
        volumes = list(self.level_volume.values())
        total_volume = sum(volumes)
        
        if total_volume == 0:
            return 0
            
        # Gini-Koeffizient der Volumenverteilung
        volumes.sort()
        n = len(volumes)
        concentration = sum(
            (2 * i - n - 1) * v
            for i, v in enumerate(volumes)
        ) / (n * total_volume)
        
        return (concentration + 1) / 2
        
    def detect_hotspots(self):
        """
        Erkennt Hotspots in der Heatmap.
        """
        if not self.level_heat:
            return 0
            
        # Lokale Maxima finden
        hotspots = []
        for level in self.level_heat:
            is_hotspot = True
            for i in range(-2, 3):
                if i != 0:
                    neighbor = self.level_heat.get(
                        level + i,
                        0
                    )
                    if neighbor >= self.level_heat[level]:
                        is_hotspot = False
                        break
                        
            if is_hotspot:
                hotspots.append((
                    level,
                    self.level_heat[level]
                ))
                
        self.hotspots = hotspots
        return len(hotspots)
        
    def calculate_level_activity(self):
        """
        Berechnet die Level-Aktivität.
        """
        if not self.level_volume:
            return 0
            
        current_level = self.get_price_level(
            self.price_history[-1]
        )
        
        # Aktivität um aktuellen Level
        activity = 0
        for level, volume in self.level_volume.items():
            if abs(level - current_level) <= 2:
                activity += volume
                
        return activity / self.p.heat_threshold
        
    def next(self):
        # Preis und Volumen speichern
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        self.price_history.append(price)
        
        # Heatmap aktualisieren
        self.update_heatmap(price, volume)
        
        # Metriken berechnen
        heat_intensity = self.calculate_heat_intensity()
        depth_concentration = self.calculate_depth_concentration()
        hotspot_strength = self.detect_hotspots()
        level_activity = self.calculate_level_activity()
        
        # Linien aktualisieren
        self.lines.heat_intensity[0] = heat_intensity
        self.lines.depth_concentration[0] = depth_concentration
        self.lines.hotspot_strength[0] = hotspot_strength
        self.lines.level_activity[0] = level_activity
        
        # Signal
        if level_activity > 1.0:
            if (heat_intensity > 0.8 and
                depth_concentration > 0.6):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (heat_intensity < 0.3 and
                  depth_concentration > 0.6):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        if len(self.price_history) > self.p.price_levels:
            self.price_history.pop(0)
            
        # Heatmap periodisch aktualisieren
        if len(self.data) % self.p.update_period == 0:
            # Wärme abkühlen lassen
            for level in self.level_heat:
                self.level_heat[level] *= 0.8
                
            # Inaktive Levels entfernen
            self.level_heat = defaultdict(
                float,
                {k: v for k, v in self.level_heat.items()
                 if v > self.p.heat_threshold * 0.1}
            )
            self.level_volume = defaultdict(
                float,
                {k: v for k, v in self.level_volume.items()
                 if v > self.p.heat_threshold * 0.1}
            )
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'heatmap': {
                'intensity': self.lines.heat_intensity[0],
                'concentration': self.lines.depth_concentration[0],
                'hotspots': len(self.hotspots),
                'activity': self.lines.level_activity[0]
            },
            'level_analysis': {
                'active_levels': len(self.level_heat),
                'hotspot_levels': [
                    level for level, _ in self.hotspots
                ],
                'heat_distribution': {
                    str(level): heat
                    for level, heat in self.level_heat.items()
                }
            },
            'concentration_analysis': {
                'value': self.lines.depth_concentration[0],
                'type': (
                    'concentrated'
                    if self.lines.depth_concentration[0] > 0.7
                    else 'distributed'
                ),
                'stability': (
                    'stable'
                    if len(self.hotspots) < 3
                    else 'volatile'
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
                    self.lines.heat_intensity[0] *
                    self.lines.depth_concentration[0]
                )
            },
            'market_conditions': {
                'heat_quality': (
                    'high'
                    if self.lines.heat_intensity[0] > 0.7
                    else 'low'
                ),
                'activity_state': (
                    'active'
                    if self.lines.level_activity[0] > 1.0
                    else 'inactive'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.heat_intensity[0] > 0.6 and
                        self.lines.depth_concentration[0] > 0.5)
                    else 'unfavorable'
                )
            }
        }
