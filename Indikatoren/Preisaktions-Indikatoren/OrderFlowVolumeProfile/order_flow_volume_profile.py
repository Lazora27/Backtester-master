import backtrader as bt
import numpy as np
from collections import defaultdict

class OrderFlowVolumeProfile(bt.Indicator):
    """
    Order Flow Volume Profile Indicator
    
    Ein fortgeschrittener Indikator zur Analyse des
    Volumen-Profils und Order Flows.
    
    Features:
    - Volumen-Profil-Analyse
    - POC (Point of Control) Identifikation
    - Value Area Berechnung
    - Signalgenerierung
    
    Parameter:
    - profile_period (50): Profilperiode
    - value_area_pct (0.7): Value Area Prozentsatz
    - poc_threshold (0.1): POC Schwelle
    """
    
    lines = ('poc_level', 'value_area_high',
             'value_area_low', 'profile_balance',
             'signal')
             
    params = (
        ('profile_period', 50),
        ('value_area_pct', 0.7),
        ('poc_threshold', 0.1)
    )
    
    plotlines = dict(
        poc_level=dict(color='blue', _name='POC Level'),
        value_area_high=dict(color='red', _name='Value Area High'),
        value_area_low=dict(color='green', _name='Value Area Low'),
        profile_balance=dict(color='purple', _name='Profile Balance'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(OrderFlowVolumeProfile, self).__init__()
        
        # Profil-Tracking
        self.price_levels = defaultdict(float)
        self.volume_profile = defaultdict(list)
        self.poc_history = []
        self.price_history = []
        
    def update_profile(self, price, volume):
        """
        Aktualisiert das Volumen-Profil.
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
        
    def find_poc(self):
        """
        Findet den Point of Control (POC).
        """
        if not self.price_levels:
            return 0
            
        # Level mit höchstem Volumen
        poc_level = max(
            self.price_levels.items(),
            key=lambda x: x[1]
        )[0]
        
        self.poc_history.append(poc_level)
        return poc_level
        
    def calculate_value_area(self):
        """
        Berechnet die Value Area.
        """
        if not self.price_levels:
            return 0, 0
            
        total_volume = sum(self.price_levels.values())
        target_volume = total_volume * self.p.value_area_pct
        
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
                
        return min(included_levels), max(included_levels)
        
    def calculate_profile_balance(self):
        """
        Berechnet die Balance des Profils.
        """
        if not self.price_levels:
            return 0
            
        poc_level = self.poc_history[-1]
        
        # Volumen über/unter POC
        volume_above = sum(
            vol for level, vol in self.price_levels.items()
            if level > poc_level
        )
        volume_below = sum(
            vol for level, vol in self.price_levels.items()
            if level < poc_level
        )
        
        total_volume = volume_above + volume_below
        if total_volume == 0:
            return 0
            
        return (volume_above - volume_below) / total_volume
        
    def next(self):
        # Preis und Volumen speichern
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        self.price_history.append(price)
        
        # Profil aktualisieren
        self.update_profile(price, volume)
        
        # POC und Value Area berechnen
        poc_level = self.find_poc()
        value_area_low, value_area_high = (
            self.calculate_value_area()
        )
        
        # Profilbalance
        profile_balance = self.calculate_profile_balance()
        
        # Linien aktualisieren
        self.lines.poc_level[0] = poc_level
        self.lines.value_area_low[0] = value_area_low
        self.lines.value_area_high[0] = value_area_high
        self.lines.profile_balance[0] = profile_balance
        
        # Signal
        current_price = self.price_history[-1]
        if abs(profile_balance) > self.p.poc_threshold:
            if (current_price < value_area_low and
                profile_balance > 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (current_price > value_area_high and
                  profile_balance < 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        if len(self.price_history) > self.p.profile_period:
            old_price = self.price_history.pop(0)
            old_level = self.get_price_level(old_price)
            
            # Altes Volumen entfernen
            if old_level in self.volume_profile:
                if self.volume_profile[old_level]:
                    old_volume = self.volume_profile[old_level].pop(0)
                    self.price_levels[old_level] -= old_volume
                    
                    if self.price_levels[old_level] <= 0:
                        del self.price_levels[old_level]
                        del self.volume_profile[old_level]
                        
        if len(self.poc_history) > self.p.profile_period:
            self.poc_history.pop(0)
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'profile': {
                'poc': self.lines.poc_level[0],
                'value_area': {
                    'low': self.lines.value_area_low[0],
                    'high': self.lines.value_area_high[0]
                },
                'balance': self.lines.profile_balance[0]
            },
            'volume_distribution': {
                'levels': len(self.price_levels),
                'concentration': (
                    'high'
                    if len(self.price_levels) < 10
                    else 'moderate'
                    if len(self.price_levels) < 20
                    else 'low'
                ),
                'distribution': {
                    str(level): volume
                    for level, volume
                    in self.price_levels.items()
                }
            },
            'profile_analysis': {
                'structure': (
                    'balanced'
                    if abs(self.lines.profile_balance[0]) <
                       self.p.poc_threshold
                    else 'imbalanced'
                ),
                'poc_stability': (
                    'stable'
                    if len(set(self.poc_history[-5:])) == 1
                    else 'volatile'
                ),
                'value_area_width': (
                    self.lines.value_area_high[0] -
                    self.lines.value_area_low[0]
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
                    abs(self.lines.profile_balance[0]) *
                    (1 if len(set(self.poc_history[-5:])) == 1
                     else 0.5)
                )
            },
            'market_conditions': {
                'profile_quality': (
                    'high'
                    if len(self.price_levels) > 15
                    else 'low'
                ),
                'value_area_quality': (
                    'defined'
                    if (self.lines.value_area_high[0] -
                        self.lines.value_area_low[0]) > 0
                    else 'undefined'
                ),
                'trading_environment': (
                    'favorable'
                    if (len(self.price_levels) > 10 and
                        abs(self.lines.profile_balance[0]) >
                        self.p.poc_threshold * 0.8)
                    else 'unfavorable'
                )
            }
        }
