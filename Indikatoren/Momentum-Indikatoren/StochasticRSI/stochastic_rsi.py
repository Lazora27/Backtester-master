import backtrader as bt

class StochasticRSI(bt.Indicator):
    """
    Stochastic RSI
    
    Kombiniert die Vorteile des Stochastic Oscillators und des RSI.
    Berechnet den Stochastic Oscillator auf Basis der RSI-Werte statt der Preise.
    
    Parameter:
    - period (14): Periode für RSI und StochRSI Berechnung
    - period_stoch (14): Periode für die Stochastic Berechnung
    - period_d (3): Periode für die Signal-Linie
    """
    
    lines = ('stochrsi', 'signal')
    params = (
        ('period', 14),
        ('period_stoch', 14),
        ('period_d', 3),
    )
    
    plotlines = dict(
        stochrsi=dict(color='blue', _name='StochRSI'),
        signal=dict(color='red', _name='Signal')
    )
    
    def __init__(self):
        # Berechne RSI
        rsi = bt.indicators.RSI(self.data, period=self.p.period)
        
        # Höchster und niedrigster RSI über period_stoch
        highest_rsi = bt.indicators.Highest(rsi, period=self.p.period_stoch)
        lowest_rsi = bt.indicators.Lowest(rsi, period=self.p.period_stoch)
        
        # StochRSI Berechnung
        self.lines.stochrsi = 100 * (rsi - lowest_rsi) / (highest_rsi - lowest_rsi)
        
        # Signal-Linie
        self.lines.signal = bt.indicators.SMA(self.lines.stochrsi, period=self.p.period_d)
