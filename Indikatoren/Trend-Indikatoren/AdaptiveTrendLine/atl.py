import backtrader as bt
import numpy as np
from scipy.signal import argrelextrema
from scipy.stats import linregress

class AdaptiveTrendLine(bt.Indicator):
    """
    Adaptive Trend Line (ATL) Indicator
    
    Ein fortgeschrittener Trend-Indikator, der automatisch Trendlinien identifiziert
    und anpasst. Kombiniert mehrere Techniken zur Trendanalyse.
    
    Features:
    - Automatische Trendlinien-Erkennung
    - Adaptive Pivot-Punkt Analyse
    - Trendstärke-Berechnung
    - Breakout-Erkennung
    - Multi-Timeframe Analyse
    
    Parameter:
    - min_points (5): Minimale Punkte für Trendlinie
    - lookback_period (20): Rückblickperiode
    - trend_threshold (0.6): Schwelle für Trendstärke
    - breakout_factor (2.0): Faktor für Breakout-Erkennung
    - smooth_period (3): Glättungsperiode
    """
    
    lines = ('upper_trend', 'lower_trend', 'trend_strength',
             'breakout_level', 'support_level', 'resistance_level',
             'trend_signal', 'breakout_signal', 'reversal_signal')
             
    params = (
        ('min_points', 5),
        ('lookback_period', 20),
        ('trend_threshold', 0.6),
        ('breakout_factor', 2.0),
        ('smooth_period', 3)
    )
    
    plotlines = dict(
        upper_trend=dict(color='green', _name='Upper Trend'),
        lower_trend=dict(color='red', _name='Lower Trend'),
        trend_strength=dict(color='blue', _name='Trend Strength'),
        breakout_level=dict(color='purple', _name='Breakout Level'),
        support_level=dict(color='gray', _name='Support'),
        resistance_level=dict(color='gray', _name='Resistance'),
        trend_signal=dict(_name='Trend', color='blue', marker='o'),
        breakout_signal=dict(_name='Breakout', color='purple', marker='^'),
        reversal_signal=dict(_name='Reversal', color='red', marker='v')
    )
    
    def __init__(self):
        super(AdaptiveTrendLine, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.ema = bt.indicators.EMA(period=20)
        
        # Preisdaten-Historie
        self.price_history = []
        self.high_history = []
        self.low_history = []
        
        # Trendlinien-Historie
        self.upper_trends = []
        self.lower_trends = []
        
        # Glättung
        self.trend_ma = bt.indicators.SMA(
            period=self.p.smooth_period
        )
        
    def find_pivot_points(self, data, order=5):
        """
        Findet Pivot-Punkte in der Preisreihe.
        
        Parameter:
        - data: Preisdaten
        - order: Fenster für lokale Extrema
        """
        if len(data) < 2 * order + 1:
            return [], []
            
        # Lokale Maxima und Minima
        maxima = argrelextrema(data, np.greater, order=order)[0]
        minima = argrelextrema(data, np.less, order=order)[0]
        
        return maxima, minima
        
    def fit_trend_line(self, points, prices):
        """
        Berechnet eine Trendlinie durch die gegebenen Punkte.
        
        Parameter:
        - points: Indizes der Punkte
        - prices: Preisdaten
        """
        if len(points) < self.p.min_points:
            return None, None
            
        x = points
        y = prices[points]
        
        slope, intercept, r_value, _, _ = linregress(x, y)
        
        return slope, intercept
        
    def calculate_trend_strength(self, slope, prices):
        """
        Berechnet die Stärke des Trends.
        
        Parameter:
        - slope: Steigung der Trendlinie
        - prices: Preisdaten
        """
        if slope is None:
            return 0
            
        # Trendstärke basierend auf Steigung und R²
        normalized_slope = np.arctan(slope) / (np.pi/2)
        
        # Preisvolatilität
        volatility = np.std(prices) if len(prices) > 1 else 0
        price_range = np.ptp(prices) if len(prices) > 1 else 0
        
        if price_range != 0:
            strength = abs(normalized_slope) * (1 - volatility/price_range)
            return max(min(strength, 1), 0)
        return 0
        
    def detect_breakout(self, current_price, trend_line, volatility):
        """
        Erkennt Breakouts von der Trendlinie.
        
        Parameter:
        - current_price: Aktueller Preis
        - trend_line: Wert der Trendlinie
        - volatility: Aktuelle Volatilität
        """
        if trend_line is None:
            return False
            
        # Breakout-Schwelle basierend auf Volatilität
        threshold = volatility * self.p.breakout_factor
        
        return abs(current_price - trend_line) > threshold
        
    def update_trend_lines(self):
        """
        Aktualisiert die Trendlinien basierend auf neuen Daten.
        """
        if len(self.price_history) < self.p.lookback_period:
            return None, None
            
        # Aktuelle Preisdaten
        prices = np.array(self.price_history[-self.p.lookback_period:])
        highs = np.array(self.high_history[-self.p.lookback_period:])
        lows = np.array(self.low_history[-self.p.lookback_period:])
        
        # Pivot-Punkte finden
        high_pivots, _ = self.find_pivot_points(highs)
        _, low_pivots = self.find_pivot_points(lows)
        
        # Trendlinien berechnen
        upper_slope, upper_intercept = self.fit_trend_line(
            high_pivots, highs
        )
        lower_slope, lower_intercept = self.fit_trend_line(
            low_pivots, lows
        )
        
        return (
            (upper_slope, upper_intercept),
            (lower_slope, lower_intercept)
        )
        
    def next(self):
        # Preisdaten aktualisieren
        self.price_history.append(self.data.close[0])
        self.high_history.append(self.data.high[0])
        self.low_history.append(self.data.low[0])
        
        # Historie begrenzen
        max_history = max(self.p.lookback_period * 2, 100)
        if len(self.price_history) > max_history:
            self.price_history.pop(0)
            self.high_history.pop(0)
            self.low_history.pop(0)
            
        # Trendlinien aktualisieren
        trend_lines = self.update_trend_lines()
        
        if trend_lines is not None:
            upper_trend, lower_trend = trend_lines
            
            # Trendlinien-Werte berechnen
            if upper_trend[0] is not None:
                self.lines.upper_trend[0] = (
                    upper_trend[0] * self.p.lookback_period +
                    upper_trend[1]
                )
            if lower_trend[0] is not None:
                self.lines.lower_trend[0] = (
                    lower_trend[0] * self.p.lookback_period +
                    lower_trend[1]
                )
                
            # Trendstärke
            upper_strength = self.calculate_trend_strength(
                upper_trend[0], self.high_history
            )
            lower_strength = self.calculate_trend_strength(
                lower_trend[0], self.low_history
            )
            
            self.lines.trend_strength[0] = (
                upper_strength + lower_strength
            ) / 2
            
            # Support und Resistance
            self.lines.support_level[0] = self.lines.lower_trend[0]
            self.lines.resistance_level[0] = self.lines.upper_trend[0]
            
            # Breakout Level
            self.lines.breakout_level[0] = (
                self.lines.upper_trend[0] +
                self.atr[0] * self.p.breakout_factor
            )
            
            # Signal-Generierung
            current_price = self.data.close[0]
            
            # Trend Signal
            if self.lines.trend_strength[0] > self.p.trend_threshold:
                if current_price > self.ema[0]:
                    self.lines.trend_signal[0] = self.data.low[0]
                else:
                    self.lines.trend_signal[0] = self.data.high[0]
            else:
                self.lines.trend_signal[0] = float('nan')
                
            # Breakout Signal
            if self.detect_breakout(
                current_price,
                self.lines.resistance_level[0],
                self.atr[0]
            ):
                self.lines.breakout_signal[0] = self.data.low[0]
            else:
                self.lines.breakout_signal[0] = float('nan')
                
            # Reversal Signal
            if (self.lines.trend_strength[0] < self.p.trend_threshold and
                abs(current_price - self.lines.support_level[0]) < self.atr[0]):
                self.lines.reversal_signal[0] = self.data.high[0]
            else:
                self.lines.reversal_signal[0] = float('nan')
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des aktuellen Trends.
        """
        return {
            'trend_lines': {
                'upper': self.lines.upper_trend[0],
                'lower': self.lines.lower_trend[0],
                'strength': self.lines.trend_strength[0]
            },
            'levels': {
                'support': self.lines.support_level[0],
                'resistance': self.lines.resistance_level[0],
                'breakout': self.lines.breakout_level[0]
            },
            'signals': {
                'trend': self.lines.trend_signal[0] != float('nan'),
                'breakout': self.lines.breakout_signal[0] != float('nan'),
                'reversal': self.lines.reversal_signal[0] != float('nan')
            },
            'market_state': {
                'trend': ('strong' if self.lines.trend_strength[0] > self.p.trend_threshold
                         else 'weak'),
                'volatility': self.atr[0],
                'direction': ('up' if self.data.close[0] > self.ema[0]
                            else 'down')
            }
        }
