import backtrader as bt
import numpy as np
from datetime import datetime, timedelta

class TimeCycle(bt.Indicator):
    """
    Time Cycle Indicator
    
    Ein fortgeschrittener Indikator zur Analyse von
    zeitbasierten Marktzyklen.
    
    Features:
    - Zeitbasierte Zyklusanalyse
    - Mehrfache Zeitrahmen
    - Zyklusüberlagerung
    - Signalgenerierung
    
    Parameter:
    - time_frames ((60, 240, 1440)): Zeitrahmen in Minuten
    - cycle_threshold (0.6): Zyklusschwelle
    - smooth_period (10): Glättungsperiode
    """
    
    lines = ('cycle', 'composite',
             'strength', 'alignment',
             'signal')
             
    params = (
        ('time_frames', (60, 240, 1440)),  # 1h, 4h, 1d
        ('cycle_threshold', 0.6),
        ('smooth_period', 10)
    )
    
    plotlines = dict(
        cycle=dict(color='blue', _name='Cycle'),
        composite=dict(color='red', _name='Composite'),
        strength=dict(color='green', _name='Strength'),
        alignment=dict(color='purple', _name='Alignment'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(TimeCycle, self).__init__()
        
        # Historie
        self.time_history = []
        self.price_history = []
        self.cycle_history = []
        
        # Zyklen pro Zeitrahmen
        self.cycles = {
            tf: [] for tf in self.p.time_frames
        }
        
    def calculate_cycle_value(self, minutes, prices):
        """
        Berechnet den Zykluswert für einen Zeitrahmen.
        """
        if len(minutes) < 2:
            return 0
            
        # Position im Zyklus
        cycle_position = (
            minutes[-1] % (24 * 60)
        ) / (24 * 60)
        
        # Preisbewegung
        price_change = (
            prices[-1] - prices[0]
        ) / prices[0]
        
        # Zykluswert
        return np.sin(2 * np.pi * cycle_position) * price_change
        
    def calculate_composite(self):
        """
        Berechnet den zusammengesetzten Zykluswert.
        """
        if not self.cycles:
            return 0
            
        # Gewichteter Durchschnitt
        weights = np.array([
            1 / tf for tf in self.p.time_frames
        ])
        weights = weights / np.sum(weights)
        
        composite = 0
        for tf, weight in zip(
            self.p.time_frames,
            weights
        ):
            if self.cycles[tf]:
                composite += (
                    self.cycles[tf][-1] * weight
                )
                
        return composite
        
    def calculate_strength(self):
        """
        Berechnet die Zyklusstärke.
        """
        if len(self.cycle_history) < self.p.smooth_period:
            return 0
            
        cycles = np.array(
            self.cycle_history[-self.p.smooth_period:]
        )
        return np.std(cycles)
        
    def calculate_alignment(self):
        """
        Berechnet die Zyklusausrichtung.
        """
        if not self.cycles:
            return 0
            
        # Richtungsübereinstimmung prüfen
        signs = [
            np.sign(cycle[-1])
            if cycle else 0
            for cycle in self.cycles.values()
        ]
        
        return np.mean(signs)
        
    def next(self):
        # Zeit und Preis speichern
        current_time = self.data.datetime.datetime(0)
        minutes_today = (
            current_time.hour * 60 +
            current_time.minute
        )
        
        self.time_history.append(minutes_today)
        self.price_history.append(self.data.close[0])
        
        # Zyklen für jeden Zeitrahmen berechnen
        for tf in self.p.time_frames:
            if len(self.time_history) >= 2:
                cycle = self.calculate_cycle_value(
                    self.time_history[-tf:],
                    self.price_history[-tf:]
                )
                self.cycles[tf].append(cycle)
            else:
                self.cycles[tf].append(0)
                
        # Composite berechnen
        composite = self.calculate_composite()
        self.cycle_history.append(composite)
        
        # Stärke und Ausrichtung
        strength = self.calculate_strength()
        alignment = self.calculate_alignment()
        
        # Linien aktualisieren
        self.lines.cycle[0] = (
            self.cycles[self.p.time_frames[0]][-1]
            if self.cycles[self.p.time_frames[0]]
            else 0
        )
        self.lines.composite[0] = composite
        self.lines.strength[0] = strength
        self.lines.alignment[0] = alignment
        
        # Signal
        if (strength > self.p.cycle_threshold and
            abs(alignment) > 0.5):
            self.lines.signal[0] = np.sign(alignment)
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            max(self.p.time_frames),
            self.p.smooth_period
        )
        for hist in [self.time_history,
                    self.price_history,
                    self.cycle_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        for cycles in self.cycles.values():
            if len(cycles) > max_period:
                cycles.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'cycles': {
                'primary': self.lines.cycle[0],
                'composite': self.lines.composite[0],
                'strength': self.lines.strength[0],
                'alignment': self.lines.alignment[0]
            },
            'time_analysis': {
                'current_phase': (
                    self.time_history[-1] /
                    (24 * 60)
                    if self.time_history
                    else 0
                ),
                'cycle_position': {
                    str(tf): (
                        self.time_history[-1] % tf /
                        tf
                        if self.time_history
                        else 0
                    )
                    for tf in self.p.time_frames
                }
            },
            'cycle_state': {
                'strength': (
                    'strong'
                    if self.lines.strength[0] >
                       self.p.cycle_threshold
                    else 'weak'
                ),
                'alignment': (
                    'aligned'
                    if abs(self.lines.alignment[0]) > 0.7
                    else 'mixed'
                ),
                'momentum': (
                    'increasing'
                    if self.lines.composite[0] > 0
                    else 'decreasing'
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
                    self.lines.strength[0] *
                    abs(self.lines.alignment[0])
                )
            },
            'market_conditions': {
                'cycle_quality': (
                    'optimal'
                    if (self.lines.strength[0] >
                        self.p.cycle_threshold and
                        abs(self.lines.alignment[0]) > 0.6)
                    else 'suboptimal'
                ),
                'time_structure': (
                    'favorable'
                    if all(
                        len(cycles) >= tf
                        for tf, cycles in self.cycles.items()
                    )
                    else 'developing'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.strength[0] >
                        self.p.cycle_threshold * 0.8 and
                        abs(self.lines.alignment[0]) > 0.5)
                    else 'unfavorable'
                )
            }
        }
