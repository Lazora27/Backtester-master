import backtrader as bt

class ChaikinMoneyFlow(bt.Indicator):
    """
    Chaikin Money Flow (CMF)
    
    Kombiniert Preis und Volumen, um den Buying/Selling Pressure zu messen.
    Positive Werte zeigen Akkumulation (Kaufdruck), negative Distribution 
    (Verkaufsdruck) an.
    
    Formel:
    Money Flow Multiplier = ((Close - Low) - (High - Close)) / (High - Low)
    Money Flow Volume = Money Flow Multiplier × Volume
    CMF = Sum(Money Flow Volume) / Sum(Volume) für n Perioden
    
    Parameter:
    - period (20): Periode für die Berechnung
    """
    
    lines = ('cmf',)
    params = (('period', 20),)
    
    plotlines = dict(
        cmf=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        )
    )
    
    def __init__(self):
        # Money Flow Multiplier
        high_low = self.data.high - self.data.low
        close_low = self.data.close - self.data.low
        high_close = self.data.high - self.data.close
        
        mf_multiplier = bt.If(
            high_low != 0,
            ((close_low - high_close) / high_low),
            0.0
        )
        
        # Money Flow Volume
        mf_volume = mf_multiplier * self.data.volume
        
        # Summiere Money Flow Volume und Volumen über die Periode
        sum_mf_volume = bt.indicators.SumN(mf_volume, period=self.p.period)
        sum_volume = bt.indicators.SumN(self.data.volume, period=self.p.period)
        
        # Chaikin Money Flow
        self.lines.cmf = sum_mf_volume / sum_volume
