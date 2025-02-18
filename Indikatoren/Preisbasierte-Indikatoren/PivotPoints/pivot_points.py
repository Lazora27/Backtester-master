import backtrader as bt

class PivotPoints(bt.Indicator):
    """
    Pivot Points
    
    Berechnet klassische Pivot Points und ihre Support/Resistance Levels.
    Unterstützt verschiedene Berechnungsmethoden.
    
    Der Indikator:
    - Berechnet Pivot Point (PP)
    - Support Levels (S1, S2, S3)
    - Resistance Levels (R1, R2, R3)
    - Midpoint Levels
    
    Parameter:
    - method ('standard'): 'standard', 'woodie', 'camarilla', 'demark'
    - timeframe ('D'): Zeitrahmen für Berechnung
    """
    
    lines = ('pp', 'r1', 'r2', 'r3', 's1', 's2', 's3', 'mid_r1_s1', 'mid_r2_s2')
    params = (
        ('method', 'standard'),
        ('timeframe', 'D')
    )
    
    plotlines = dict(
        pp=dict(color='darkblue', _name='PP'),
        r1=dict(color='green', _name='R1'),
        r2=dict(color='darkgreen', _name='R2'),
        r3=dict(color='red', _name='R3'),
        s1=dict(color='orange', _name='S1'),
        s2=dict(color='darkorange', _name='S2'),
        s3=dict(color='purple', _name='S3'),
        mid_r1_s1=dict(color='gray', _name='Mid R1/S1'),
        mid_r2_s2=dict(color='darkgray', _name='Mid R2/S2')
    )
    
    def __init__(self):
        # Timeframe Data
        if self.p.timeframe == 'D':
            self.high = self.data.high(-1)
            self.low = self.data.low(-1)
            self.close = self.data.close(-1)
        else:
            self.high = self.data.high
            self.low = self.data.low
            self.close = self.data.close
            
    def standard_pivots(self):
        """Standard Pivot Point Berechnung."""
        pp = (self.high + self.low + self.close) / 3
        
        r1 = (2 * pp) - self.low
        r2 = pp + (self.high - self.low)
        r3 = r1 + (self.high - self.low)
        
        s1 = (2 * pp) - self.high
        s2 = pp - (self.high - self.low)
        s3 = s1 - (self.high - self.low)
        
        return pp, r1, r2, r3, s1, s2, s3
        
    def woodie_pivots(self):
        """Woodie's Pivot Point Berechnung."""
        pp = (self.high + self.low + 2 * self.close) / 4
        
        r1 = (2 * pp) - self.low
        r2 = pp + (self.high - self.low)
        r3 = self.high + 2 * (pp - self.low)
        
        s1 = (2 * pp) - self.high
        s2 = pp - (self.high - self.low)
        s3 = self.low - 2 * (self.high - pp)
        
        return pp, r1, r2, r3, s1, s2, s3
        
    def camarilla_pivots(self):
        """Camarilla Pivot Point Berechnung."""
        range_ = self.high - self.low
        
        pp = (self.high + self.low + self.close) / 3
        
        r1 = self.close + range_ * 1.0833
        r2 = self.close + range_ * 1.1666
        r3 = self.close + range_ * 1.2500
        
        s1 = self.close - range_ * 1.0833
        s2 = self.close - range_ * 1.1666
        s3 = self.close - range_ * 1.2500
        
        return pp, r1, r2, r3, s1, s2, s3
        
    def demark_pivots(self):
        """DeMark Pivot Point Berechnung."""
        if self.close < self.open:
            x = self.high + (2 * self.low) + self.close
        elif self.close > self.open:
            x = (2 * self.high) + self.low + self.close
        else:
            x = self.high + self.low + (2 * self.close)
            
        pp = x / 4
        
        r1 = x / 2 - self.low
        r2 = pp + (self.high - self.low)
        r3 = r1 + (self.high - self.low)
        
        s1 = x / 2 - self.high
        s2 = pp - (self.high - self.low)
        s3 = s1 - (self.high - self.low)
        
        return pp, r1, r2, r3, s1, s2, s3
        
    def next(self):
        # Pivot Points berechnen
        if self.p.method == 'woodie':
            pp, r1, r2, r3, s1, s2, s3 = self.woodie_pivots()
        elif self.p.method == 'camarilla':
            pp, r1, r2, r3, s1, s2, s3 = self.camarilla_pivots()
        elif self.p.method == 'demark':
            pp, r1, r2, r3, s1, s2, s3 = self.demark_pivots()
        else:  # standard
            pp, r1, r2, r3, s1, s2, s3 = self.standard_pivots()
            
        # Lines setzen
        self.lines.pp[0] = pp
        self.lines.r1[0] = r1
        self.lines.r2[0] = r2
        self.lines.r3[0] = r3
        self.lines.s1[0] = s1
        self.lines.s2[0] = s2
        self.lines.s3[0] = s3
        
        # Midpoints
        self.lines.mid_r1_s1[0] = (r1 + s1) / 2
        self.lines.mid_r2_s2[0] = (r2 + s2) / 2
