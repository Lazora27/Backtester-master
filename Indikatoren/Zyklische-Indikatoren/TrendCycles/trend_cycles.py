import backtrader as bt
import numpy as np
from scipy import signal

class TrendCycles(bt.Indicator):
    """
    Trend Cycles Indicator
    
    Ein fortgeschrittener Indikator zur Analyse von
    Trendzyklen und deren Interaktion.
    
    Features:
    - Trendzyklusextraktion
    - Multi-Trend-Analyse
    - Zyklusüberlagerung
    - Signalgenerierung
    
    Parameter:
    - cycle_periods ((20, 40, 80)): Zyklusperioden
    - trend_threshold (0.02): Trendschwelle
    - smooth_period (10): Glättungsperiode
    """
    
    lines = ('primary_cycle', 'secondary_cycle',
             'trend_strength', 'cycle_alignment',
             'signal')
             
    params = (
        ('cycle_periods', (20, 40, 80)),
        ('trend_threshold', 0.02),
        ('smooth_period', 10)
    )
    
    plotlines = dict(
        primary_cycle=dict(color='blue', _name='Primary Cycle'),
        secondary_cycle=dict(color='red', _name='Secondary Cycle'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        cycle_alignment=dict(color='purple', _name='Cycle Alignment'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(TrendCycles, self).__init__()
        
        # Historie
        self.price_history = []
        self.cycle_history = {
            period: []
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
        
        # Trend extrahieren
        trend = signal.filtfilt(b, a, data)
        cycle = data - trend
        
        return cycle[-1]
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.price_history) < self.p.smooth_period:
            return 0
            
        prices = np.array(
            self.price_history[-self.p.smooth_period:]
        )
        trend = np.polyfit(
            range(len(prices)),
            prices,
            1
        )[0]
        
        return abs(trend) / np.mean(prices)
        
    def calculate_alignment(self):
        """
        Berechnet die Zyklusausrichtung.
        """
        if not all(self.cycle_history.values()):
            return 0
            
        # Richtungsübereinstimmung prüfen
        signs = [
            np.sign(cycles[-1])
            if cycles else 0
            for cycles in self.cycle_history.values()
        ]
        
        return np.mean(signs)
        
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
                
            # Primär- und Sekundärzyklen
            primary = self.cycle_history[
                self.p.cycle_periods[0]
            ][-1]
            secondary = self.cycle_history[
                self.p.cycle_periods[1]
            ][-1]
            
            # Trendstärke und Ausrichtung
            trend_strength = self.calculate_trend_strength()
            alignment = self.calculate_alignment()
            
            # Linien aktualisieren
            self.lines.primary_cycle[0] = primary
            self.lines.secondary_cycle[0] = secondary
            self.lines.trend_strength[0] = trend_strength
            self.lines.cycle_alignment[0] = alignment
            
            # Signal
            if trend_strength > self.p.trend_threshold:
                if alignment > 0.5:
                    self.lines.signal[0] = 1  # Kaufsignal
                elif alignment < -0.5:
                    self.lines.signal[0] = -1  # Verkaufssignal
                else:
                    self.lines.signal[0] = 0
            else:
                self.lines.signal[0] = 0
        else:
            # Standardwerte
            self.lines.primary_cycle[0] = 0
            self.lines.secondary_cycle[0] = 0
            self.lines.trend_strength[0] = 0
            self.lines.cycle_alignment[0] = 0
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
                'primary': self.lines.primary_cycle[0],
                'secondary': self.lines.secondary_cycle[0],
                'strength': self.lines.trend_strength[0],
                'alignment': self.lines.cycle_alignment[0]
            },
            'trend_state': {
                'strength': (
                    'strong'
                    if self.lines.trend_strength[0] >
                       self.p.trend_threshold
                    else 'weak'
                ),
                'direction': (
                    'up'
                    if self.lines.cycle_alignment[0] > 0
                    else 'down'
                    if self.lines.cycle_alignment[0] < 0
                    else 'neutral'
                ),
                'quality': (
                    'high'
                    if abs(
                        self.lines.cycle_alignment[0]
                    ) > 0.7
                    else 'low'
                )
            },
            'cycle_analysis': {
                'harmony': (
                    'aligned'
                    if abs(
                        self.lines.cycle_alignment[0]
                    ) > 0.5
                    else 'divergent'
                ),
                'dominance': (
                    'primary'
                    if abs(
                        self.lines.primary_cycle[0]
                    ) > abs(
                        self.lines.secondary_cycle[0]
                    )
                    else 'secondary'
                ),
                'interaction': (
                    'constructive'
                    if (np.sign(
                        self.lines.primary_cycle[0]
                    ) == np.sign(
                        self.lines.secondary_cycle[0]
                    ))
                    else 'destructive'
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
                    self.lines.trend_strength[0] *
                    abs(self.lines.cycle_alignment[0])
                )
            },
            'market_conditions': {
                'trend_quality': (
                    'optimal'
                    if (self.lines.trend_strength[0] >
                        self.p.trend_threshold and
                        abs(self.lines.cycle_alignment[0]) > 0.6)
                    else 'suboptimal'
                ),
                'cycle_structure': (
                    'clear'
                    if all(
                        len(cycles) >= period
                        for period, cycles in
                        self.cycle_history.items()
                    )
                    else 'developing'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.trend_strength[0] >
                        self.p.trend_threshold * 0.8 and
                        abs(self.lines.cycle_alignment[0]) > 0.5)
                    else 'unfavorable'
                )
            }
        }
