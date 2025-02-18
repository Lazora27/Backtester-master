import backtrader as bt

class StandardDeviationIndicator(bt.Indicator):
    """
    Standard Deviation Indicator
    
    Misst die Volatilität durch Berechnung der Standardabweichung der Preise.
    Höhere Werte zeigen höhere Volatilität an.
    
    Formel:
    StdDev = sqrt(Σ(x - μ)² / n)
    x = Preis
    μ = Durchschnittspreis
    n = Anzahl der Perioden
    
    Parameter:
    - period (20): Berechnungsperiode
    - movav (SMA): Typ des gleitenden Durchschnitts für Mittelwert
    - normalize (False): Ob die Standardabweichung normalisiert werden soll
    """
    
    lines = ('stddev', 'normalized')
    params = (
        ('period', 20),
        ('movav', bt.indicators.SMA),
        ('normalize', False)  # Normalisierung optional
    )
    
    plotlines = dict(
        stddev=dict(color='red', _name='StdDev'),
        normalized=dict(_plotskip=True)
    )
    
    def __init__(self):
        # Berechne Standardabweichung
        self.lines.stddev = bt.indicators.StandardDeviation(
            self.data,
            period=self.p.period,
            movav=self.p.movav
        )
        
        if self.p.normalize:
            # Normalisierte Standardabweichung (0-100 Skala)
            highest_stddev = bt.indicators.Highest(self.lines.stddev, period=self.p.period)
            lowest_stddev = bt.indicators.Lowest(self.lines.stddev, period=self.p.period)
            
            self.lines.normalized = bt.If(
                (highest_stddev - lowest_stddev) != 0,
                100 * (self.lines.stddev - lowest_stddev) / (highest_stddev - lowest_stddev),
                50  # Standardwert wenn keine Variation
            )
