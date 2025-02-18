import backtrader as bt

class AroonIndicator(bt.Indicator):
    """
    Aroon Indicator
    
    Der Aroon Indicator besteht aus zwei Linien:
    - Aroon Up: Misst die Zeit seit dem letzten Höchststand
    - Aroon Down: Misst die Zeit seit dem letzten Tiefststand
    
    Werte nahe 100 zeigen einen starken Trend an.
    
    Parameter:
    - period (25): Periode für die Berechnung
    """
    
    lines = ('aroon_up', 'aroon_down')
    params = (('period', 25),)
    
    plotlines = dict(
        aroon_up=dict(color='green'),
        aroon_down=dict(color='red')
    )
    
    def __init__(self):
        # Speichere die letzten period+1 Werte
        self.addminperiod(self.p.period + 1)
        
    def next(self):
        # Finde den letzten Höchststand
        highest = float('-inf')
        days_since_high = 0
        for i in range(self.p.period + 1):
            if self.data.high[-i] > highest:
                highest = self.data.high[-i]
                days_since_high = i
                
        # Finde den letzten Tiefststand
        lowest = float('inf')
        days_since_low = 0
        for i in range(self.p.period + 1):
            if self.data.low[-i] < lowest:
                lowest = self.data.low[-i]
                days_since_low = i
                
        # Berechne Aroon Up und Down
        self.lines.aroon_up[0] = ((self.p.period - days_since_high) / self.p.period) * 100
        self.lines.aroon_down[0] = ((self.p.period - days_since_low) / self.p.period) * 100
