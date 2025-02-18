import backtrader as bt

class McClellanOscillator(bt.Indicator):
    """
    McClellan Oscillator
    
    Ein Momentum-Indikator für die Marktbreite, der die Differenz zwischen zwei
    exponentiellen gleitenden Durchschnitten des Advance-Decline-Spreads verwendet.
    
    Formel:
    1. Net Advances = Advances - Declines
    2. McClellan Oscillator = 19-Tage EMA(Net Advances) - 39-Tage EMA(Net Advances)
    
    Parameter:
    - fast_period (19): Periode für schnellen EMA
    - slow_period (39): Periode für langsamen EMA
    """
    
    lines = ('oscillator', 'signal')
    params = (
        ('fast_period', 19),
        ('slow_period', 39),
        ('signal_period', 9)
    )
    
    plotlines = dict(
        oscillator=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        ),
        signal=dict(color='blue', _name='Signal')
    )
    
    def __init__(self):
        # Net Advances berechnen
        net_advances = self.data0 - self.data1
        
        # EMAs berechnen
        fast_ema = bt.indicators.EMA(net_advances, period=self.p.fast_period)
        slow_ema = bt.indicators.EMA(net_advances, period=self.p.slow_period)
        
        # McClellan Oscillator
        self.lines.oscillator = fast_ema - slow_ema
        
        # Signal Line
        self.lines.signal = bt.indicators.EMA(
            self.lines.oscillator,
            period=self.p.signal_period
        )
        
    def next(self):
        # Hier könnten zusätzliche Signale implementiert werden
        # z.B. Divergenzen oder Überkreuzungen mit der Signallinie
        pass
