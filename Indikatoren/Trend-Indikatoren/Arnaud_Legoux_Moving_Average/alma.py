import backtrader as bt
import numpy as np

class ArnaudLegouxMovingAverage(bt.Indicator):
    """
    Arnaud Legoux Moving Average (ALMA)
    
    Der ALMA kombiniert die Vorteile einer Gaußschen Glättung mit reduziertem Lag.
    
    Formel:
    ALMA = sum(P[i] * w[i]) / sum(w[i])
    w[i] = exp(-((i - offset)^2) / (2 * sigma^2))
    
    Parameters:
    - period (20): Anzahl der Perioden
    - offset (0.85): Position des Gaußschen Filters [0, 1]
    - sigma (6): Breite des Gaußschen Filters
    """
    
    lines = ('alma',)
    params = (
        ('period', 20),
        ('offset', 0.85),
        ('sigma', 6),
    )
    
    def __init__(self):
        super(ArnaudLegouxMovingAverage, self).__init__()
        
        # Berechne die Gewichte
        m = self.p.offset * (self.p.period - 1)
        s = self.p.period / self.p.sigma
        weights = np.zeros(self.p.period)
        
        for i in range(self.p.period):
            weights[i] = np.exp(-((i - m) ** 2) / (2 * s * s))
            
        # Normalisiere die Gewichte
        weights = weights / np.sum(weights)
        
        # Erstelle den ALMA
        self.lines.alma = bt.indicators.WeightedMovingAverage(
            self.data,
            period=self.p.period,
            coef=weights
        )
