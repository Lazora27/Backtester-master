import backtrader as bt

class DonchianChannels(bt.Indicator):
    """
    Donchian Channels
    
    Zeigt den höchsten Hoch- und niedrigsten Tiefkurs über eine bestimmte Periode an.
    Die Mittellinie ist der Durchschnitt aus oberem und unterem Band.
    
    Parameter:
    - period (20): Periode für die Berechnung
    """
    
    lines = ('dcm', 'dch', 'dcl')  # middle, high, low
    params = (('period', 20),)
    
    plotinfo = dict(subplot=False)
    plotlines = dict(
        dcm=dict(ls='--', color='gray'),
        dch=dict(color='green'),
        dcl=dict(color='red'),
    )
    
    def __init__(self):
        super(DonchianChannels, self).__init__()
        
        # Höchstes Hoch der Periode
        self.lines.dch = bt.indicators.Highest(self.data.high, period=self.p.period)
        
        # Niedrigstes Tief der Periode
        self.lines.dcl = bt.indicators.Lowest(self.data.low, period=self.p.period)
        
        # Mittellinie
        self.lines.dcm = (self.lines.dch + self.lines.dcl) / 2.0
