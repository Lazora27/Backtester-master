import backtrader as bt
import numpy as np

class RelativeVigorIndex(bt.Indicator):
    """
    Relative Vigor Index (RVI)
    
    Vergleicht die Position des Schlusskurses relativ zum Tageshoch/-tief mit der
    Preisbewegung. Die Idee ist, dass in Aufwärtstrends die Schlusskurse eher nahe
    am Tageshoch und in Abwärtstrends eher nahe am Tagestief liegen.
    
    Formel:
    RVI = (Close - Open) / (High - Low)
    Signal = 4-Perioden gleitender Durchschnitt des RVI
    
    Parameter:
    - period (10): Periode für die Berechnung
    """
    
    lines = ('rvi', 'signal')
    params = (('period', 10),)
    
    plotlines = dict(
        rvi=dict(color='green', _name='RVI'),
        signal=dict(color='red', _name='Signal')
    )
    
    def __init__(self):
        # Berechne Zähler (Schlusskurs - Eröffnungskurs)
        numerator = self.data.close - self.data.open
        
        # Berechne Nenner (Hoch - Tief)
        denominator = self.data.high - self.data.low
        
        # Verhindere Division durch Null
        self.rvi_raw = bt.If(denominator != 0, numerator / denominator, 0)
        
        # Berechne gleitende Durchschnitte für RVI und Signal
        self.lines.rvi = bt.indicators.SMA(self.rvi_raw, period=self.p.period)
        
        # Signal ist ein 4-Perioden gleitender Durchschnitt des RVI
        self.lines.signal = bt.indicators.SMA(self.lines.rvi, period=4)
