import backtrader as bt
import numpy as np

class UlcerIndex(bt.Indicator):
    """
    Ulcer Index
    
    Misst das Drawdown-Risiko, indem er die Tiefe und Dauer von Preisrückgängen
    berücksichtigt. Je höher der Index, desto größer das Drawdown-Risiko.
    
    Formel:
    1. Prozent-Drawdown = ((Close - 14-Perioden-Hoch) / 14-Perioden-Hoch) × 100
    2. Quadrierter Durchschnitt = (Σ(Prozent-Drawdown²)) / n
    3. Ulcer Index = √Quadrierter Durchschnitt
    
    Parameter:
    - period (14): Berechnungsperiode
    """
    
    lines = ('ui',)
    params = (('period', 14),)
    
    plotlines = dict(
        ui=dict(color='red', _name='Ulcer')
    )
    
    def __init__(self):
        # Höchstkurs über die Periode
        highest = bt.indicators.Highest(self.data, period=self.p.period)
        
        # Prozentualer Drawdown
        pct_drawdown = ((self.data - highest) / highest) * 100.0
        
        # Quadriere den Drawdown
        squared_drawdown = pct_drawdown * pct_drawdown
        
        # Durchschnitt der quadrierten Drawdowns
        avg_squared = bt.indicators.SumN(squared_drawdown, period=self.p.period) / self.p.period
        
        # Wurzel für den Ulcer Index
        self.lines.ui = bt.indicators.SqrtN(avg_squared)
        
    def next(self):
        # Hier könnten zusätzliche Signale implementiert werden
        # z.B. Risikomanagement basierend auf UI-Levels
        pass
