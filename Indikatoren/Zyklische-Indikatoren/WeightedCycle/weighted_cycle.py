import backtrader as bt
import numpy as np
from scipy import signal

class WeightedCycle(bt.Indicator):
    """
    Weighted Cycle Indicator
    
    Ein fortgeschrittener Indikator, der gewichtete Zyklen
    analysiert und kombiniert.
    
    Features:
    - Gewichtete Zyklusanalyse
    - Adaptive Gewichtung
    - Zyklusüberlagerung
    - Signalgenerierung
    
    Parameter:
    - cycle_periods ((10, 20, 40)): Zyklusperioden
    - weight_adapt_rate (0.1): Gewichtsanpassungsrate
    - smooth_period (5): Glättungsperiode
    """
    
    lines = ('weighted_cycle', 'dominant_cycle',
             'cycle_strength', 'weight_distribution',
             'signal')
             
    params = (
        ('cycle_periods', (10, 20, 40)),
        ('weight_adapt_rate', 0.1),
        ('smooth_period', 5)
    )
    
    plotlines = dict(
        weighted_cycle=dict(color='blue', _name='Weighted Cycle'),
        dominant_cycle=dict(color='red', _name='Dominant Cycle'),
        cycle_strength=dict(color='green', _name='Cycle Strength'),
        weight_distribution=dict(color='purple', _name='Weight Distribution'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(WeightedCycle, self).__init__()
        
        # Historie
        self.price_history = []
        self.cycle_history = {
            period: [] for period in self.p.cycle_periods
        }
        
        # Gewichte initialisieren
        self.weights = {
            period: 1.0 / len(self.p.cycle_periods)
            for period in self.p.cycle_periods
        }
        
    def extract_cycle(self, data, period):
        """
        Extrahiert einen Zyklus mit gegebener Periode.
        """
        if len(data) < period:
            return 0
            
        # Butterworth-Filter
        nyq = 0.5 * len(data)
        cutoff = period / nyq
        b, a = signal.butter(2, cutoff, btype='low')
        
        # Trend extrahieren und Zyklus isolieren
        trend = signal.filtfilt(b, a, data)
        cycle = data - trend
        
        return cycle[-1]
        
    def update_weights(self):
        """
        Aktualisiert die Zyklusgewichte basierend auf Performance.
        """
        if not all(self.cycle_history.values()):
            return
            
        # Performance der letzten Periode berechnen
        performances = {}
        for period, cycles in self.cycle_history.items():
            if len(cycles) >= 2:
                # Richtungsgenauigkeit bewerten
                accuracy = np.sign(cycles[-1]) == np.sign(
                    self.price_history[-1] -
                    self.price_history[-2]
                )
                performances[period] = (
                    1 if accuracy else -1
                )
            else:
                performances[period] = 0
                
        # Gewichte anpassen
        total_performance = sum(
            abs(p) for p in performances.values()
        )
        if total_performance > 0:
            for period in self.weights:
                self.weights[period] = (
                    (1 - self.p.weight_adapt_rate) *
                    self.weights[period] +
                    self.p.weight_adapt_rate *
                    (performances[period] /
                     total_performance + 1) / 2
                )
                
            # Normalisieren
            total_weight = sum(self.weights.values())
            for period in self.weights:
                self.weights[period] /= total_weight
                
    def calculate_weighted_cycle(self):
        """
        Berechnet den gewichteten Gesamtzyklus.
        """
        if not all(self.cycle_history.values()):
            return 0
            
        weighted_sum = sum(
            self.weights[period] * cycles[-1]
            for period, cycles in self.cycle_history.items()
        )
        
        return weighted_sum
        
    def find_dominant_cycle(self):
        """
        Identifiziert den dominanten Zyklus.
        """
        if not all(self.cycle_history.values()):
            return 0
            
        dominant_period = max(
            self.weights.items(),
            key=lambda x: x[1]
        )[0]
        
        return self.cycle_history[dominant_period][-1]
        
    def calculate_cycle_strength(self):
        """
        Berechnet die Gesamtstärke der Zyklen.
        """
        if not all(self.cycle_history.values()):
            return 0
            
        strengths = [
            abs(cycles[-1])
            for cycles in self.cycle_history.values()
        ]
        
        return np.mean(strengths)
        
    def next(self):
        # Preis speichern
        self.price_history.append(self.data.close[0])
        
        if len(self.price_history) >= min(
            self.p.cycle_periods
        ):
            # Zyklen extrahieren
            prices = np.array(self.price_history)
            for period in self.p.cycle_periods:
                cycle = self.extract_cycle(
                    prices,
                    period
                )
                self.cycle_history[period].append(cycle)
                
            # Gewichte aktualisieren
            self.update_weights()
            
            # Gewichteter Zyklus
            weighted_cycle = self.calculate_weighted_cycle()
            
            # Dominanter Zyklus
            dominant_cycle = self.find_dominant_cycle()
            
            # Zyklusstärke
            cycle_strength = self.calculate_cycle_strength()
            
            # Gewichtsverteilung
            weight_distribution = max(self.weights.values())
            
            # Linien aktualisieren
            self.lines.weighted_cycle[0] = weighted_cycle
            self.lines.dominant_cycle[0] = dominant_cycle
            self.lines.cycle_strength[0] = cycle_strength
            self.lines.weight_distribution[0] = (
                weight_distribution
            )
            
            # Signal
            if cycle_strength > 0.1:
                if weighted_cycle > 0:
                    self.lines.signal[0] = 1  # Kaufsignal
                elif weighted_cycle < 0:
                    self.lines.signal[0] = -1  # Verkaufssignal
                else:
                    self.lines.signal[0] = 0
            else:
                self.lines.signal[0] = 0
        else:
            # Standardwerte
            self.lines.weighted_cycle[0] = 0
            self.lines.dominant_cycle[0] = 0
            self.lines.cycle_strength[0] = 0
            self.lines.weight_distribution[0] = (
                1.0 / len(self.p.cycle_periods)
            )
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            max(self.p.cycle_periods),
            self.p.smooth_period
        )
        if len(self.price_history) > max_period:
            self.price_history.pop(0)
            
        for cycles in self.cycle_history.values():
            if len(cycles) > max_period:
                cycles.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'cycles': {
                'weighted': self.lines.weighted_cycle[0],
                'dominant': self.lines.dominant_cycle[0],
                'strength': self.lines.cycle_strength[0],
                'distribution': self.lines.weight_distribution[0]
            },
            'weights': {
                str(period): weight
                for period, weight in self.weights.items()
            },
            'cycle_state': {
                'dominant_period': max(
                    self.weights.items(),
                    key=lambda x: x[1]
                )[0],
                'strength': (
                    'strong'
                    if self.lines.cycle_strength[0] > 0.15
                    else 'weak'
                ),
                'stability': (
                    'stable'
                    if self.lines.weight_distribution[0] > 0.4
                    else 'unstable'
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
                    self.lines.cycle_strength[0] *
                    self.lines.weight_distribution[0]
                )
            },
            'market_conditions': {
                'cycle_quality': (
                    'optimal'
                    if (self.lines.cycle_strength[0] > 0.12 and
                        self.lines.weight_distribution[0] > 0.35)
                    else 'suboptimal'
                ),
                'weight_structure': (
                    'concentrated'
                    if self.lines.weight_distribution[0] > 0.4
                    else 'distributed'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.cycle_strength[0] > 0.1 and
                        self.lines.weight_distribution[0] > 0.3)
                    else 'unfavorable'
                )
            }
        }
