import backtrader as bt

class VortexIndicator(bt.Indicator):
    """
    Vortex Indicator (VI)
    
    Der Vortex Indicator besteht aus zwei Oszillatoren, die positive und negative
    Trendbewegungen messen. Kreuzt der +VI den -VI von unten, ist dies ein
    Kaufsignal, umgekehrt ein Verkaufssignal.
    
    Parameter:
    - period (14): Periode für die Berechnung
    """
    
    lines = ('vi_plus', 'vi_minus')
    params = (('period', 14),)
    
    plotlines = dict(
        vi_plus=dict(color='green'),
        vi_minus=dict(color='red')
    )
    
    def __init__(self):
        # Berechne True Range
        self.tr = bt.indicators.TrueRange(self.data)
        
        # +VM (Positive Vortex Movement)
        self.vm_plus = abs(self.data.high(0) - self.data.low(-1))
        
        # -VM (Negative Vortex Movement)
        self.vm_minus = abs(self.data.low(0) - self.data.high(-1))
        
        # Summiere die Werte über die Periode
        self.tr_sum = bt.indicators.SumN(self.tr, period=self.p.period)
        self.vm_plus_sum = bt.indicators.SumN(self.vm_plus, period=self.p.period)
        self.vm_minus_sum = bt.indicators.SumN(self.vm_minus, period=self.p.period)
        
        # Berechne +VI und -VI
        self.lines.vi_plus = self.vm_plus_sum / self.tr_sum
        self.lines.vi_minus = self.vm_minus_sum / self.tr_sum
