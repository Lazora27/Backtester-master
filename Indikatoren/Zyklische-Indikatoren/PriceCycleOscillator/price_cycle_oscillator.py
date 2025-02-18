import backtrader as bt
import numpy as np
from scipy import signal

class PriceCycleOscillator(bt.Indicator):
    """
    Price Cycle Oscillator
    
    Ein fortgeschrittener Indikator zur Identifikation und Analyse
    von Preiszyklen mittels spektraler Analyse.
    
    Features:
    - Spektrale Zyklusanalyse
    - Dominante Zyklusidentifikation
    - Oszillatorberechnung
    - Signalgenerierung
    
    Parameter:
    - period (20): Analyseperiode
    - num_cycles (3): Anzahl der zu identifizierenden Zyklen
    - smooth_period (5): Glättungsperiode
    """
    
    lines = ('oscillator', 'dominant_cycle',
             'cycle_strength', 'phase',
             'signal')
             
    params = (
        ('period', 20),
        ('num_cycles', 3),
        ('smooth_period', 5)
    )
    
    plotlines = dict(
        oscillator=dict(color='blue', _name='Oscillator'),
        dominant_cycle=dict(color='red', _name='Dominant Cycle'),
        cycle_strength=dict(color='green', _name='Cycle Strength'),
        phase=dict(color='purple', _name='Phase'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(PriceCycleOscillator, self).__init__()
        
        # Historie
        self.price_history = []
        self.cycle_history = []
        self.oscillator_history = []
        
    def find_dominant_cycles(self):
        """
        Identifiziert dominante Zyklen mittels FFT.
        """
        if len(self.price_history) < self.p.period:
            return 0, 0
            
        # FFT durchführen
        prices = np.array(self.price_history[-self.p.period:])
        fft = np.fft.fft(prices - np.mean(prices))
        freqs = np.fft.fftfreq(len(prices))
        
        # Dominante Frequenzen finden
        magnitudes = np.abs(fft)
        sorted_idx = np.argsort(magnitudes)[::-1]
        
        # Nur positive Frequenzen berücksichtigen
        positive_idx = [
            idx for idx in sorted_idx
            if freqs[idx] > 0
        ][:self.p.num_cycles]
        
        if positive_idx:
            dominant_period = int(
                1 / freqs[positive_idx[0]]
            )
            strength = magnitudes[positive_idx[0]] / sum(
                magnitudes
            )
            return dominant_period, strength
            
        return 0, 0
        
    def calculate_oscillator(self):
        """
        Berechnet den Oszillatorwert.
        """
        if len(self.price_history) < self.p.period:
            return 0
            
        prices = np.array(self.price_history[-self.p.period:])
        detrended = signal.detrend(prices)
        
        if len(detrended) >= self.p.smooth_period:
            return np.mean(
                detrended[-self.p.smooth_period:]
            )
        return detrended[-1]
        
    def calculate_phase(self):
        """
        Berechnet die Zyklusphase.
        """
        if len(self.oscillator_history) < 2:
            return 0
            
        current = self.oscillator_history[-1]
        previous = self.oscillator_history[-2]
        
        if current > previous:
            return 1  # Aufwärtsphase
        elif current < previous:
            return -1  # Abwärtsphase
        return 0  # Neutral
        
    def next(self):
        # Preis speichern
        self.price_history.append(self.data.close[0])
        
        # Dominante Zyklen finden
        dominant_period, cycle_strength = (
            self.find_dominant_cycles()
        )
        self.cycle_history.append(dominant_period)
        
        # Oszillator berechnen
        oscillator = self.calculate_oscillator()
        self.oscillator_history.append(oscillator)
        
        # Phase berechnen
        phase = self.calculate_phase()
        
        # Linien aktualisieren
        self.lines.oscillator[0] = oscillator
        self.lines.dominant_cycle[0] = dominant_period
        self.lines.cycle_strength[0] = cycle_strength
        self.lines.phase[0] = phase
        
        # Signal
        if len(self.oscillator_history) >= 2:
            if (phase > 0 and
                cycle_strength > 0.3):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (phase < 0 and
                  cycle_strength > 0.3):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.smooth_period
        )
        for hist in [self.price_history,
                    self.cycle_history,
                    self.oscillator_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'cycle': {
                'period': self.lines.dominant_cycle[0],
                'strength': self.lines.cycle_strength[0],
                'phase': self.lines.phase[0],
                'oscillator': self.lines.oscillator[0]
            },
            'cycle_state': {
                'trend': (
                    'up' if self.lines.phase[0] > 0
                    else 'down' if self.lines.phase[0] < 0
                    else 'neutral'
                ),
                'strength': (
                    'strong'
                    if self.lines.cycle_strength[0] > 0.5
                    else 'weak'
                ),
                'stability': (
                    'stable'
                    if len(self.cycle_history) >= 2 and
                       abs(self.cycle_history[-1] -
                           self.cycle_history[-2]) < 2
                    else 'unstable'
                )
            },
            'oscillator_analysis': {
                'value': self.lines.oscillator[0],
                'momentum': (
                    'increasing'
                    if self.lines.phase[0] > 0
                    else 'decreasing'
                    if self.lines.phase[0] < 0
                    else 'neutral'
                ),
                'volatility': (
                    'high'
                    if abs(self.lines.oscillator[0]) > 1
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
                    self.lines.cycle_strength[0] *
                    abs(self.lines.phase[0])
                )
            },
            'market_conditions': {
                'cycle_quality': (
                    'optimal'
                    if (self.lines.cycle_strength[0] > 0.4 and
                        abs(self.lines.phase[0]) == 1)
                    else 'suboptimal'
                ),
                'trend_structure': (
                    'clear'
                    if abs(self.lines.oscillator[0]) > 0.5
                    else 'unclear'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.cycle_strength[0] > 0.3 and
                        abs(self.lines.phase[0]) == 1 and
                        abs(self.lines.oscillator[0]) > 0.4)
                    else 'unfavorable'
                )
            }
        }
