import backtrader as bt
import numpy as np

class SineWaveIndicator(bt.Indicator):
    """
    Sine Wave Indicator
    
    Ein zyklischer Indikator, der Preisbewegungen in Sinuswellen zerlegt.
    Basiert auf der Annahme, dass Märkte in zyklischen Mustern schwingen.
    
    Der Indikator:
    - Generiert Lead und Lag Signale
    - Identifiziert potenzielle Wendepunkte
    - Misst zyklische Überkauft/Überverkauft-Levels
    
    Parameter:
    - period (20): Basisperiode für die Berechnung
    - smooth (True): Ob die Signale geglättet werden sollen
    """
    
    lines = ('sine', 'lead', 'lag')
    params = (
        ('period', 20),
        ('smooth', True)
    )
    
    plotlines = dict(
        sine=dict(color='darkblue', _name='Sine'),
        lead=dict(color='green', _name='Lead'),
        lag=dict(color='red', _name='Lag')
    )
    
    def __init__(self):
        self.addminperiod(self.p.period)
        
        # Preisglättung
        self.price = self.data0
        if self.p.smooth:
            self.price = bt.indicators.SMA(self.data0, period=4)
            
        # Phase
        self.phase = 0
        
        # Dominanter Zyklus
        self.dc = HilbertDominantCycle(
            self.data0,
            period=self.p.period
        )
        
    def next(self):
        # Aktualisiere Phase
        self.phase = self.dc.phase[0]
        
        # Berechne Sinus-Komponenten
        self.lines.sine[0] = np.sin(self.phase) * 100
        self.lines.lead[0] = np.sin(self.phase + np.pi/4) * 100
        self.lines.lag[0] = np.sin(self.phase - np.pi/4) * 100
        
class SineWaveOscillator(bt.Indicator):
    """
    Sine Wave Oscillator
    
    Ein Oszillator basierend auf dem Sine Wave Indicator. Kombiniert
    Lead und Lag Signale für Handelsentscheidungen.
    
    Parameter:
    - period (20): Basisperiode
    - threshold (25): Schwellenwert für Signale
    """
    
    lines = ('osc', 'signal')
    params = (
        ('period', 20),
        ('threshold', 25)
    )
    
    plotlines = dict(
        osc=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        ),
        signal=dict(color='blue', _name='Signal')
    )
    
    def __init__(self):
        # Sine Wave Komponenten
        self.sw = SineWaveIndicator(
            self.data0,
            period=self.p.period
        )
        
        # Oszillator = Lead - Lag
        self.lines.osc = self.sw.lead - self.sw.lag
        
        # Signallinie
        self.lines.signal = bt.indicators.EMA(
            self.lines.osc,
            period=9
        )
        
    def next(self):
        # Überprüfe Schwellenwerte
        if abs(self.lines.osc[0]) > self.p.threshold:
            if self.lines.osc[0] > 0:
                self.buy_signal = True
                self.sell_signal = False
            else:
                self.buy_signal = False
                self.sell_signal = True
        else:
            self.buy_signal = False
            self.sell_signal = False
