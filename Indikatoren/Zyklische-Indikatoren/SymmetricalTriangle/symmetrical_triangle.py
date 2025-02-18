import backtrader as bt
import numpy as np
from scipy import stats

class SymmetricalTriangle(bt.Indicator):
    """
    Symmetrical Triangle Pattern Indicator
    
    Ein fortgeschrittener Indikator zur Erkennung und Analyse
    von symmetrischen Dreiecksformationen.
    
    Features:
    - Trendlinienberechnung
    - Konvergenzanalyse
    - Ausbruchserkennung
    - Signalgenerierung
    
    Parameter:
    - min_points (5): Minimale Punktanzahl
    - lookback_period (30): Rückblickperiode
    - breakout_threshold (0.02): Ausbruchsschwelle
    """
    
    lines = ('upper_line', 'lower_line',
             'convergence', 'breakout',
             'signal')
             
    params = (
        ('min_points', 5),
        ('lookback_period', 30),
        ('breakout_threshold', 0.02)
    )
    
    plotlines = dict(
        upper_line=dict(color='blue', _name='Upper Line'),
        lower_line=dict(color='red', _name='Lower Line'),
        convergence=dict(color='green', _name='Convergence'),
        breakout=dict(color='purple', _name='Breakout'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(SymmetricalTriangle, self).__init__()
        
        # Historie
        self.high_history = []
        self.low_history = []
        self.pattern_points = []
        
    def find_peaks(self, data, is_high=True):
        """
        Findet lokale Maxima oder Minima.
        """
        if len(data) < 3:
            return []
            
        peaks = []
        for i in range(1, len(data)-1):
            if is_high:
                if (data[i] > data[i-1] and
                    data[i] > data[i+1]):
                    peaks.append((i, data[i]))
            else:
                if (data[i] < data[i-1] and
                    data[i] < data[i+1]):
                    peaks.append((i, data[i]))
                    
        return peaks
        
    def calculate_trendlines(self):
        """
        Berechnet die obere und untere Trendlinie.
        """
        if len(self.high_history) < self.p.min_points:
            return None, None
            
        # Peaks finden
        highs = self.find_peaks(self.high_history, True)
        lows = self.find_peaks(self.low_history, False)
        
        if len(highs) < 2 or len(lows) < 2:
            return None, None
            
        # Trendlinien berechnen
        high_x = [x for x, _ in highs]
        high_y = [y for _, y in highs]
        low_x = [x for x, _ in lows]
        low_y = [y for _, y in lows]
        
        # Regression für obere Linie
        upper_slope, upper_intercept, _, _, _ = stats.linregress(
            high_x,
            high_y
        )
        
        # Regression für untere Linie
        lower_slope, lower_intercept, _, _, _ = stats.linregress(
            low_x,
            low_y
        )
        
        return (
            (upper_slope, upper_intercept),
            (lower_slope, lower_intercept)
        )
        
    def calculate_convergence(self, upper, lower):
        """
        Berechnet die Konvergenz der Trendlinien.
        """
        if not upper or not lower:
            return 0
            
        upper_slope, _ = upper
        lower_slope, _ = lower
        
        # Konvergenz basierend auf Steigungsdifferenz
        return abs(upper_slope - lower_slope)
        
    def detect_breakout(self, upper, lower):
        """
        Erkennt Ausbrüche aus dem Dreieck.
        """
        if not upper or not lower:
            return 0
            
        current_price = self.data.close[0]
        upper_slope, upper_intercept = upper
        lower_slope, lower_intercept = lower
        
        # Aktuelle Trendlinienwerte
        current_upper = (
            upper_slope * (len(self.high_history)-1) +
            upper_intercept
        )
        current_lower = (
            lower_slope * (len(self.low_history)-1) +
            lower_intercept
        )
        
        # Ausbruchserkennung
        if current_price > current_upper * (
            1 + self.p.breakout_threshold
        ):
            return 1  # Aufwärtsausbruch
        elif current_price < current_lower * (
            1 - self.p.breakout_threshold
        ):
            return -1  # Abwärtsausbruch
            
        return 0
        
    def next(self):
        # Preise speichern
        self.high_history.append(self.data.high[0])
        self.low_history.append(self.data.low[0])
        
        # Trendlinien berechnen
        trendlines = self.calculate_trendlines()
        
        if trendlines:
            upper, lower = trendlines
            
            # Aktuelle Linienwerte
            current_upper = (
                upper[0] * (len(self.high_history)-1) +
                upper[1]
            )
            current_lower = (
                lower[0] * (len(self.low_history)-1) +
                lower[1]
            )
            
            # Konvergenz
            convergence = self.calculate_convergence(
                upper,
                lower
            )
            
            # Ausbruch
            breakout = self.detect_breakout(
                upper,
                lower
            )
            
            # Linien aktualisieren
            self.lines.upper_line[0] = current_upper
            self.lines.lower_line[0] = current_lower
            self.lines.convergence[0] = convergence
            self.lines.breakout[0] = breakout
            
            # Signal
            if breakout != 0 and convergence > 0:
                self.lines.signal[0] = breakout
            else:
                self.lines.signal[0] = 0
        else:
            # Standardwerte
            self.lines.upper_line[0] = self.data.high[0]
            self.lines.lower_line[0] = self.data.low[0]
            self.lines.convergence[0] = 0
            self.lines.breakout[0] = 0
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = self.p.lookback_period
        for hist in [self.high_history,
                    self.low_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'pattern': {
                'upper_line': self.lines.upper_line[0],
                'lower_line': self.lines.lower_line[0],
                'convergence': self.lines.convergence[0],
                'breakout': self.lines.breakout[0]
            },
            'formation': {
                'quality': (
                    'high'
                    if self.lines.convergence[0] > 0.01
                    else 'low'
                ),
                'stage': (
                    'mature'
                    if len(self.high_history) >=
                       self.p.min_points
                    else 'developing'
                ),
                'symmetry': (
                    'good'
                    if abs(
                        self.lines.upper_line[0] -
                        self.data.close[0]
                    ) / self.data.close[0] -
                    abs(
                        self.lines.lower_line[0] -
                        self.data.close[0]
                    ) / self.data.close[0] < 0.1
                    else 'poor'
                )
            },
            'breakout_analysis': {
                'status': (
                    'up' if self.lines.breakout[0] > 0
                    else 'down' if self.lines.breakout[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.breakout[0]),
                'confirmation': (
                    'confirmed'
                    if abs(self.lines.breakout[0]) > 0 and
                       self.lines.convergence[0] > 0.01
                    else 'unconfirmed'
                )
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'reliability': (
                    self.lines.convergence[0] *
                    abs(self.lines.breakout[0])
                )
            },
            'market_conditions': {
                'pattern_quality': (
                    'optimal'
                    if (self.lines.convergence[0] > 0.01 and
                        len(self.high_history) >=
                        self.p.min_points)
                    else 'suboptimal'
                ),
                'volatility': (
                    'high'
                    if abs(
                        self.lines.upper_line[0] -
                        self.lines.lower_line[0]
                    ) / self.data.close[0] > 0.05
                    else 'low'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.convergence[0] > 0.008 and
                        abs(self.lines.breakout[0]) > 0)
                    else 'unfavorable'
                )
            }
        }
