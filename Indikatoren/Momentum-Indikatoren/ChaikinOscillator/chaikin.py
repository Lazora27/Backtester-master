import backtrader as bt

class ChaikinOscillator(bt.Indicator):
    """
    Chaikin Oscillator
    
    Kombiniert Preis und Volumen, um Momentum zu messen. Basiert auf dem 
    Accumulation/Distribution Line (ADL) und der Differenz zweier EMAs der ADL.
    
    Formel:
    1. Money Flow Multiplier = ((Close - Low) - (High - Close)) / (High - Low)
    2. Money Flow Volume = Money Flow Multiplier × Volume
    3. ADL = Vorherige ADL + Money Flow Volume
    4. Chaikin Oscillator = EMA(3, ADL) - EMA(10, ADL)
    
    Parameter:
    - fast_period (3): Periode für den schnellen EMA
    - slow_period (10): Periode für den langsamen EMA
    """
    
    lines = ('chaikin',)
    params = (
        ('fast_period', 3),
        ('slow_period', 10)
    )
    
    plotlines = dict(
        chaikin=dict(color='darkblue', _name='Chaikin')
    )
    
    def __init__(self):
        # Money Flow Multiplier
        high_low = self.data.high - self.data.low
        mf_multiplier = bt.If(
            high_low != 0,
            ((self.data.close - self.data.low) - (self.data.high - self.data.close)) / high_low,
            0
        )
        
        # Money Flow Volume
        mf_volume = mf_multiplier * self.data.volume
        
        # Accumulation/Distribution Line (ADL)
        self.adl = bt.indicators.AccumulationDistribution(self.data)
        
        # Chaikin Oscillator = Differenz der EMAs der ADL
        fast_ema = bt.indicators.EMA(self.adl, period=self.p.fast_period)
        slow_ema = bt.indicators.EMA(self.adl, period=self.p.slow_period)
        
        self.lines.chaikin = fast_ema - slow_ema
