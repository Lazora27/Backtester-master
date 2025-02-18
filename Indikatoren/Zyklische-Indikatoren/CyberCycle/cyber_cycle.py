import backtrader as bt
import numpy as np

class CyberCycle(bt.Indicator):
    """
    Cyber Cycle Indicator
    
    Ein fortgeschrittener zyklischer Indikator, der Preisbewegungen in
    ihre zyklischen Komponenten zerlegt. Entwickelt von John Ehlers.
    
    Der Indikator:
    - Reduziert Lag
    - Filtert Rauschen
    - Identifiziert Wendepunkte früh
    
    Parameter:
    - period (20): Basisperiode
    - alpha (0.07): Glättungsfaktor
    - smooth (True): Ob zusätzliche Glättung angewendet werden soll
    """
    
    lines = ('cycle', 'trigger', 'smooth_cycle')
    params = (
        ('period', 20),
        ('alpha', 0.07),
        ('smooth', True)
    )
    
    plotlines = dict(
        cycle=dict(color='darkblue', _name='Cycle'),
        trigger=dict(color='red', _name='Trigger'),
        smooth_cycle=dict(color='green', _name='Smooth')
    )
    
    def __init__(self):
        self.addminperiod(self.p.period)
        
        # Initialisierung
        self.smooth_price = 0
        self.cycle1 = 0
        self.cycle2 = 0
        self.price1 = 0
        self.price2 = 0
        
    def next(self):
        # Median Price
        price = (self.data.high[0] + self.data.low[0]) / 2.0
        
        # Erste Glättung
        self.smooth_price = (price + 2 * self.price1 + 2 * 
                           self.price2) / 5.0
        
        # Cycle Berechnung
        cycle = (1.0 - 0.5 * self.p.alpha) * (1.0 - 0.5 * self.p.alpha) * \
                (self.smooth_price - 2.0 * self.price1 + self.price2) + \
                2.0 * (1.0 - self.p.alpha) * self.cycle1 - \
                (1.0 - self.p.alpha) * (1.0 - self.p.alpha) * self.cycle2
                
        self.lines.cycle[0] = cycle
        
        # Trigger Line
        self.lines.trigger[0] = self.cycle1
        
        # Geglätteter Cycle
        if self.p.smooth:
            self.lines.smooth_cycle[0] = bt.indicators.EMA(
                self.lines.cycle,
                period=8
            )[0]
        else:
            self.lines.smooth_cycle[0] = cycle
            
        # Werte aktualisieren
        self.cycle2 = self.cycle1
        self.cycle1 = cycle
        self.price2 = self.price1
        self.price1 = self.smooth_price
        
class CyberCycleOscillator(bt.Indicator):
    """
    Cyber Cycle Oscillator
    
    Ein Oszillator basierend auf dem Cyber Cycle.
    
    Parameter:
    - period (20): Basisperiode
    - overbought (100): Überkauft-Level
    - oversold (-100): Überverkauft-Level
    """
    
    lines = ('oscillator', 'signal')
    params = (
        ('period', 20),
        ('overbought', 100),
        ('oversold', -100)
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
        # Cyber Cycle
        self.cc = CyberCycle(
            self.data0,
            period=self.p.period
        )
        
        # Oszillator
        self.lines.oscillator = 100 * (self.cc.cycle / 
                                     bt.indicators.Highest(abs(self.cc.cycle),
                                                        period=self.p.period))
        
        # Signallinie
        self.lines.signal = bt.indicators.EMA(
            self.lines.oscillator,
            period=9
        )
        
        # Zonen
        self.overbought = bt.indicators.CrossOver(
            self.lines.oscillator,
            self.p.overbought
        )
        
        self.oversold = bt.indicators.CrossOver(
            self.lines.oscillator,
            self.p.oversold
        )
