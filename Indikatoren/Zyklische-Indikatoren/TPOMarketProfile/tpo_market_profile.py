import backtrader as bt
import numpy as np
from collections import defaultdict

class TPOMarketProfile(bt.Indicator):
    """
    TPO Market Profile Indicator
    
    Ein fortgeschrittener Indikator zur Analyse der Marktstruktur
    mittels Time Price Opportunity (TPO) Profilen.
    
    Features:
    - TPO-Profilberechnung
    - Value Area Analyse
    - Point of Control Identifikation
    - Signalgenerierung
    
    Parameter:
    - tpo_period (30): TPO-Periodenanzahl
    - value_area (0.7): Value Area Prozentsatz
    - price_levels (50): Anzahl der Preisstufen
    """
    
    lines = ('poc', 'vah', 'val',
             'profile_strength', 'distribution',
             'signal')
             
    params = (
        ('tpo_period', 30),
        ('value_area', 0.7),
        ('price_levels', 50)
    )
    
    plotlines = dict(
        poc=dict(color='blue', _name='Point of Control'),
        vah=dict(color='red', _name='Value Area High'),
        val=dict(color='green', _name='Value Area Low'),
        profile_strength=dict(color='purple', _name='Profile Strength'),
        distribution=dict(color='orange', _name='Distribution'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(TPOMarketProfile, self).__init__()
        
        # Historie
        self.price_history = []
        self.volume_history = []
        self.tpo_profiles = []
        
    def calculate_price_levels(self):
        """
        Berechnet die Preisstufen für das TPO-Profil.
        """
        if not self.price_history:
            return []
            
        price_min = min(self.price_history)
        price_max = max(self.price_history)
        price_range = price_max - price_min
        
        if price_range == 0:
            return [price_min]
            
        step = price_range / (self.p.price_levels - 1)
        return np.linspace(
            price_min,
            price_max,
            self.p.price_levels
        )
        
    def build_tpo_profile(self):
        """
        Erstellt das TPO-Profil.
        """
        if len(self.price_history) < self.p.tpo_period:
            return None
            
        price_levels = self.calculate_price_levels()
        if not price_levels.any():
            return None
            
        # TPO-Zählung pro Preisstufe
        tpo_counts = defaultdict(int)
        for i, price in enumerate(
            self.price_history[-self.p.tpo_period:]
        ):
            # Nächste Preisstufe finden
            level_idx = np.abs(
                price_levels - price
            ).argmin()
            tpo_counts[level_idx] += 1
            
        return {
            'levels': price_levels,
            'counts': tpo_counts,
            'total_tpo': sum(tpo_counts.values())
        }
        
    def find_value_area(self, profile):
        """
        Findet Value Area High und Low.
        """
        if not profile:
            return None, None, None
            
        levels = profile['levels']
        counts = profile['counts']
        total_tpo = profile['total_tpo']
        
        # Point of Control
        poc_idx = max(
            counts.keys(),
            key=lambda k: counts[k]
        )
        poc = levels[poc_idx]
        
        # Value Area berechnen
        target_tpo = total_tpo * self.p.value_area
        current_tpo = counts[poc_idx]
        
        vah_idx = poc_idx
        val_idx = poc_idx
        
        while current_tpo < target_tpo:
            # Nächste Levels prüfen
            above_count = (
                counts[vah_idx + 1]
                if vah_idx + 1 < len(levels)
                else 0
            )
            below_count = (
                counts[val_idx - 1]
                if val_idx - 1 >= 0
                else 0
            )
            
            if above_count > below_count:
                vah_idx += 1
                current_tpo += above_count
            else:
                val_idx -= 1
                current_tpo += below_count
                
        return (
            poc,
            levels[vah_idx],
            levels[val_idx]
        )
        
    def calculate_profile_strength(self, profile):
        """
        Berechnet die Stärke des TPO-Profils.
        """
        if not profile:
            return 0
            
        counts = profile['counts']
        total_tpo = profile['total_tpo']
        
        # Konzentration um POC
        poc_idx = max(
            counts.keys(),
            key=lambda k: counts[k]
        )
        
        concentration = counts[poc_idx] / total_tpo
        return concentration
        
    def calculate_distribution(self, profile):
        """
        Berechnet die Verteilung der TPOs.
        """
        if not profile:
            return 0
            
        counts = profile['counts']
        total_tpo = profile['total_tpo']
        
        # Schiefe der Verteilung
        values = np.array([
            counts[k] for k in sorted(counts.keys())
        ])
        if len(values) > 2:
            return stats.skew(values)
        return 0
        
    def next(self):
        # Preis und Volumen speichern
        self.price_history.append(self.data.close[0])
        self.volume_history.append(self.data.volume[0])
        
        # TPO-Profil erstellen
        profile = self.build_tpo_profile()
        if profile:
            self.tpo_profiles.append(profile)
            
            # Value Area analysieren
            poc, vah, val = self.find_value_area(profile)
            
            # Profilstärke und Verteilung
            strength = self.calculate_profile_strength(
                profile
            )
            distribution = self.calculate_distribution(
                profile
            )
            
            # Linien aktualisieren
            self.lines.poc[0] = poc
            self.lines.vah[0] = vah
            self.lines.val[0] = val
            self.lines.profile_strength[0] = strength
            self.lines.distribution[0] = distribution
            
            # Signal
            current_price = self.data.close[0]
            if current_price > vah and strength > 0.3:
                self.lines.signal[0] = 1  # Kaufsignal
            elif current_price < val and strength > 0.3:
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            # Standardwerte
            self.lines.poc[0] = self.data.close[0]
            self.lines.vah[0] = self.data.high[0]
            self.lines.val[0] = self.data.low[0]
            self.lines.profile_strength[0] = 0
            self.lines.distribution[0] = 0
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = self.p.tpo_period
        for hist in [self.price_history,
                    self.volume_history,
                    self.tpo_profiles]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'profile': {
                'poc': self.lines.poc[0],
                'vah': self.lines.vah[0],
                'val': self.lines.val[0],
                'strength': self.lines.profile_strength[0],
                'distribution': self.lines.distribution[0]
            },
            'value_area': {
                'width': (
                    self.lines.vah[0] -
                    self.lines.val[0]
                ) / self.lines.poc[0],
                'position': (
                    'balanced'
                    if abs(
                        self.data.close[0] -
                        self.lines.poc[0]
                    ) < 0.01 * self.lines.poc[0]
                    else 'high'
                    if self.data.close[0] >
                       self.lines.poc[0]
                    else 'low'
                ),
                'strength': (
                    'strong'
                    if self.lines.profile_strength[0] > 0.3
                    else 'weak'
                )
            },
            'distribution_analysis': {
                'skew': self.lines.distribution[0],
                'type': (
                    'normal'
                    if abs(
                        self.lines.distribution[0]
                    ) < 0.5
                    else 'skewed'
                ),
                'balance': (
                    'balanced'
                    if abs(
                        self.lines.distribution[0]
                    ) < 0.3
                    else 'imbalanced'
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
                    (1 - abs(
                        self.lines.distribution[0]
                    ) / 2)
                )
            },
            'market_conditions': {
                'profile_quality': (
                    'optimal'
                    if (self.lines.profile_strength[0] > 0.25 and
                        abs(self.lines.distribution[0]) < 0.4)
                    else 'suboptimal'
                ),
                'value_area_state': (
                    'defined'
                    if (self.lines.vah[0] -
                        self.lines.val[0]
                    ) / self.lines.poc[0] < 0.05
                    else 'wide'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.profile_strength[0] > 0.2 and
                        abs(self.lines.distribution[0]) < 0.5 and
                        (self.lines.vah[0] -
                         self.lines.val[0]
                        ) / self.lines.poc[0] < 0.06)
                    else 'unfavorable'
                )
            }
        }
