import backtrader as bt
import numpy as np

class ZigZagIndicator(bt.Indicator):
    """
    Zig Zag Indicator
    
    Verbindet signifikante Hochs und Tiefs im Chart, um den Trend zu visualisieren.
    Ignoriert kleine Preisbewegungen unter dem definierten Prozentsatz.
    
    Parameter:
    - percentage (5.0): Minimale Preisänderung in Prozent für einen neuen Punkt
    """
    
    lines = ('zigzag',)
    params = (('percentage', 5.0),)
    
    plotinfo = dict(subplot=False)
    plotlines = dict(
        zigzag=dict(color='black', width=2.0)
    )
    
    def __init__(self):
        super(ZigZagIndicator, self).__init__()
        
        self.last_high = float('-inf')
        self.last_low = float('inf')
        self.last_price = None
        self.trend = None  # 1 für aufwärts, -1 für abwärts
        
    def next(self):
        current_price = self.data[0]
        
        if len(self) <= 1:
            self.last_price = current_price
            self.lines.zigzag[0] = current_price
            return
            
        # Berechne prozentuale Änderung
        if self.trend is None:
            # Initialisiere Trend
            self.trend = 1 if current_price > self.last_price else -1
            self.lines.zigzag[0] = self.last_price
            return
            
        price_change = abs((current_price - self.last_price) / self.last_price * 100)
        
        if price_change >= self.p.percentage:
            if self.trend == 1:  # Aufwärtstrend
                if current_price < self.last_price:
                    # Trendwende nach unten
                    self.trend = -1
                    self.last_price = current_price
                    self.lines.zigzag[0] = current_price
                else:
                    # Neues Hoch
                    self.last_price = current_price
                    self.lines.zigzag[0] = current_price
            else:  # Abwärtstrend
                if current_price > self.last_price:
                    # Trendwende nach oben
                    self.trend = 1
                    self.last_price = current_price
                    self.lines.zigzag[0] = current_price
                else:
                    # Neues Tief
                    self.last_price = current_price
                    self.lines.zigzag[0] = current_price
        else:
            # Keine signifikante Änderung
            self.lines.zigzag[0] = self.lines.zigzag[-1]
