import backtrader as bt

class EaseOfMovement(bt.Indicator):
    """
    Ease of Movement (EMV)
    
    Zeigt die "Leichtigkeit" der Preisbewegung an. Positive Werte bedeuten, dass
    der Preis leicht steigt, negative Werte zeigen an, dass er leicht fällt.
    
    Formel:
    Distance Moved = ((H + L) / 2) - ((Prior H + Prior L) / 2)
    Box Ratio = Volume / (High - Low)
    EMV = Distance Moved / Box Ratio
    
    Parameter:
    - period (14): Glättungsperiode
    - scale (10000): Skalierungsfaktor
    """
    
    lines = ('eom', 'eom_ma')
    params = (
        ('period', 14),
        ('scale', 10000)
    )
    
    plotlines = dict(
        eom=dict(_plotskip=True),  # Raw EMV wird nicht geplottet
        eom_ma=dict(color='navy', _name='EOM')  # Nur geglättete Linie wird gezeigt
    )
    
    def __init__(self):
        # Mittelpunktbewegung
        mid_point_move = ((self.data.high + self.data.low) / 2.0 -
                         (self.data.high(-1) + self.data.low(-1)) / 2.0)
        
        # Box Ratio
        box_ratio = self.data.volume / (self.data.high - self.data.low)
        
        # Ease of Movement
        self.lines.eom = (mid_point_move / box_ratio) * self.p.scale
        
        # Geglätteter EMV
        self.lines.eom_ma = bt.indicators.SMA(self.lines.eom, period=self.p.period)
