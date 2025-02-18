import backtrader as bt
import numpy as np

class HistoricalVolatility(bt.Indicator):
    """
    Historical Volatility
    
    Berechnet die annualisierte historische Volatilität basierend auf 
    logarithmischen Renditen. Wird oft für Optionspreismodelle verwendet.
    
    Formel:
    1. Log Returns = ln(Close/Previous Close)
    2. Standard Deviation of Log Returns
    3. Annualized Volatility = StdDev × √(Trading Days per Year)
    
    Parameter:
    - period (20): Berechnungsperiode
    - annual_factor (252): Handelstage pro Jahr für Annualisierung
    - normalize (False): Ob die Volatilität als Prozent ausgegeben werden soll
    """
    
    lines = ('hv', 'non_annualized')
    params = (
        ('period', 20),
        ('annual_factor', 252),  # Handelstage pro Jahr
        ('normalize', False)
    )
    
    plotlines = dict(
        hv=dict(color='darkblue', _name='HV'),
        non_annualized=dict(_plotskip=True)
    )
    
    def __init__(self):
        # Logarithmische Renditen
        self.logret = bt.indicators.LogReturns(self.data)
        
        # Nicht-annualisierte Volatilität
        self.lines.non_annualized = stddev = bt.indicators.StandardDeviation(
            self.logret,
            period=self.p.period
        )
        
        # Annualisierte Volatilität
        annualized = stddev * np.sqrt(self.p.annual_factor)
        
        if self.p.normalize:
            # Ausgabe als Prozent
            self.lines.hv = annualized * 100
        else:
            # Ausgabe als Dezimalzahl
            self.lines.hv = annualized
