import backtrader as bt
import numpy as np

class HilbertPhaseIndicator(bt.Indicator):
    """
    Hilbert Transform - Phase Indicator
    
    Berechnet die momentane Phase des Preiszyklus mittels der
    Hilbert-Transformation.
    
    Der Indikator:
    - Identifiziert die Zyklusphase (0-360°)
    - Zeigt Wendepunkte
    - Unterstützt Market Timing
    
    Parameter:
    - period (20): Basisperiode
    - smooth (True): Ob das Signal geglättet werden soll
    """
    
    lines = ('phase', 'inphase', 'quadrature')
    params = (
        ('period', 20),
        ('smooth', True)
    )
    
    plotlines = dict(
        phase=dict(color='darkblue', _name='Phase'),
        inphase=dict(color='green', _name='InPhase'),
        quadrature=dict(color='red', _name='Quadrature')
    )
    
    def __init__(self):
        self.addminperiod(self.p.period)
        
        # Preisglättung
        self.smooth_price = self.data0
        if self.p.smooth:
            self.smooth_price = bt.indicators.SMA(self.data0, period=4)
            
        # Hilbert Transform Komponenten
        self.real = np.zeros(self.p.period)
        self.imag = np.zeros(self.p.period)
        
    def next(self):
        # Aktualisiere Komponenten
        for i in range(self.p.period - 1, 0, -1):
            self.real[i] = self.real[i-1]
            self.imag[i] = self.imag[i-1]
            
        self.real[0] = self.smooth_price[0]
        
        # Hilbert Transform
        sum_real = 0
        sum_imag = 0
        for i in range(self.p.period):
            angle = (2.0 * np.pi * i) / self.p.period
            sum_real += self.real[i] * np.cos(angle)
            sum_imag += self.real[i] * np.sin(angle)
            
        # In-Phase und Quadratur Komponenten
        self.lines.inphase[0] = sum_real
        self.lines.quadrature[0] = sum_imag
        
        # Phase berechnen
        if abs(sum_real) > 0:
            phase = np.arctan2(sum_imag, sum_real)
            if phase < 0:
                phase += 2.0 * np.pi
                
            self.lines.phase[0] = (phase * 180.0 / np.pi)
        else:
            self.lines.phase[0] = 0
            
class PhaseDivergence(bt.Indicator):
    """
    Phase Divergence
    
    Identifiziert Divergenzen zwischen Preis und Phase.
    
    Parameter:
    - period (20): Basisperiode
    - divergence_threshold (30): Schwellenwert für Divergenzen
    """
    
    lines = ('divergence',)
    params = (
        ('period', 20),
        ('divergence_threshold', 30)
    )
    
    plotlines = dict(
        divergence=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        )
    )
    
    def __init__(self):
        # Phase Indicator
        self.phase = HilbertPhaseIndicator(
            self.data0,
            period=self.p.period
        )
        
        # Preisdifferenz
        price_diff = self.data0 - self.data0(-self.p.period)
        
        # Phasendifferenz
        phase_diff = self.phase.phase - self.phase.phase(-self.p.period)
        
        # Divergenz
        self.lines.divergence = bt.If(
            abs(phase_diff) > self.p.divergence_threshold,
            price_diff * np.sign(phase_diff),
            0
        )
