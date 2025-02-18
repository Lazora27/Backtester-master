import backtrader as bt

class DetrendedPriceOscillator(bt.Indicator):
    """
    Detrended Price Oscillator (DPO)
    
    Entfernt den Trend aus der Preisreihe, um zyklische Komponenten
    besser sichtbar zu machen.
    
    Der Indikator:
    - Eliminiert langfristige Trends
    - Zeigt Zyklen und Wendepunkte
    - Identifiziert überkaufte/überverkaufte Bereiche
    
    Formel:
    DPO = Price - Simple Moving Average(Price, period/2 + 1)
    verschoben um (period/2 + 1) Perioden
    
    Parameter:
    - period (20): Berechnungsperiode
    - centered (True): Ob der Indikator zentriert werden soll
    """
    
    lines = ('dpo', 'signal')
    params = (
        ('period', 20),
        ('centered', True)
    )
    
    plotlines = dict(
        dpo=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        ),
        signal=dict(color='blue', _name='Signal')
    )
    
    def __init__(self):
        # Berechne Verschiebung
        self.shift = int(self.p.period / 2 + 1)
        
        # Moving Average
        ma = bt.indicators.SMA(
            self.data0,
            period=self.p.period
        )
        
        if self.p.centered:
            # Zentrierte Version
            self.lines.dpo = self.data0(-self.shift) - ma
        else:
            # Nicht-zentrierte Version
            self.lines.dpo = self.data0 - ma(-self.shift)
            
        # Signallinie
        self.lines.signal = bt.indicators.EMA(
            self.lines.dpo,
            period=9
        )
        
class DPOCycles(bt.Indicator):
    """
    DPO Cycle Analysis
    
    Analysiert die Zyklen im DPO für Handelssignale.
    
    Parameter:
    - period (20): DPO-Periode
    - cycle_threshold (0): Schwellenwert für Zyklusidentifikation
    """
    
    lines = ('cycle_strength',)
    params = (
        ('period', 20),
        ('cycle_threshold', 0)
    )
    
    plotlines = dict(
        cycle_strength=dict(
            _method='bar',
            alpha=0.5,
            width=0.7,
            color='gray'
        )
    )
    
    def __init__(self):
        # DPO berechnen
        self.dpo = DetrendedPriceOscillator(
            self.data0,
            period=self.p.period
        )
        
        # Zero-Crossings zählen
        self.crossover = bt.indicators.CrossOver(
            self.dpo.dpo,
            0.0
        )
        
        # Zyklusstärke
        self.lines.cycle_strength = bt.If(
            abs(self.dpo.dpo) > self.p.cycle_threshold,
            abs(self.dpo.dpo),
            0
        )
