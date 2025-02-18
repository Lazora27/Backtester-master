import backtrader as bt

class AccumulationDistributionLine(bt.Indicator):
    """
    Accumulation/Distribution Line (A/D Line)
    
    Misst Geld-Flow in und aus einem Asset. Verwendet die Position des Schlusskurses
    innerhalb der Handelsspanne, um das Volumen zu gewichten.
    
    Formel:
    Money Flow Multiplier = ((Close - Low) - (High - Close)) / (High - Low)
    Money Flow Volume = Money Flow Multiplier × Volume
    A/D = Previous A/D + Current Money Flow Volume
    
    Parameter:
    - movav (None): Optional, Moving Average Typ für Signallinie
    - movav_period (20): Periode für Moving Average
    """
    
    lines = ('ad', 'signal')
    params = (
        ('movav', None),
        ('movav_period', 20)
    )
    
    plotlines = dict(
        ad=dict(color='blue', _name='A/D Line'),
        signal=dict(color='red', _name='Signal')
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
        
        # Accumulation/Distribution Line
        self.lines.ad = bt.indicators.Cumsum(mf_volume)
        
        # Optional: Signallinie
        if self.p.movav:
            self.lines.signal = self.p.movav(self.lines.ad, period=self.p.movav_period)
        else:
            self.lines.signal = bt.indicators.SMA(self.lines.ad, period=self.p.movav_period)
