import backtrader as bt

class CommodityChannelIndex(bt.Indicator):
    """
    Commodity Channel Index (CCI)
    
    Misst die Abweichung des Preises vom statistischen Durchschnitt.
    Werte über +100 deuten auf überkaufte, Werte unter -100 auf überverkaufte 
    Bedingungen hin.
    
    Parameter:
    - period (20): Periode für die Berechnung
    - factor (0.015): Konstante für die CCI-Berechnung
    """
    
    lines = ('cci',)
    params = (
        ('period', 20),
        ('factor', 0.015)
    )
    
    plotlines = dict(
        cci=dict(color='purple', _name='CCI')
    )
    
    def __init__(self):
        # Typischer Preis
        typical_price = (self.data.high + self.data.low + self.data.close) / 3.0
        
        # Gleitender Durchschnitt des typischen Preises
        ma = bt.indicators.SMA(typical_price, period=self.p.period)
        
        # Mittlere Abweichung
        mean_dev = bt.indicators.MeanDeviation(typical_price, ma, period=self.p.period)
        
        # CCI Berechnung
        self.lines.cci = (typical_price - ma) / (self.p.factor * mean_dev)
