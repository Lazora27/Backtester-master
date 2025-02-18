import backtrader as bt
import numpy as np

class EhlersDecycler(bt.Indicator):
    """
    Ehlers Decycler
    
    Eine fortgeschrittene Implementierung des Decycler-Konzepts
    nach John Ehlers, mit verbesserter Zykluserkennung und
    Trendextraktion.
    
    Features:
    - Ehlers Super Smoother Filter
    - Adaptive Zykluserkennung
    - Trendextraktion
    - Signalgenerierung
    
    Parameter:
    - hp_period (40): Hochpass-Filterperiode
    - cutoff (0.1): Grenzfrequenz
    - smooth_period (10): Glättungsperiode
    """
    
    lines = ('decycler', 'super_smoother',
             'cycle_period', 'trend_quality',
             'signal')
             
    params = (
        ('hp_period', 40),
        ('cutoff', 0.1),
        ('smooth_period', 10)
    )
    
    plotlines = dict(
        decycler=dict(color='blue', _name='Decycler'),
        super_smoother=dict(color='red', _name='Super Smoother'),
        cycle_period=dict(color='green', _name='Cycle Period'),
        trend_quality=dict(color='purple', _name='Trend Quality'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(EhlersDecycler, self).__init__()
        
        # Historie
        self.price_history = []
        self.decycler_history = []
        
        # Filter-Koeffizienten
        self.calculate_filter_coefficients()
        
    def calculate_filter_coefficients(self):
        """
        Berechnet die Filter-Koeffizienten.
        """
        self.a1 = np.exp(-np.sqrt(2) * np.pi * self.p.cutoff)
        self.a2 = 2 * self.a1 * np.cos(
            np.sqrt(2) * np.pi * self.p.cutoff
        )
        self.a3 = -self.a1 * self.a1
        self.b1 = -(2 * self.a1)
        self.b2 = self.a1 * self.a1
        self.c1 = 1 - self.a1
        
    def super_smoother_filter(self, data):
        """
        Wendet den Ehlers Super Smoother Filter an.
        """
        if len(data) < 3:
            return data[-1] if data else 0
            
        return (
            self.c1 * (data[-1] + data[-2]) / 2 +
            self.a1 * data[-2] +
            self.a2 * data[-3] +
            self.a3 * data[-4]
            if len(data) >= 4
            else data[-1]
        )
        
    def calculate_cycle_period(self):
        """
        Berechnet die dominante Zyklusperiode.
        """
        if len(self.price_history) < 4:
            return self.p.hp_period
            
        # Ehlers' Dominant Cycle Period
        real = (
            self.price_history[-1] -
            2 * self.price_history[-2] +
            self.price_history[-3]
        )
        imag = (
            (self.price_history[-1] -
             self.price_history[-3]) / 2
        )
        
        if imag != 0 and real != 0:
            period = 2 * np.pi / np.arctan(imag / real)
            return min(max(period, 8), self.p.hp_period)
            
        return self.p.hp_period
        
    def calculate_trend_quality(self):
        """
        Berechnet die Trendqualität.
        """
        if len(self.decycler_history) < self.p.smooth_period:
            return 0
            
        trend = np.array(
            self.decycler_history[-self.p.smooth_period:]
        )
        return 1 - np.std(trend) / np.mean(np.abs(trend))
        
    def next(self):
        # Preis speichern
        self.price_history.append(self.data.close[0])
        
        # Super Smoother Filter anwenden
        smoothed = self.super_smoother_filter(
            self.price_history
        )
        
        # Zyklusperiode berechnen
        cycle_period = self.calculate_cycle_period()
        
        # Decycler berechnen
        if len(self.price_history) >= 4:
            decycler = (
                smoothed +
                self.a1 * (smoothed - self.price_history[-2]) +
                self.a2 * (
                    self.price_history[-2] -
                    self.price_history[-3]
                ) +
                self.a3 * (
                    self.price_history[-3] -
                    self.price_history[-4]
                )
            )
        else:
            decycler = smoothed
            
        self.decycler_history.append(decycler)
        
        # Linien aktualisieren
        self.lines.decycler[0] = decycler
        self.lines.super_smoother[0] = smoothed
        self.lines.cycle_period[0] = cycle_period
        self.lines.trend_quality[0] = self.calculate_trend_quality()
        
        # Signal
        if len(self.decycler_history) >= 2:
            if (decycler > self.decycler_history[-2] and
                self.lines.trend_quality[0] > 0.7):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (decycler < self.decycler_history[-2] and
                  self.lines.trend_quality[0] > 0.7):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.hp_period,
            self.p.smooth_period
        )
        for hist in [self.price_history,
                    self.decycler_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'decycler': {
                'value': self.lines.decycler[0],
                'smoothed': self.lines.super_smoother[0],
                'trend': (
                    'up'
                    if len(self.decycler_history) >= 2 and
                       self.lines.decycler[0] >
                       self.decycler_history[-2]
                    else 'down'
                )
            },
            'cycles': {
                'period': self.lines.cycle_period[0],
                'quality': self.lines.trend_quality[0],
                'stability': (
                    'stable'
                    if self.lines.trend_quality[0] > 0.7
                    else 'unstable'
                )
            },
            'trend': {
                'strength': (
                    abs(
                        self.lines.decycler[0] -
                        self.lines.super_smoother[0]
                    )
                    if len(self.decycler_history) >= 1
                    else 0
                ),
                'quality': (
                    'high'
                    if self.lines.trend_quality[0] > 0.8
                    else 'medium'
                    if self.lines.trend_quality[0] > 0.5
                    else 'low'
                ),
                'reliability': self.lines.trend_quality[0]
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'confidence': (
                    self.lines.trend_quality[0] *
                    abs(self.lines.signal[0])
                )
            },
            'market_state': {
                'cycle_dominance': (
                    'low'
                    if self.lines.trend_quality[0] > 0.8
                    else 'high'
                ),
                'trend_condition': (
                    'trending'
                    if self.lines.trend_quality[0] > 0.7
                    else 'cyclic'
                ),
                'trading_quality': (
                    'optimal'
                    if self.lines.trend_quality[0] > 0.8 and
                       abs(self.lines.signal[0]) > 0
                    else 'suboptimal'
                )
            }
        }
