import backtrader as bt
import numpy as np

class MurreyMathLines(bt.Indicator):
    """
    Murrey Math Lines (MML)
    
    Berechnet die 8 Murrey Math Lines basierend auf dem Oktaven-Konzept.
    Jede Oktave wird in 8 gleiche Teile geteilt, die wichtige
    Unterstützungs- und Widerstandsniveaus darstellen.
    
    Lines:
    - 8/8 (Ultimate Resistance)
    - 7/8 (Weak, Stall and Reverse)
    - 6/8 (Resistance)
    - 5/8 (Top of Trading Range)
    - 4/8 (Major Support/Resistance)
    - 3/8 (Bottom of Trading Range)
    - 2/8 (Support)
    - 1/8 (Weak, Stall and Reverse)
    - 0/8 (Ultimate Support)
    
    Parameter:
    - period (64): Berechnungsperiode
    - shift (1): Verschiebung für Oktavenberechnung
    """
    
    lines = ('line_0_8', 'line_1_8', 'line_2_8', 'line_3_8',
             'line_4_8', 'line_5_8', 'line_6_8', 'line_7_8', 'line_8_8')
             
    params = (
        ('period', 64),
        ('shift', 1)
    )
    
    plotlines = dict(
        line_0_8=dict(color='red', _name='0/8'),
        line_1_8=dict(color='orange', _name='1/8'),
        line_2_8=dict(color='yellow', _name='2/8'),
        line_3_8=dict(color='green', _name='3/8'),
        line_4_8=dict(color='blue', _name='4/8'),
        line_5_8=dict(color='purple', _name='5/8'),
        line_6_8=dict(color='brown', _name='6/8'),
        line_7_8=dict(color='gray', _name='7/8'),
        line_8_8=dict(color='black', _name='8/8')
    )
    
    def __init__(self):
        super(MurreyMathLines, self).__init__()
        
        # Höchst- und Tiefstkurse
        self.high = bt.indicators.Highest(self.data.high, period=self.p.period)
        self.low = bt.indicators.Lowest(self.data.low, period=self.p.period)
        
    def find_octave(self, price_range):
        """Findet die passende Oktave für den Preisbereich."""
        octaves = [10000000, 5000000, 2500000, 1250000, 625000,
                  312500, 156250, 78125, 39062.5, 19531.25,
                  9765.625, 4882.8125, 2441.40625, 1220.703125,
                  610.3515625, 305.17578125, 152.587890625,
                  76.2939453125, 38.14697265625, 19.073486328125,
                  9.5367431640625, 4.76837158203125,
                  2.384185791015625, 1.1920928955078125,
                  0.59604644775390625, 0.29802322387695312]
                  
        for octave in octaves:
            if price_range <= octave:
                continue
            return octave
            
        return octaves[-1]
        
    def next(self):
        # Preisbereich
        price_range = self.high[0] - self.low[0]
        
        # Oktave finden
        octave = self.find_octave(price_range)
        
        # Basispreis berechnen
        base = int(self.low[0] / octave) * octave
        if self.low[0] < 0:
            base -= octave
            
        # Murrey Math Lines berechnen
        for i in range(9):
            level = base + (octave * i / 8.0)
            setattr(self.lines[f'line_{i}_8'], 0, level)
            
class MurreyMathSignals(bt.Indicator):
    """
    Murrey Math Signale
    
    Generiert Handelssignale basierend auf Murrey Math Lines.
    
    Parameter:
    - period (64): Berechnungsperiode für MML
    - threshold (0.1): Schwellenwert für Signale
    """
    
    lines = ('buy_signal', 'sell_signal')
    params = (
        ('period', 64),
        ('threshold', 0.1)
    )
    
    plotlines = dict(
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        self.mml = MurreyMathLines(period=self.p.period)
        
        # Preisabstand zu den Linien
        self.dist_0_8 = abs(self.data.close - self.mml.line_0_8)
        self.dist_8_8 = abs(self.data.close - self.mml.line_8_8)
        
    def next(self):
        # Kaufsignal nahe 0/8 Linie
        if self.dist_0_8[0] < self.p.threshold * self.data.close[0]:
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Verkaufssignal nahe 8/8 Linie
        if self.dist_8_8[0] < self.p.threshold * self.data.close[0]:
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
