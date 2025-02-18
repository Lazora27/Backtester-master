import backtrader as bt
import numpy as np
from scipy.fft import fft, fftfreq

class FourierTransformAnalysis(bt.Indicator):
    """
    Fourier Transform Analysis
    
    Verwendet die Fast Fourier Transformation (FFT) zur Analyse der
    dominanten Zyklen im Preisgeschehen.
    
    Der Indikator:
    - Identifiziert dominante Frequenzen
    - Filtert Rauschen
    - Projiziert zukünftige Zyklen
    
    Parameter:
    - period (128): Anzahl der Datenpunkte für FFT
    - num_harmonics (3): Anzahl der zu berücksichtigenden Harmonischen
    - projection (20): Länge der Projektion
    """
    
    lines = ('cycle', 'projection', 'strength')
    params = (
        ('period', 128),
        ('num_harmonics', 3),
        ('projection', 20)
    )
    
    plotlines = dict(
        cycle=dict(color='darkblue', _name='Cycle'),
        projection=dict(color='red', _name='Projection'),
        strength=dict(
            _method='bar',
            alpha=0.3,
            width=0.7,
            color='gray'
        )
    )
    
    def __init__(self):
        self.addminperiod(self.p.period)
        
        # Preisdaten-Buffer
        self.price_buffer = np.zeros(self.p.period)
        
        # FFT-Komponenten
        self.frequencies = None
        self.amplitudes = None
        self.phases = None
        
    def next(self):
        # Aktualisiere Buffer
        self.price_buffer = np.roll(self.price_buffer, -1)
        self.price_buffer[-1] = self.data0[0]
        
        if len(self.price_buffer) < self.p.period:
            return
            
        # FFT durchführen
        fft_result = fft(self.price_buffer)
        freqs = fftfreq(self.p.period)
        
        # Positive Frequenzen extrahieren
        pos_mask = freqs > 0
        freqs = freqs[pos_mask]
        fft_result = fft_result[pos_mask]
        
        # Amplituden und Phasen
        amplitudes = np.abs(fft_result)
        phases = np.angle(fft_result)
        
        # Dominante Frequenzen finden
        sorted_indices = np.argsort(amplitudes)[::-1]
        top_indices = sorted_indices[:self.p.num_harmonics]
        
        # Rekonstruktion
        t = np.arange(self.p.period + self.p.projection)
        reconstruction = np.zeros(len(t))
        
        for idx in top_indices:
            freq = freqs[idx]
            amp = amplitudes[idx]
            phase = phases[idx]
            reconstruction += amp * np.cos(2 * np.pi * freq * t + phase)
            
        # Setze Linien
        self.lines.cycle[0] = reconstruction[self.p.period-1]
        self.lines.projection[0] = reconstruction[self.p.period]
        
        # Zyklenstärke (normalisiert)
        strength = amplitudes[top_indices[0]] / np.sum(amplitudes)
        self.lines.strength[0] = strength * 100
        
class FourierCycleFilter(bt.Indicator):
    """
    Fourier Cycle Filter
    
    Filtert Preisdaten basierend auf der FFT-Analyse.
    
    Parameter:
    - period (128): FFT-Periode
    - cutoff (0.1): Frequenz-Cutoff
    """
    
    lines = ('filtered',)
    params = (
        ('period', 128),
        ('cutoff', 0.1)
    )
    
    plotlines = dict(
        filtered=dict(color='darkgreen', _name='Filtered')
    )
    
    def __init__(self):
        self.addminperiod(self.p.period)
        
        # Preisdaten-Buffer
        self.price_buffer = np.zeros(self.p.period)
        
    def next(self):
        # Aktualisiere Buffer
        self.price_buffer = np.roll(self.price_buffer, -1)
        self.price_buffer[-1] = self.data0[0]
        
        if len(self.price_buffer) < self.p.period:
            return
            
        # FFT
        fft_result = fft(self.price_buffer)
        freqs = fftfreq(self.p.period)
        
        # Frequenzfilter
        fft_result[np.abs(freqs) > self.p.cutoff] = 0
        
        # Inverse FFT
        filtered = np.real(np.fft.ifft(fft_result))
        self.lines.filtered[0] = filtered[-1]
