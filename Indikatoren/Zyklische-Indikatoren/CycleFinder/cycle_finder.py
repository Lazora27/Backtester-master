import backtrader as bt
import numpy as np
from scipy import fft

class CycleFinder(bt.Indicator):
    """
    Cycle Finder Indicator
    
    Ein fortgeschrittener Indikator zur Identifizierung dominanter
    Marktzyklen mittels Fourier-Transformation.
    
    Features:
    - FFT-basierte Zyklusanalyse
    - Dominante Zykluserkennung
    - Trendstärkeberechnung
    - Signalgenerierung
    
    Parameter:
    - period (120): Analysezeitraum
    - min_cycle (10): Minimale Zykluslänge
    - max_cycle (60): Maximale Zykluslänge
    - smooth_period (10): Glättungsperiode
    """
    
    lines = ('dominant_cycle', 'cycle_strength',
             'cycle_phase', 'cycle_quality',
             'signal')
             
    params = (
        ('period', 120),
        ('min_cycle', 10),
        ('max_cycle', 60),
        ('smooth_period', 10)
    )
    
    plotlines = dict(
        dominant_cycle=dict(color='blue', _name='Dominant Cycle'),
        cycle_strength=dict(color='red', _name='Cycle Strength'),
        cycle_phase=dict(color='green', _name='Cycle Phase'),
        cycle_quality=dict(color='purple', _name='Cycle Quality'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(CycleFinder, self).__init__()
        
        # Historie
        self.price_history = []
        self.cycle_history = []
        
    def find_dominant_cycle(self):
        """
        Findet den dominanten Zyklus mittels FFT.
        """
        if len(self.price_history) < self.p.period:
            return 0, 0
            
        # Daten vorbereiten
        prices = np.array(self.price_history[-self.p.period:])
        prices = prices - np.mean(prices)
        
        # FFT durchführen
        fft_result = fft.fft(prices)
        frequencies = fft.fftfreq(len(prices))
        
        # Nur positive Frequenzen betrachten
        positive_freq_idx = np.where(
            (frequencies > 0) &
            (frequencies <= 0.5)
        )[0]
        
        # Amplituden berechnen
        amplitudes = np.abs(fft_result[positive_freq_idx])
        frequencies = frequencies[positive_freq_idx]
        
        # Zykluslängen berechnen
        cycle_lengths = 1 / frequencies
        
        # Relevante Zyklen filtern
        valid_cycles = np.where(
            (cycle_lengths >= self.p.min_cycle) &
            (cycle_lengths <= self.p.max_cycle)
        )[0]
        
        if len(valid_cycles) == 0:
            return 0, 0
            
        # Dominanten Zyklus finden
        max_amplitude_idx = np.argmax(
            amplitudes[valid_cycles]
        )
        dominant_cycle = cycle_lengths[
            valid_cycles[max_amplitude_idx]
        ]
        cycle_strength = amplitudes[
            valid_cycles[max_amplitude_idx]
        ]
        
        return dominant_cycle, cycle_strength
        
    def calculate_cycle_phase(self, cycle_length):
        """
        Berechnet die aktuelle Zyklusphase.
        """
        if cycle_length == 0 or len(self.price_history) < cycle_length:
            return 0
            
        phase = (len(self.price_history) % cycle_length) / cycle_length
        return phase * 2 * np.pi
        
    def calculate_cycle_quality(self, cycle_length):
        """
        Berechnet die Qualität des Zyklus.
        """
        if cycle_length == 0 or len(self.price_history) < 2 * cycle_length:
            return 0
            
        # Vergleiche aktuelle und vorherige Zyklusperiode
        current_cycle = self.price_history[-int(cycle_length):]
        prev_cycle = self.price_history[-2*int(cycle_length):-int(cycle_length)]
        
        if len(current_cycle) != len(prev_cycle):
            return 0
            
        correlation = np.corrcoef(current_cycle, prev_cycle)[0, 1]
        return abs(correlation)
        
    def next(self):
        # Preis speichern
        self.price_history.append(self.data.close[0])
        
        # Dominanten Zyklus finden
        cycle, strength = self.find_dominant_cycle()
        self.cycle_history.append(cycle)
        
        # Linien aktualisieren
        self.lines.dominant_cycle[0] = cycle
        self.lines.cycle_strength[0] = strength
        self.lines.cycle_phase[0] = self.calculate_cycle_phase(cycle)
        self.lines.cycle_quality[0] = self.calculate_cycle_quality(cycle)
        
        # Signal
        if len(self.cycle_history) >= 2:
            if (self.cycle_history[-1] > self.cycle_history[-2] and
                self.lines.cycle_quality[0] > 0.7):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (self.cycle_history[-1] < self.cycle_history[-2] and
                  self.lines.cycle_quality[0] > 0.7):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_history = max(
            self.p.period,
            int(2 * self.p.max_cycle)
        )
        if len(self.price_history) > max_history:
            self.price_history.pop(0)
        if len(self.cycle_history) > max_history:
            self.cycle_history.pop(0)
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'cycle': {
                'length': self.lines.dominant_cycle[0],
                'strength': self.lines.cycle_strength[0],
                'phase': self.lines.cycle_phase[0],
                'quality': self.lines.cycle_quality[0]
            },
            'cycle_state': {
                'position': (
                    'peak'
                    if abs(self.lines.cycle_phase[0] - np.pi) < 0.1
                    else 'trough'
                    if abs(self.lines.cycle_phase[0] - 2*np.pi) < 0.1
                    else 'transition'
                ),
                'strength': (
                    'strong'
                    if self.lines.cycle_strength[0] > 0.7
                    else 'weak'
                ),
                'reliability': (
                    'high'
                    if self.lines.cycle_quality[0] > 0.8
                    else 'medium'
                    if self.lines.cycle_quality[0] > 0.5
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
                'confidence': (
                    self.lines.cycle_quality[0] *
                    self.lines.cycle_strength[0]
                )
            },
            'market_state': {
                'cycle_trend': (
                    'expanding'
                    if len(self.cycle_history) >= 2 and
                       self.cycle_history[-1] >
                       self.cycle_history[-2]
                    else 'contracting'
                ),
                'phase_position': (
                    'bullish'
                    if 0 <= self.lines.cycle_phase[0] <= np.pi
                    else 'bearish'
                ),
                'cycle_stability': (
                    'stable'
                    if self.lines.cycle_quality[0] > 0.7
                    else 'unstable'
                )
            }
        }
