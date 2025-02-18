import backtrader as bt
import numpy as np

class EhlersFisherTransform(bt.Indicator):
    """
    Ehlers Fisher Transform
    
    Transformiert Preisdaten in eine Gauß'sche Normalverteilung. Dies macht
    Wendepunkte und extreme Marktbedingungen leichter erkennbar.
    
    Der Indikator:
    - Normalisiert Preisbewegungen
    - Identifiziert Überkauft/Überverkauft-Zustände
    - Reduziert Fehlsignale
    
    Parameter:
    - period (10): Berechnungsperiode
    - poles (3): Anzahl der Pole für IIR-Filter
    """
    
    lines = ('fisher', 'trigger')
    params = (
        ('period', 10),
        ('poles', 3)
    )
    
    plotlines = dict(
        fisher=dict(color='darkblue', _name='Fisher'),
        trigger=dict(color='red', _name='Trigger')
    )
    
    def __init__(self):
        self.addminperiod(self.p.period)
        
        # Median Price
        self.median = (self.data.high + self.data.low) / 2.0
        
        # Initialisierung
        self.value1 = 0
        self.value2 = 0
        
    def next(self):
        # Höchst- und Tiefstwerte über die Periode
        highest = bt.indicators.Highest(
            self.median,
            period=self.p.period
        )[0]
        lowest = bt.indicators.Lowest(
            self.median,
            period=self.p.period
        )[0]
        
        # Normalisierung auf [-1, 1]
        if highest != lowest:
            value1 = 0.33 * 2 * ((self.median[0] - lowest) / 
                                (highest - lowest) - 0.5) + 0.67 * self.value1
        else:
            value1 = 0
            
        self.value1 = value1
        
        # Fisher Transform
        if value1 > 0.99:
            value1 = 0.999
        elif value1 < -0.99:
            value1 = -0.999
            
        self.lines.fisher[0] = 0.5 * np.log((1 + value1) / (1 - value1)) + \
                              0.5 * self.value2
                              
        self.value2 = self.lines.fisher[0]
        
        # Trigger Line (verzögerte Fisher)
        self.lines.trigger[0] = self.lines.fisher[-1]
        
class FisherSignals(bt.Indicator):
    """
    Fisher Transform Signale
    
    Generiert Handelssignale basierend auf der Fisher Transform.
    
    Parameter:
    - threshold (1.0): Schwellenwert für Signale
    """
    
    lines = ('signal',)
    params = (('threshold', 1.0),)
    
    plotlines = dict(
        signal=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        )
    )
    
    def __init__(self):
        # Fisher Transform
        self.fisher = EhlersFisherTransform(self.data0)
        
        # Signale
        self.lines.signal = bt.If(
            self.fisher.fisher > self.p.threshold,
            1,
            bt.If(
                self.fisher.fisher < -self.p.threshold,
                -1,
                0
            )
        )
