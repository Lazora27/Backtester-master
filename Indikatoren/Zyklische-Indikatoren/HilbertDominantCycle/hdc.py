import backtrader as bt
import numpy as np

class HilbertDominantCycle(bt.Indicator):
    """
    Hilbert Transform - Dominant Cycle
    
    Berechnet die dominante Zykluslänge im Preisgeschehen mittels der
    Hilbert-Transformation. Basiert auf John Ehlers' Arbeiten.
    
    Der Indikator:
    - Identifiziert die vorherrschende Zykluslänge
    - Hilft bei der Anpassung anderer Indikatoren
    - Unterstützt Market Timing
    
    Parameter:
    - period (20): Basisperiode für die Berechnung
    - smooth (True): Ob das Signal geglättet werden soll
    """
    
    lines = ('dc', 'smooth_dc', 'phase')
    params = (
        ('period', 20),
        ('smooth', True)
    )
    
    plotlines = dict(
        dc=dict(color='darkblue', _name='Dominant Cycle'),
        smooth_dc=dict(color='red', _name='Smooth DC'),
        phase=dict(_plotskip=True)
    )
    
    def __init__(self):
        self.addminperiod(self.p.period)
        
        # Hilbert Transform Komponenten
        self.smooth_price = self.data0
        if self.p.smooth:
            self.smooth_price = bt.indicators.SMA(self.data0, period=4)
            
        # Phasenakkumulator
        self.phase_acc = 0
        
        # Dominanter Zyklus
        self.dc_period = self.p.period
        
    def next(self):
        # Price Series
        price = self.smooth_price[0]
        
        # Hilbert Transform
        real = 0
        imag = 0
        for i in range(self.p.period):
            angle = (2.0 * np.pi * i) / self.p.period
            real += price * np.cos(angle)
            imag += price * np.sin(angle)
            
        # Dominante Zykluslänge
        if abs(real) > 0:
            self.dc_period = abs(2.0 * np.pi * (imag / real))
            
        self.dc_period = max(min(self.dc_period, 50), 10)
        
        # Phase
        self.phase_acc += (2.0 * np.pi) / self.dc_period
        if self.phase_acc > 2.0 * np.pi:
            self.phase_acc -= 2.0 * np.pi
            
        self.lines.dc[0] = self.dc_period
        self.lines.phase[0] = self.phase_acc
        
        # Geglätteter dominanter Zyklus
        if self.p.smooth:
            self.lines.smooth_dc[0] = bt.indicators.EMA(
                self.lines.dc,
                period=10
            )[0]
        else:
            self.lines.smooth_dc[0] = self.dc_period
            
class DominantCycleOscillator(bt.Indicator):
    """
    Dominant Cycle Oscillator
    
    Ein Oszillator basierend auf dem dominanten Zyklus. Erzeugt Signale
    basierend auf der Zyklusphase.
    
    Parameter:
    - period (20): Basisperiode für die Berechnung
    """
    
    lines = ('osc', 'signal')
    params = (('period', 20),)
    
    plotlines = dict(
        osc=dict(color='darkgreen', _name='DC Osc'),
        signal=dict(color='red', _name='Signal')
    )
    
    def __init__(self):
        # Dominanter Zyklus
        self.dc = HilbertDominantCycle(
            self.data0,
            period=self.p.period
        )
        
        # Oszillator
        self.lines.osc = bt.indicators.SinN(self.dc.phase) * 100
        
        # Signallinie
        self.lines.signal = bt.indicators.CosN(self.dc.phase) * 100
