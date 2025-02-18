import backtrader as bt

class MoneyFlowIndex(bt.Indicator):
    """
    Money Flow Index (MFI)
    
    Ein volumengewichteter RSI. Vergleicht positive und negative Money Flow über
    eine bestimmte Periode. Werte über 80 zeigen überkauft, unter 20 überverkauft an.
    
    Formel:
    Typical Price = (High + Low + Close) / 3
    Raw Money Flow = Typical Price × Volume
    Money Flow Ratio = Positive Money Flow / Negative Money Flow
    MFI = 100 - (100 / (1 + Money Flow Ratio))
    
    Parameter:
    - period (14): Periode für die Berechnung
    """
    
    lines = ('mfi',)
    params = (('period', 14),)
    
    plotlines = dict(
        mfi=dict(color='navy', _name='MFI')
    )
    
    def __init__(self):
        # Typical Price
        typical_price = (self.data.high + self.data.low + self.data.close) / 3.0
        
        # Raw Money Flow
        raw_money_flow = typical_price * self.data.volume
        
        # Positive/Negative Money Flow basierend auf Typical Price Änderung
        price_change = typical_price - typical_price(-1)
        pos_money_flow = bt.If(price_change > 0, raw_money_flow, 0.0)
        neg_money_flow = bt.If(price_change < 0, raw_money_flow, 0.0)
        
        # Summiere positive und negative Money Flows
        pos_flow_sum = bt.indicators.SumN(pos_money_flow, period=self.p.period)
        neg_flow_sum = bt.indicators.SumN(neg_money_flow, period=self.p.period)
        
        # Money Flow Ratio
        money_ratio = bt.If(
            neg_flow_sum != 0,
            pos_flow_sum / neg_flow_sum,
            0.0
        )
        
        # Money Flow Index
        self.lines.mfi = 100.0 - (100.0 / (1.0 + money_ratio))
