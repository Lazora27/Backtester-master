import backtrader as bt

class VolumeWeightedMovingAverage(bt.Indicator):
    """
    Volume Weighted Moving Average (VWMA)
    
    Der VWMA gewichtet die Preise basierend auf dem Handelsvolumen.
    Dies gibt Perioden mit höherem Volumen mehr Gewicht.
    
    Formel:
    VWMA = Σ(Price * Volume) / Σ(Volume)
    
    Parameter:
    - period (20): Anzahl der Perioden für die Berechnung
    """
    
    lines = ('vwma',)
    params = (('period', 20),)
    
    def __init__(self):
        # Berechne das Produkt von Preis und Volumen
        price_volume = self.data * self.data.volume
        
        # Summiere Preis*Volumen und Volumen über die Periode
        sum_price_volume = bt.indicators.SumN(price_volume, period=self.p.period)
        sum_volume = bt.indicators.SumN(self.data.volume, period=self.p.period)
        
        # VWMA ist das Verhältnis der beiden Summen
        self.lines.vwma = sum_price_volume / sum_volume
