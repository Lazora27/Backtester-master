import backtrader as bt
import numpy as np
from enum import Enum
from collections import deque

class ZoneType(Enum):
    """Zonen-Typen"""
    SUPPLY = "Supply"
    DEMAND = "Demand"
    EQUILIBRIUM = "Equilibrium"

class ZoneStrength(Enum):
    """Zonen-Stärke"""
    WEAK = 1
    MODERATE = 2
    STRONG = 3
    VERY_STRONG = 4

class SupplyDemandLiquidityMap(bt.Indicator):
    """
    Supply/Demand Liquidity Map
    
    Ein fortgeschrittener Indikator zur Analyse von
    Angebots- und Nachfragezonen sowie Liquidität.
    
    Features:
    - Supply/Demand Zonen-Erkennung
    - Liquiditätsanalyse
    - Zonenqualitäts-Bewertung
    - Reaktionsanalyse
    - Zonenmigration
    
    Parameter:
    - zone_lookback (50): Rückblickperiode
    - min_zone_size (0.2): Min. Zonengröße
    - strength_threshold (0.6): Stärkeschwelle
    """
    
    lines = ('zone_signal', 'liquidity_score', 'strength')
    params = (
        ('zone_lookback', 50),
        ('min_zone_size', 0.2),
        ('strength_threshold', 0.6),
    )
    
    plotlines = dict(
        zone_signal=dict(color='blue', _name='Zone Signal'),
        liquidity_score=dict(color='green', _name='Liquidity'),
        strength=dict(color='red', _name='Strength')
    )
    
    def __init__(self):
        super(SupplyDemandLiquidityMap, self).__init__()
        
        # Zonen-Tracking
        self.zones = []
        
        # Preispuffer
        self.price_history = deque(maxlen=self.p.zone_lookback)
        self.volume_history = deque(maxlen=self.p.zone_lookback)
        
        # Reaktions-Tracking
        self.reactions = {}
        
    def identify_zone(self, candles):
        """Identifiziert Supply/Demand Zonen"""
        if len(candles) < 3:
            return None
            
        # Letzte 3 Kerzen analysieren
        c1, c2, c3 = candles[-3:]
        
        # Demand Zone (Unterstützung)
        if (c1['low'] < c2['low'] and
            c2['low'] < c3['low'] and
            c1['volume'] > np.mean([
                c['volume'] for c in candles[-10:]
            ])):
            
            return {
                'type': ZoneType.DEMAND,
                'level': c1['low'],
                'size': abs(c1['high'] - c1['low']),
                'volume': c1['volume'],
                'age': 0
            }
            
        # Supply Zone (Widerstand)
        elif (c1['high'] > c2['high'] and
              c2['high'] > c3['high'] and
              c1['volume'] > np.mean([
                  c['volume'] for c in candles[-10:]
              ])):
              
            return {
                'type': ZoneType.SUPPLY,
                'level': c1['high'],
                'size': abs(c1['high'] - c1['low']),
                'volume': c1['volume'],
                'age': 0
            }
            
        return None
        
    def calculate_zone_strength(self, zone):
        """Berechnet die Stärke einer Zone"""
        if not zone:
            return 0
            
        # Basis-Stärke
        strength = 1.0
        
        # Volumen-Faktor
        if self.volume_history:
            vol_factor = (
                zone['volume'] /
                np.mean(self.volume_history)
            )
            strength *= min(2, vol_factor)
            
        # Alters-Faktor
        age_factor = max(
            0.5,
            1 - (zone['age'] / self.p.zone_lookback)
        )
        strength *= age_factor
        
        # Reaktions-Faktor
        if zone['level'] in self.reactions:
            reaction_count = self.reactions[zone['level']]
            reaction_factor = min(
                2,
                1 + (reaction_count / 10)
            )
            strength *= reaction_factor
            
        return min(4, strength)
        
    def analyze_liquidity(self, price, volume):
        """Analysiert Liquidität an aktuellem Preis"""
        if not self.price_history:
            return 0
            
        # Volumengewichteter Durchschnittspreis
        vwap = np.average(
            self.price_history,
            weights=self.volume_history
        )
        
        # Preisabweichung
        deviation = abs(price - vwap) / vwap
        
        # Volumenanalyse
        vol_ratio = (
            volume /
            np.mean(self.volume_history)
        )
        
        # Liquiditätsscore
        score = (
            (1 - deviation) * 0.7 +
            min(1, vol_ratio) * 0.3
        )
        
        return score
        
    def update_zones(self, price):
        """Aktualisiert bestehende Zonen"""
        updated_zones = []
        
        for zone in self.zones:
            # Alter erhöhen
            zone['age'] += 1
            
            # Zone noch aktiv?
            if zone['age'] < self.p.zone_lookback:
                # Preis in Zone?
                if abs(price - zone['level']) < (
                    zone['size'] / 2
                ):
                    # Reaktion zählen
                    if zone['level'] not in self.reactions:
                        self.reactions[zone['level']] = 0
                    self.reactions[zone['level']] += 1
                    
                updated_zones.append(zone)
                
        self.zones = updated_zones
        
    def next(self):
        # Kerzen-Daten sammeln
        candle = {
            'open': self.data.open[0],
            'high': self.data.high[0],
            'low': self.data.low[0],
            'close': self.data.close[0],
            'volume': self.data.volume[0]
        }
        
        # Historie aktualisieren
        self.price_history.append(self.data.close[0])
        self.volume_history.append(self.data.volume[0])
        
        # Letzte Kerzen für Analyse
        candles = [
            {
                'open': self.data.open[-i],
                'high': self.data.high[-i],
                'low': self.data.low[-i],
                'close': self.data.close[-i],
                'volume': self.data.volume[-i]
            }
            for i in range(3)
            if len(self.data) > i
        ]
        
        # Zonen aktualisieren
        self.update_zones(self.data.close[0])
        
        # Neue Zone identifizieren
        new_zone = self.identify_zone(candles)
        if new_zone and new_zone['size'] > self.p.min_zone_size:
            self.zones.append(new_zone)
            
        # Aktive Zone finden
        active_zone = None
        max_strength = 0
        
        for zone in self.zones:
            strength = self.calculate_zone_strength(zone)
            if strength > max_strength:
                max_strength = strength
                active_zone = zone
                
        # Liquidität analysieren
        liquidity = self.analyze_liquidity(
            self.data.close[0],
            self.data.volume[0]
        )
        
        # Linien aktualisieren
        self.lines.zone_signal[0] = (
            1 if (active_zone and
                 active_zone['type'] == ZoneType.DEMAND)
            else -1 if (active_zone and
                       active_zone['type'] == ZoneType.SUPPLY)
            else 0
        )
        self.lines.liquidity_score[0] = liquidity
        self.lines.strength[0] = max_strength
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        current_price = self.data.close[0]
        
        # Aktive Zonen
        active_zones = [
            z for z in self.zones
            if abs(z['level'] - current_price) <
            z['size']
        ]
        
        # Stärkste Zone
        strongest_zone = None
        max_strength = 0
        
        for zone in active_zones:
            strength = self.calculate_zone_strength(zone)
            if strength > max_strength:
                max_strength = strength
                strongest_zone = zone
                
        return {
            'zones': {
                'active_count': len(active_zones),
                'types': {
                    'supply': len([
                        z for z in active_zones
                        if z['type'] == ZoneType.SUPPLY
                    ]),
                    'demand': len([
                        z for z in active_zones
                        if z['type'] == ZoneType.DEMAND
                    ])
                },
                'strongest': {
                    'type': (
                        strongest_zone['type'].value
                        if strongest_zone else None
                    ),
                    'level': (
                        strongest_zone['level']
                        if strongest_zone else None
                    ),
                    'strength': max_strength
                }
            },
            'liquidity_analysis': {
                'score': self.lines.liquidity_score[0],
                'quality': (
                    'high'
                    if self.lines.liquidity_score[0] > 0.8
                    else 'moderate'
                    if self.lines.liquidity_score[0] > 0.5
                    else 'low'
                )
            },
            'market_structure': {
                'bias': (
                    'bullish'
                    if len([
                        z for z in active_zones
                        if z['type'] == ZoneType.DEMAND
                    ]) > len([
                        z for z in active_zones
                        if z['type'] == ZoneType.SUPPLY
                    ])
                    else 'bearish'
                    if len([
                        z for z in active_zones
                        if z['type'] == ZoneType.SUPPLY
                    ]) > len([
                        z for z in active_zones
                        if z['type'] == ZoneType.DEMAND
                    ])
                    else 'neutral'
                ),
                'zone_quality': (
                    ZoneStrength(
                        min(4, int(max_strength))
                    ).name
                    if max_strength > 0
                    else 'NONE'
                )
            },
            'trading_opportunities': {
                'setup_quality': (
                    'excellent'
                    if (max_strength > 3 and
                        self.lines.liquidity_score[0] > 0.8)
                    else 'good'
                    if (max_strength > 2 and
                        self.lines.liquidity_score[0] > 0.6)
                    else 'moderate'
                    if max_strength > 1
                    else 'poor'
                ),
                'key_levels': [
                    {
                        'level': z['level'],
                        'type': z['type'].value,
                        'strength': self.calculate_zone_strength(z)
                    }
                    for z in active_zones
                ]
            }
        }
