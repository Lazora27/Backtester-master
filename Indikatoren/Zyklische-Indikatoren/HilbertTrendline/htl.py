import backtrader as bt
import numpy as np

class HilbertTrendline(bt.Indicator):
    """
    Hilbert Transform - Instantaneous Trendline
    
    Ein adaptiver Trendindikator, der die Hilbert-Transformation nutzt, um
    die momentane Trendrichtung zu bestimmen. Basiert auf John Ehlers' Arbeiten.
    
    Der Indikator:
    - Passt sich automatisch an verschiedene Marktbedingungen an
    - Reduziert Lag im Vergleich zu traditionellen MAs
    - Identifiziert Trendwechsel früher
    
    Parameter:
    - period (20): Basisperiode für die Berechnung
    - smooth_period (3): Glättungsperiode
    """
    
    lines = ('trendline', 'slope', 'momentum')
    params = (
        ('period', 20),
        ('smooth_period', 3)
    )
    
    plotlines = dict(
        trendline=dict(color='darkblue', _name='HTL'),
        slope=dict(color='red', _name='Slope'),
        momentum=dict(_plotskip=True)
    )
    
    def __init__(self):
        self.addminperiod(self.p.period)
        
        # Preisglättung
        self.smooth_price = bt.indicators.SMA(
            self.data0,
            period=self.p.smooth_period
        )
        
        # Hilbert Transform Komponenten
        self.quad = np.zeros(self.p.period)
        self.in_phase = np.zeros(self.p.period)
        self.prev_trendline = 0
        
    def next(self):
        # Aktualisiere Quadratur und In-Phase Komponenten
        for i in range(self.p.period - 1, 0, -1):
            self.quad[i] = self.quad[i-1]
            self.in_phase[i] = self.in_phase[i-1]
            
        self.quad[0] = self.smooth_price[0]
        self.in_phase[0] = self.smooth_price[-3]
        
        # Hilbert Transform
        re = 0
        im = 0
        for i in range(self.p.period):
            re += self.in_phase[i] * np.cos(i * np.pi / self.p.period)
            im += self.quad[i] * np.sin(i * np.pi / self.p.period)
            
        # Trendline berechnen
        if abs(re) > 0:
            phase = np.arctan2(im, re)
            trendline = self.smooth_price[0] + (im * np.cos(phase) - re * np.sin(phase))
        else:
            trendline = self.smooth_price[0]
            
        self.lines.trendline[0] = trendline
        
        # Steigung berechnen
        self.lines.slope[0] = trendline - self.prev_trendline
        self.prev_trendline = trendline
        
        # Momentum
        self.lines.momentum[0] = self.lines.slope[0] * self.lines.slope[-1]
        
class HilbertTrendSignals(bt.Indicator):
    """
    Hilbert Trend Signals
    
    Generiert Handelssignale basierend auf der Hilbert Trendline.
    
    Parameter:
    - period (20): Basisperiode für die HTL
    - threshold (0): Schwellenwert für Signale
    """
    
    lines = ('signal',)
    params = (
        ('period', 20),
        ('threshold', 0)
    )
    
    plotlines = dict(
        signal=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        )
    )
    
    def __init__(self):
        # Hilbert Trendline
        self.htl = HilbertTrendline(
            self.data0,
            period=self.p.period
        )
        
        # Signale basierend auf Momentum und Steigung
        self.lines.signal = bt.If(
            self.htl.momentum > self.p.threshold,
            1,
            bt.If(self.htl.momentum < -self.p.threshold, -1, 0)
        )
