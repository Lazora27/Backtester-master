import backtrader as bt

class RateOfChange(bt.Indicator):
    """
    Rate of Change (ROC)
    
    Misst die prozentuale Veränderung des Preises über eine bestimmte Periode.
    Ein positiver ROC zeigt steigende Preise an, ein negativer ROC fallende Preise.
    
    Formel: ROC = ((Aktueller Preis - Preis vor n Perioden) / Preis vor n Perioden) * 100
    
    Parameter:
    - period (12): Anzahl der Perioden für die Berechnung
    """
    
    lines = ('roc',)
    params = (('period', 12),)
    
    plotlines = dict(
        roc=dict(color='darkgreen', _name='ROC')
    )
    
    def __init__(self):
        # Hole den Preis vor n Perioden
        price_n_periods_ago = self.data(-self.p.period)
        
        # Berechne ROC
        self.lines.roc = ((self.data / price_n_periods_ago) - 1.0) * 100
