import backtrader as bt

class ChandeMomentumOscillator(bt.Indicator):
    """
    Chande Momentum Oscillator (CMO)
    
    Ein Momentum-Indikator, der die Differenz zwischen der Summe der Aufwärts- und
    Abwärtsbewegungen im Verhältnis zu ihrer Summe misst. Ähnlich wie der RSI,
    aber mit einer anderen Berechnungsmethode.
    
    Formel:
    CMO = 100 * ((Su - Sd)/(Su + Sd))
    Su = Summe der Aufwärtsbewegungen über n Perioden
    Sd = Summe der Abwärtsbewegungen über n Perioden
    
    Parameter:
    - period (14): Periode für die Berechnung
    """
    
    lines = ('cmo',)
    params = (('period', 14),)
    
    plotlines = dict(
        cmo=dict(color='darkblue', _name='CMO')
    )
    
    def __init__(self):
        # Berechne Preisänderungen
        price_change = self.data - self.data(-1)
        
        # Trenne positive und negative Änderungen
        up_moves = bt.If(price_change > 0, price_change, 0.0)
        down_moves = bt.If(price_change < 0, -price_change, 0.0)
        
        # Summiere Auf- und Abwärtsbewegungen
        sum_up = bt.indicators.SumN(up_moves, period=self.p.period)
        sum_down = bt.indicators.SumN(down_moves, period=self.p.period)
        
        # Berechne CMO
        total_moves = sum_up + sum_down
        self.lines.cmo = bt.If(
            total_moves != 0,
            100.0 * (sum_up - sum_down) / total_moves,
            0.0
        )
