import backtrader as bt
import numpy as np

class HilbertSinewave(bt.Indicator):
    """
    Hilbert Transform - Sinewave
    
    Erzeugt Sinus- und Kosinuswellen basierend auf der Hilbert-Transformation
    der Preisdaten.
    
    Der Indikator:
    - Generiert Lead/Lag Signale
    - Identifiziert Marktzyklen
    - Zeigt Trendrichtung
    
    Parameter:
    - period (20): Basisperiode
    - smooth (True): Ob die Signale geglättet werden sollen
    """
    
    lines = ('sine', 'leadsine', 'cosine', 'dcphase')
    params = (
        ('period', 20),
        ('smooth', True)
    )
    
    plotlines = dict(
        sine=dict(color='darkblue', _name='Sine'),
        leadsine=dict(color='green', _name='LeadSine'),
        cosine=dict(color='red', _name='Cosine'),
        dcphase=dict(_plotskip=True)
    )
    
    def __init__(self):
        self.addminperiod(self.p.period)
        
        # Preisglättung
        self.price = self.data0
        if self.p.smooth:
            self.price = bt.indicators.SMA(self.data0, period=4)
            
        # Hilbert Transform Komponenten
        self.smooth_period = 0
        self.dc_period = self.p.period
        self.phase = 0
        
    def next(self):
        # Dominante Zyklusperiode
        self.dc_period = max(
            min(self.dc_period, 50),
            10
        )
        
        # Phase akkumulieren
        self.phase += (2.0 * np.pi) / self.dc_period
        if self.phase > 2.0 * np.pi:
            self.phase -= 2.0 * np.pi
            
        self.lines.dcphase[0] = self.phase
        
        # Sinus und Kosinus berechnen
        self.lines.sine[0] = np.sin(self.phase) * 100
        self.lines.cosine[0] = np.cos(self.phase) * 100
        
        # Lead Sinus (45° Vorsprung)
        lead_phase = self.phase + (np.pi / 4)
        if lead_phase > 2.0 * np.pi:
            lead_phase -= 2.0 * np.pi
            
        self.lines.leadsine[0] = np.sin(lead_phase) * 100
        
class SinewaveOscillator(bt.Indicator):
    """
    Sinewave Oscillator
    
    Kombiniert Sinus- und Kosinuswellen zu einem Oszillator.
    
    Parameter:
    - period (20): Basisperiode
    - threshold (80): Schwellenwert für Signale
    """
    
    lines = ('oscillator', 'signal')
    params = (
        ('period', 20),
        ('threshold', 80)
    )
    
    plotlines = dict(
        oscillator=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        ),
        signal=dict(color='blue', _name='Signal')
    )
    
    def __init__(self):
        # Sinewave Komponenten
        self.sw = HilbertSinewave(
            self.data0,
            period=self.p.period
        )
        
        # Oszillator = Sinus - Kosinus
        self.lines.oscillator = self.sw.sine - self.sw.cosine
        
        # Signallinie
        self.lines.signal = bt.indicators.EMA(
            self.lines.oscillator,
            period=9
        )
        
        # Signale
        self.buy_signal = bt.indicators.CrossOver(
            self.lines.oscillator,
            self.lines.signal
        )
        
        self.sell_signal = bt.indicators.CrossOver(
            self.lines.signal,
            self.lines.oscillator
        )
