import backtrader as bt
import numpy as np
from collections import defaultdict

class VolumeProfile(bt.Indicator):
    """
    Volume Profile Indicator
    
    Ein fortgeschrittener Indikator zur Analyse des
    Volumensprofils und der Preisverteilung.
    
    Features:
    - Volumenprofilanalyse
    - Preisverteilung
    - Profilmuster
    - Signalgenerierung
    
    Parameter:
    - profile_period (50): Profilperiode
    - price_levels (20): Preisebenen
    - volume_threshold (0.7): Volumenschwelle
    """
    
    lines = ('profile_poc', 'profile_vwap',
             'profile_balance', 'profile_strength',
             'signal')
             
    params = (
        ('profile_period', 50),
        ('price_levels', 20),
        ('volume_threshold', 0.7)
    )
    
    plotlines = dict(
        profile_poc=dict(color='blue', _name='Profile POC'),
        profile_vwap=dict(color='red', _name='Profile VWAP'),
        profile_balance=dict(color='green', _name='Profile Balance'),
        profile_strength=dict(color='purple', _name='Profile Strength'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(VolumeProfile, self).__init__()
        
        # Profil Tracking
        self.price_levels = defaultdict(float)
        self.volume_profile = defaultdict(list)
        self.poc_history = []
        self.vwap_history = []
        
    def update_profile(self, price, volume):
        """
        Aktualisiert das Volumprofil.
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
        
    def find_profile_poc(self):
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
        
    def calculate_profile_vwap(self):
        """
        Berechnet den volumengewichteten Durchschnittspreis.
        """
        if not self.price_levels:
            return 0
            
        total_volume = sum(self.price_levels.values())
        if total_volume == 0:
            return 0
            
        vwap = sum(
            price * volume
            for price, volume in self.price_levels.items()
        ) / total_volume
        
        self.vwap_history.append(vwap)
        return vwap
        
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
        
    def calculate_profile_strength(self):
        """
        Berechnet die Stärke des Profils.
        """
        if not self.price_levels:
            return 0
            
        # Stärke basierend auf Volumenverteilung
        total_volume = sum(self.price_levels.values())
        if total_volume == 0:
            return 0
            
        max_volume = max(self.price_levels.values())
        return max_volume / total_volume
        
    def next(self):
        # Preis und Volumen speichern
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        # Profil aktualisieren
        self.update_profile(price, volume)
        
        # Profil-Metriken berechnen
        profile_poc = self.find_profile_poc()
        profile_vwap = self.calculate_profile_vwap()
        profile_balance = self.calculate_profile_balance()
        profile_strength = self.calculate_profile_strength()
        
        # Linien aktualisieren
        self.lines.profile_poc[0] = profile_poc
        self.lines.profile_vwap[0] = profile_vwap
        self.lines.profile_balance[0] = profile_balance
        self.lines.profile_strength[0] = profile_strength
        
        # Signal
        if profile_strength > self.p.volume_threshold:
            if (price < profile_poc and
                profile_balance > 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (price > profile_poc and
                  profile_balance < 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        if len(self.poc_history) > self.p.profile_period:
            self.poc_history.pop(0)
            
        if len(self.vwap_history) > self.p.profile_period:
            self.vwap_history.pop(0)
            
        # Alte Levels entfernen
        current_time = len(self.data)
        for level in list(self.volume_profile.keys()):
            while (len(self.volume_profile[level]) >
                   self.p.profile_period):
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
            'profile_metrics': {
                'poc': self.lines.profile_poc[0],
                'vwap': self.lines.profile_vwap[0],
                'balance': self.lines.profile_balance[0],
                'strength': self.lines.profile_strength[0]
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
                    if abs(self.lines.profile_balance[0]) < 0.2
                    else 'top_heavy'
                    if self.lines.profile_balance[0] > 0
                    else 'bottom_heavy'
                ),
                'poc_stability': (
                    'stable'
                    if len(set(self.poc_history[-5:])) == 1
                    else 'volatile'
                ),
                'vwap_trend': (
                    'up'
                    if len(self.vwap_history) > 1 and
                    self.vwap_history[-1] > self.vwap_history[-2]
                    else 'down'
                )
            },
            'level_analysis': {
                'active_levels': len(self.price_levels),
                'dominant_levels': sum(
                    1 for v in self.price_levels.values()
                    if v > sum(self.price_levels.values()) *
                       self.p.volume_threshold
                ),
                'level_distribution': (
                    'even'
                    if len(self.price_levels) > self.p.price_levels
                    else 'concentrated'
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
                    self.lines.profile_strength[0] *
                    (1 if len(set(self.poc_history[-5:])) == 1
                     else 0.5)
                )
            },
            'market_conditions': {
                'profile_quality': (
                    'high'
                    if self.lines.profile_strength[0] >
                       self.p.volume_threshold
                    else 'low'
                ),
                'balance_state': (
                    'balanced'
                    if abs(self.lines.profile_balance[0]) < 0.2
                    else 'imbalanced'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.profile_strength[0] >
                        self.p.volume_threshold and
                        abs(self.lines.profile_balance[0]) > 0.2)
                    else 'unfavorable'
                )
            }
        }
