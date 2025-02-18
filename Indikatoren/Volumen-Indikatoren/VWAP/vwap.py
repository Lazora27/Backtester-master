import backtrader as bt

class VolumeWeightedAveragePrice(bt.Indicator):
    """
    Volume Weighted Average Price (VWAP)
    
    Berechnet den durchschnittlichen Preis gewichtet nach Handelsvolumen.
    Wird oft als fairer Preis und für die Ausführungsqualität verwendet.
    
    Formel:
    VWAP = Σ(Preis * Volumen) / Σ(Volumen)
    
    Parameter:
    - period (None): Wenn None, wird der gesamte Zeitraum verwendet
    """
    
    lines = ('vwap',)
    params = (('period', None),)
    
    plotlines = dict(
        vwap=dict(color='blue', _name='VWAP')
    )
    
    def __init__(self):
        # Typischer Preis
        typical_price = (self.data.high + self.data.low + self.data.close) / 3.0
        
        # Preis * Volumen
        price_volume = typical_price * self.data.volume
        
        if self.p.period:
            # Berechne VWAP für definierte Periode
            sum_price_volume = bt.indicators.SumN(price_volume, period=self.p.period)
            sum_volume = bt.indicators.SumN(self.data.volume, period=self.p.period)
        else:
            # Berechne VWAP für gesamten Zeitraum
            sum_price_volume = bt.indicators.Cumsum(price_volume)
            sum_volume = bt.indicators.Cumsum(self.data.volume)
        
        # VWAP Berechnung
        self.lines.vwap = sum_price_volume / sum_volume
