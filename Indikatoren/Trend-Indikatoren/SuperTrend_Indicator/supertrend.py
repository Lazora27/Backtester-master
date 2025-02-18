import backtrader as bt

class SuperTrend(bt.Indicator):
    """
    SuperTrend Indicator
    
    Ein Trend-Following Indikator, der auf dem ATR (Average True Range) basiert.
    Zeigt Auf- und Abwärtstrends an und kann als Trailing-Stop verwendet werden.
    
    Parameter:
    - period (10): Periode für ATR-Berechnung
    - multiplier (3.0): Multiplikator für die Bandbreite
    """
    
    lines = ('supertrend', 'direction')  # direction: 1=long, -1=short
    params = (
        ('period', 10),
        ('multiplier', 3.0),
    )
    
    plotinfo = dict(subplot=False)
    plotlines = dict(
        supertrend=dict(linestyle='-', linewidth=2.0),
        direction=dict(skip=True)  # Richtung wird nicht geplottet
    )
    
    def __init__(self):
        super(SuperTrend, self).__init__()
        
        # Berechne True Range und ATR
        self.atr = bt.indicators.ATR(self.data, period=self.p.period)
        
        # Berechne Basic Upper und Lower Bands
        self.hl2 = (self.data.high + self.data.low) / 2.0
        self.basic_ub = self.hl2 + (self.p.multiplier * self.atr)
        self.basic_lb = self.hl2 - (self.p.multiplier * self.atr)
        
        # Initialisiere Arrays für final upper/lower bands
        self.final_ub = [0.0] * len(self.data)
        self.final_lb = [0.0] * len(self.data)
        self.direction = [1.0] * len(self.data)  # 1 für Aufwärtstrend, -1 für Abwärtstrend
        self.supertrend = [0.0] * len(self.data)
        
    def next(self):
        i = len(self) - 1
        
        if i < 1:
            self.final_ub[i] = self.basic_ub[i]
            self.final_lb[i] = self.basic_lb[i]
            self.direction[i] = 1
            self.supertrend[i] = self.final_lb[i]
            return
        
        # Berechne Final Upper Band
        if self.basic_ub[i] < self.final_ub[i-1] or self.data.close[i-1] > self.final_ub[i-1]:
            self.final_ub[i] = self.basic_ub[i]
        else:
            self.final_ub[i] = self.final_ub[i-1]
            
        # Berechne Final Lower Band
        if self.basic_lb[i] > self.final_lb[i-1] or self.data.close[i-1] < self.final_lb[i-1]:
            self.final_lb[i] = self.basic_lb[i]
        else:
            self.final_lb[i] = self.final_lb[i-1]
            
        # Berechne SuperTrend
        if self.direction[i-1] == 1:
            if self.data.close[i] <= self.final_ub[i]:
                self.direction[i] = -1
                self.supertrend[i] = self.final_ub[i]
            else:
                self.direction[i] = 1
                self.supertrend[i] = self.final_lb[i]
        else:
            if self.data.close[i] >= self.final_lb[i]:
                self.direction[i] = 1
                self.supertrend[i] = self.final_lb[i]
            else:
                self.direction[i] = -1
                self.supertrend[i] = self.final_ub[i]
                
        self.lines.supertrend[0] = self.supertrend[i]
        self.lines.direction[0] = self.direction[i]
