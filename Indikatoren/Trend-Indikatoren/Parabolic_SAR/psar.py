import backtrader as bt

class ParabolicSAR(bt.Indicator):
    """
    Parabolic SAR (Stop and Reverse)
    
    Ein Trend-Following Indikator, der potenzielle Trendwenden anzeigt und
    als Trailing-Stop verwendet werden kann.
    
    Parameter:
    - af_start (0.02): Anfangswert des Acceleration Factor
    - af_inc (0.02): Increment des Acceleration Factor
    - af_max (0.2): Maximaler Wert des Acceleration Factor
    """
    
    lines = ('psar',)
    params = (
        ('af_start', 0.02),
        ('af_inc', 0.02),
        ('af_max', 0.2),
    )
    
    plotinfo = dict(subplot=False, plotmarkers=True)
    plotlines = dict(
        psar=dict(marker='.', markersize=8.0, color='black', fillstyle='full')
    )
    
    def __init__(self):
        super(ParabolicSAR, self).__init__()
        
        self.trend = 1  # 1 für Aufwärtstrend, -1 für Abwärtstrend
        self.af = self.p.af_start  # Acceleration Factor
        self.ep = float('-inf')  # Extreme Point
        self.hp = float('-inf')  # Highest Point
        self.lp = float('inf')   # Lowest Point
        self.sar = None
        
    def next(self):
        if len(self) <= 1:
            self.sar = self.data.low[0]  # Initialisiere SAR mit erstem Low
            self.trend = 1
            self.ep = self.data.high[0]
            return
        
        # Berechne SAR
        if self.trend == 1:  # Aufwärtstrend
            if self.data.low[0] > self.sar:
                # Trend setzt sich fort
                self.sar = self.sar + self.af * (self.ep - self.sar)
                if self.data.high[0] > self.ep:
                    self.ep = self.data.high[0]
                    self.af = min(self.af + self.p.af_inc, self.p.af_max)
            else:
                # Trendwende nach unten
                self.trend = -1
                self.sar = self.ep
                self.ep = self.data.low[0]
                self.af = self.p.af_start
        else:  # Abwärtstrend
            if self.data.high[0] < self.sar:
                # Trend setzt sich fort
                self.sar = self.sar + self.af * (self.ep - self.sar)
                if self.data.low[0] < self.ep:
                    self.ep = self.data.low[0]
                    self.af = min(self.af + self.p.af_inc, self.p.af_max)
            else:
                # Trendwende nach oben
                self.trend = 1
                self.sar = self.ep
                self.ep = self.data.high[0]
                self.af = self.p.af_start
        
        # Begrenze SAR-Werte
        if self.trend == 1:
            self.sar = min(self.sar, self.data.low[0], self.data.low[-1])
        else:
            self.sar = max(self.sar, self.data.high[0], self.data.high[-1])
            
        self.lines.psar[0] = self.sar
