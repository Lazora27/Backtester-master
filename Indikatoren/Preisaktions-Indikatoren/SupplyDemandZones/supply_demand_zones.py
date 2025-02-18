import backtrader as bt
import numpy as np
from collections import defaultdict

class SupplyDemandZones(bt.Indicator):
    """
    Supply & Demand Zones Indicator
    
    Ein fortgeschrittener Indikator zur Identifikation und
    Analyse von Angebots- und Nachfragezonen.
    
    Features:
    - Zonen-Identifikation
    - Stärkeanalyse
    - Zonenqualität
    - Signalgenerierung
    
    Parameter:
    - zone_period (50): Zonenberechnungsperiode
    - strength_threshold (0.7): Stärkeschwelle
    - zone_margin (0.002): Zonenmarge
    """
    
    lines = ('supply_level', 'demand_level',
             'zone_strength', 'zone_quality',
             'signal')
             
    params = (
        ('zone_period', 50),
        ('strength_threshold', 0.7),
        ('zone_margin', 0.002)
    )
    
    plotlines = dict(
        supply_level=dict(color='red', _name='Supply Level'),
        demand_level=dict(color='green', _name='Demand Level'),
        zone_strength=dict(color='blue', _name='Zone Strength'),
        zone_quality=dict(color='purple', _name='Zone Quality'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(SupplyDemandZones, self).__init__()
        
        # Zonen Tracking
        self.price_history = []
        self.volume_history = []
        self.supply_zones = []
        self.demand_zones = []
        self.zone_tests = defaultdict(int)
        
    def identify_zones(self):
        """
        Identifiziert Angebots- und Nachfragezonen.
        """
        if len(self.price_history) < 3:
            return [], []
            
        supply_zones = []
        demand_zones = []
        
        for i in range(1, len(self.price_history) - 1):
            price = self.price_history[i]
            prev_price = self.price_history[i - 1]
            next_price = self.price_history[i + 1]
            volume = self.volume_history[i]
            
            # Zonengrenzen
            upper = price * (1 + self.p.zone_margin)
            lower = price * (1 - self.p.zone_margin)
            
            # Angebots- und Nachfragezonen identifizieren
            if (prev_price < price > next_price and
                volume > np.mean(self.volume_history)):
                supply_zones.append({
                    'price': price,
                    'volume': volume,
                    'upper': upper,
                    'lower': lower,
                    'index': i
                })
                
            if (prev_price > price < next_price and
                volume > np.mean(self.volume_history)):
                demand_zones.append({
                    'price': price,
                    'volume': volume,
                    'upper': upper,
                    'lower': lower,
                    'index': i
                })
                
        return supply_zones, demand_zones
        
    def calculate_zone_strength(self, zone):
        """
        Berechnet die Stärke einer Zone.
        """
        if not zone:
            return 0
            
        # Stärke basierend auf Volumen und Tests
        volume_ratio = zone['volume'] / np.mean(
            self.volume_history
        )
        test_factor = 1 + (
            self.zone_tests[zone['price']] * 0.1
        )
        
        return volume_ratio * test_factor
        
    def calculate_zone_quality(self, zones):
        """
        Berechnet die Qualität der Zonen.
        """
        if not zones:
            return 0
            
        # Qualität basierend auf Abstand und Stärke
        qualities = []
        current_price = self.price_history[-1]
        
        for zone in zones:
            distance = abs(
                current_price - zone['price']
            ) / zone['price']
            strength = self.calculate_zone_strength(zone)
            
            quality = strength * (1 - min(distance, 1))
            qualities.append(quality)
            
        return max(qualities) if qualities else 0
        
    def update_zone_tests(self, price):
        """
        Aktualisiert die Zonentests.
        """
        for zone in self.supply_zones + self.demand_zones:
            if (zone['lower'] <= price <= zone['upper']):
                self.zone_tests[zone['price']] += 1
                
    def next(self):
        # Preis und Volumen speichern
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        self.price_history.append(price)
        self.volume_history.append(volume)
        
        # Zonen identifizieren
        supply_zones, demand_zones = self.identify_zones()
        self.supply_zones = supply_zones
        self.demand_zones = demand_zones
        
        # Zonentests aktualisieren
        self.update_zone_tests(price)
        
        # Nächste Supply/Demand Level
        supply_level = (
            min(z['lower'] for z in supply_zones)
            if supply_zones else price
        )
        demand_level = (
            max(z['upper'] for z in demand_zones)
            if demand_zones else price
        )
        
        # Stärke und Qualität
        supply_strength = max(
            (self.calculate_zone_strength(z)
             for z in supply_zones),
            default=0
        )
        demand_strength = max(
            (self.calculate_zone_strength(z)
             for z in demand_zones),
            default=0
        )
        
        zone_strength = max(
            supply_strength,
            demand_strength
        )
        
        zone_quality = max(
            self.calculate_zone_quality(supply_zones),
            self.calculate_zone_quality(demand_zones)
        )
        
        # Linien aktualisieren
        self.lines.supply_level[0] = supply_level
        self.lines.demand_level[0] = demand_level
        self.lines.zone_strength[0] = zone_strength
        self.lines.zone_quality[0] = zone_quality
        
        # Signal
        if zone_strength > self.p.strength_threshold:
            if (price <= demand_level and
                zone_quality > 0.5):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (price >= supply_level and
                  zone_quality > 0.5):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        if len(self.price_history) > self.p.zone_period:
            self.price_history.pop(0)
            self.volume_history.pop(0)
            
        # Alte Zonen entfernen
        current_index = len(self.price_history) - 1
        self.supply_zones = [
            z for z in self.supply_zones
            if current_index - z['index'] < self.p.zone_period
        ]
        self.demand_zones = [
            z for z in self.demand_zones
            if current_index - z['index'] < self.p.zone_period
        ]
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'zones': {
                'supply': {
                    'level': self.lines.supply_level[0],
                    'count': len(self.supply_zones),
                    'strength': max(
                        (self.calculate_zone_strength(z)
                         for z in self.supply_zones),
                        default=0
                    )
                },
                'demand': {
                    'level': self.lines.demand_level[0],
                    'count': len(self.demand_zones),
                    'strength': max(
                        (self.calculate_zone_strength(z)
                         for z in self.demand_zones),
                        default=0
                    )
                }
            },
            'zone_analysis': {
                'strength': self.lines.zone_strength[0],
                'quality': self.lines.zone_quality[0],
                'distribution': (
                    'balanced'
                    if abs(len(self.supply_zones) -
                          len(self.demand_zones)) <= 2
                    else 'supply_heavy'
                    if len(self.supply_zones) >
                       len(self.demand_zones)
                    else 'demand_heavy'
                )
            },
            'zone_tests': {
                'total': sum(self.zone_tests.values()),
                'distribution': dict(self.zone_tests),
                'reliability': (
                    'high'
                    if any(v >= 3 for v in self.zone_tests.values())
                    else 'moderate'
                    if any(v >= 2 for v in self.zone_tests.values())
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
                    self.lines.zone_strength[0] *
                    self.lines.zone_quality[0]
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
                'zone_structure': (
                    'clear'
                    if (len(self.supply_zones) > 0 and
                        len(self.demand_zones) > 0)
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
