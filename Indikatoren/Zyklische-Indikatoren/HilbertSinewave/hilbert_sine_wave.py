import backtrader as bt
import numpy as np

class HilbertSineWave(bt.Indicator):
    """
    Hilbert Sine Wave Oscillator
    
    Ein fortgeschrittener Zyklusindikator, der die Hilbert-Transformation
    verwendet, um dominante Zyklen zu identifizieren und zu analysieren.
    
    Features:
    - Hilbert-Transformation
    - Dominante Zyklusberechnung
    - Phasenanalyse
    - Signalgenerierung
    
    Parameter:
    - period (20): Analysezeitraum
    - smooth_period (10): Glättungsperiode
    - phase_shift (0): Phasenverschiebung
    """
    
    lines = ('sine_wave', 'lead_sine',
             'dominant_cycle', 'phase_angle',
             'signal')
             
    params = (
        ('period', 20),
        ('smooth_period', 10),
        ('phase_shift', 0)
    )
    
    plotlines = dict(
        sine_wave=dict(color='blue', _name='Sine Wave'),
        lead_sine=dict(color='red', _name='Lead Sine'),
        dominant_cycle=dict(color='green', _name='Dominant Cycle'),
        phase_angle=dict(color='purple', _name='Phase Angle'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(HilbertSineWave, self).__init__()
        
        # Historie
        self.price_history = []
        self.hilbert_history = []
        self.phase_history = []
        
        # Hilbert-Transformationskoeffizienten
        self.a = [0.0962, 0.5769, -0.5769, -0.0962]
        self.b = [0.0962, 0.5769, 0.5769, 0.0962]
        
    def hilbert_transform(self, data):
        """
        Führt die Hilbert-Transformation durch.
        """
        if len(data) < 4:
            return 0
            
        real = sum(
            self.a[i] * data[-i-1]
            for i in range(4)
        )
        imag = sum(
            self.b[i] * data[-i-1]
            for i in range(4)
        )
        
        return real, imag
        
    def calculate_dominant_cycle(self):
        """
        Berechnet den dominanten Zyklus.
        """
        if len(self.hilbert_history) < 2:
            return self.p.period
            
        # Differenz der Hilbert-Phasen
        phase_diff = (
            self.hilbert_history[-1][1] -
            self.hilbert_history[-2][1]
        )
        
        if phase_diff != 0:
            cycle = 2 * np.pi / abs(phase_diff)
            return min(max(cycle, 8), self.p.period)
            
        return self.p.period
        
    def calculate_phase_angle(self):
        """
        Berechnet den Phasenwinkel.
        """
        if len(self.hilbert_history) < 1:
            return 0
            
        real, imag = self.hilbert_history[-1]
        
        if real != 0:
            angle = np.arctan2(imag, real)
            return (angle + np.pi) % (2 * np.pi)
            
        return 0
        
    def next(self):
        # Preis speichern
        self.price_history.append(self.data.close[0])
        
        # Hilbert-Transformation
        if len(self.price_history) >= 4:
            hilbert = self.hilbert_transform(self.price_history)
            self.hilbert_history.append(hilbert)
            
            # Phasenwinkel
            phase = self.calculate_phase_angle()
            self.phase_history.append(phase)
            
            # Dominanter Zyklus
            dominant_cycle = self.calculate_dominant_cycle()
            
            # Sine Wave und Lead Sine berechnen
            sine_wave = np.sin(phase + self.p.phase_shift)
            lead_sine = np.sin(
                phase + self.p.phase_shift + np.pi/4
            )
            
            # Linien aktualisieren
            self.lines.sine_wave[0] = sine_wave
            self.lines.lead_sine[0] = lead_sine
            self.lines.dominant_cycle[0] = dominant_cycle
            self.lines.phase_angle[0] = phase
            
            # Signal
            if len(self.phase_history) >= 2:
                if (sine_wave > 0 and
                    self.phase_history[-2] < np.pi/2):
                    self.lines.signal[0] = 1  # Kaufsignal
                elif (sine_wave < 0 and
                      self.phase_history[-2] > 3*np.pi/2):
                    self.lines.signal[0] = -1  # Verkaufssignal
                else:
                    self.lines.signal[0] = 0
            else:
                self.lines.signal[0] = 0
        else:
            # Standardwerte
            self.lines.sine_wave[0] = 0
            self.lines.lead_sine[0] = 0
            self.lines.dominant_cycle[0] = self.p.period
            self.lines.phase_angle[0] = 0
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.smooth_period
        )
        for hist in [self.price_history,
                    self.hilbert_history,
                    self.phase_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'wave': {
                'sine': self.lines.sine_wave[0],
                'lead': self.lines.lead_sine[0],
                'phase': self.lines.phase_angle[0],
                'cycle': self.lines.dominant_cycle[0]
            },
            'cycle_state': {
                'position': (
                    'peak'
                    if abs(self.lines.sine_wave[0] - 1) < 0.1
                    else 'trough'
                    if abs(self.lines.sine_wave[0] + 1) < 0.1
                    else 'transition'
                ),
                'momentum': (
                    'increasing'
                    if self.lines.lead_sine[0] > 0
                    else 'decreasing'
                ),
                'phase_quality': (
                    'optimal'
                    if len(self.phase_history) >= 2 and
                       abs(
                           self.phase_history[-1] -
                           self.phase_history[-2]
                       ) < np.pi/4
                    else 'suboptimal'
                )
            },
            'market_structure': {
                'cycle_length': (
                    'stable'
                    if self.lines.dominant_cycle[0] > 10
                    else 'unstable'
                ),
                'wave_quality': (
                    'clean'
                    if abs(self.lines.sine_wave[0]) > 0.7
                    else 'noisy'
                ),
                'trend_alignment': (
                    'aligned'
                    if (self.lines.sine_wave[0] > 0 and
                        self.lines.lead_sine[0] > 0) or
                       (self.lines.sine_wave[0] < 0 and
                        self.lines.lead_sine[0] < 0)
                    else 'divergent'
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
                    abs(self.lines.sine_wave[0]) *
                    (1 - abs(
                        self.lines.sine_wave[0] -
                        self.lines.lead_sine[0]
                    ) / 2)
                )
            },
            'trading_conditions': {
                'cycle_phase': (
                    'optimal'
                    if abs(self.lines.sine_wave[0]) > 0.8
                    else 'suboptimal'
                ),
                'momentum_quality': (
                    'strong'
                    if abs(self.lines.lead_sine[0]) > 0.7
                    else 'weak'
                ),
                'trade_timing': (
                    'favorable'
                    if (abs(self.lines.sine_wave[0]) > 0.7 and
                        abs(self.lines.lead_sine[0]) > 0.7)
                    else 'unfavorable'
                )
            }
        }
