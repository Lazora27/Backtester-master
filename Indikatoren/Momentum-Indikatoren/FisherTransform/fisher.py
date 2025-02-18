import backtrader as bt
import numpy as np

class FisherTransform(bt.Indicator):
    """
    Fisher Transform Indicator
    
    Wendet die Fisher-Transformation auf die Preisdaten an, um eine normalverteilte
    Zeitreihe zu erzeugen. Dies macht Wendepunkte im Markt deutlicher sichtbar.
    
    Formel:
    1. Value = 0.33 * 2 * ((Price - Lowest Low)/(Highest High - Lowest Low) - 0.5) + 0.67 * Previous Value
    2. Fisher = 0.5 * ln((1 + Value)/(1 - Value))
    
    Parameter:
    - period (10): Periode für die Berechnung der Höchst-/Tiefstkurse
    """
    
    lines = ('fisher', 'signal')
    params = (('period', 10),)
    
    plotlines = dict(
        fisher=dict(color='green', _name='Fisher'),
        signal=dict(color='red', _name='Signal')
    )
    
    def __init__(self):
        # Mittelpunktpreis
        median_price = (self.data.high + self.data.low) / 2.0
        
        # Höchst- und Tiefstkurse
        highest = bt.indicators.Highest(median_price, period=self.p.period)
        lowest = bt.indicators.Lowest(median_price, period=self.p.period)
        
        # Normalisiere Preise auf [-1, 1]
        self.value = bt.indicators.DivByZero(
            median_price - lowest,
            highest - lowest,
            zero=0.5
        ) * 2.0 - 1.0
        
        # Wende Fisher Transform an
        self.lines.fisher = bt.indicators.Fisher(self.value, period=1)
        
        # Signal ist der verzögerte Fisher-Wert
        self.lines.signal = self.lines.fisher(-1)
        
class Fisher(bt.Indicator):
    """Hilfsindiktor für die Fisher-Transformation"""
    
    lines = ('fisher',)
    params = (('period', 1),)
    
    def __init__(self):
        self.addminperiod(self.p.period + 1)
        
    def next(self):
        value = self.data[0]
        # Begrenze value auf [-0.999, 0.999] um numerische Probleme zu vermeiden
        value = max(min(value, 0.999), -0.999)
        
        # Fisher Transform
        self.lines.fisher[0] = 0.5 * np.log((1.0 + value) / (1.0 - value))
