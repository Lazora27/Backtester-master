import backtrader as bt
import numpy as np

class ElderImpulseSystem(bt.Indicator):
    """
    Elder Impulse System
    
    Ein Momentum-Indikator, der MACD und EMA kombiniert, um
    Marktstärke und Trendbewegungen zu identifizieren.
    
    Features:
    - MACD-EMA Kombination
    - Impulsstärke-Berechnung
    - Trendrichtungs-Analyse
    - Signalstärke-Bewertung
    - Multi-Timeframe Analyse
    
    Parameter:
    - ema_period (13): EMA Periode
    - macd_fast (12): MACD schnelle Periode
    - macd_slow (26): MACD langsame Periode
    - macd_signal (9): MACD Signal Periode
    - impulse_threshold (0.0): Impulsschwelle
    """
    
    lines = ('impulse', 'trend', 'strength',
             'ema_slope', 'macd_slope',
             'buy_signal', 'sell_signal')
             
    params = (
        ('ema_period', 13),
        ('macd_fast', 12),
        ('macd_slow', 26),
        ('macd_signal', 9),
        ('impulse_threshold', 0.0)
    )
    
    plotlines = dict(
        impulse=dict(color='blue', _name='Impulse'),
        trend=dict(color='green', _name='Trend'),
        strength=dict(color='red', _name='Strength'),
        ema_slope=dict(color='gray', _name='EMA Slope'),
        macd_slope=dict(color='orange', _name='MACD Slope'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(ElderImpulseSystem, self).__init__()
        
        # Basis-Indikatoren
        self.ema = bt.indicators.EMA(period=self.p.ema_period)
        self.macd = bt.indicators.MACD(
            period_me1=self.p.macd_fast,
            period_me2=self.p.macd_slow,
            period_signal=self.p.macd_signal
        )
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        
        # Historie
        self.impulse_history = []
        self.trend_history = []
        self.strength_history = []
        
    def calculate_slope(self, data, period=5):
        """
        Berechnet die Steigung einer Datenserie.
        """
        if len(data) < period:
            return 0
            
        y = data[-period:]
        x = list(range(period))
        
        # Lineare Regression
        n = period
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(xi * yi for xi, yi in zip(x, y))
        sum_xx = sum(xi * xi for xi in x)
        
        # Steigung berechnen
        if (n * sum_xx - sum_x * sum_x) == 0:
            return 0
            
        slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
        return slope
        
    def calculate_impulse(self):
        """
        Berechnet den Impuls basierend auf EMA und MACD.
        """
        # EMA Steigung
        ema_slope = self.calculate_slope(
            self.ema.get(size=5)
        )
        self.lines.ema_slope[0] = ema_slope
        
        # MACD Steigung
        macd_slope = self.calculate_slope(
            self.macd.macd.get(size=5)
        )
        self.lines.macd_slope[0] = macd_slope
        
        # Impuls-Klassifikation
        if ema_slope > 0 and macd_slope > 0:
            return 1  # Grün (Bullish)
        elif ema_slope < 0 and macd_slope < 0:
            return -1  # Rot (Bearish)
        else:
            return 0  # Blau (Neutral)
            
    def calculate_strength(self):
        """
        Berechnet die Stärke des Impulses.
        """
        ema_strength = abs(self.lines.ema_slope[0])
        macd_strength = abs(self.lines.macd_slope[0])
        
        # Normalisierung
        if self.data[0] != 0:
            strength = (ema_strength + macd_strength) / self.data[0]
        else:
            strength = 0
            
        return min(1.0, strength)
        
    def next(self):
        # Impuls berechnen
        self.lines.impulse[0] = self.calculate_impulse()
        
        # Trend bestimmen
        self.lines.trend[0] = np.sign(self.lines.ema_slope[0])
        
        # Stärke berechnen
        self.lines.strength[0] = self.calculate_strength()
        
        # Historie aktualisieren
        self.impulse_history.append(self.lines.impulse[0])
        self.trend_history.append(self.lines.trend[0])
        self.strength_history.append(self.lines.strength[0])
        
        if len(self.impulse_history) > self.p.ema_period:
            self.impulse_history.pop(0)
            self.trend_history.pop(0)
            self.strength_history.pop(0)
            
        # Signal-Generierung
        # Buy Signal
        if (self.lines.impulse[0] > 0 and
            self.lines.strength[0] > self.p.impulse_threshold and
            self.lines.trend[0] > 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.impulse[0] < 0 and
            self.lines.strength[0] > self.p.impulse_threshold and
            self.lines.trend[0] < 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'impulse': {
                'current': self.lines.impulse[0],
                'strength': self.lines.strength[0],
                'trend': self.lines.trend[0],
                'slopes': {
                    'ema': self.lines.ema_slope[0],
                    'macd': self.lines.macd_slope[0]
                }
            },
            'classification': {
                'type': (
                    'bullish' if self.lines.impulse[0] > 0
                    else 'bearish' if self.lines.impulse[0] < 0
                    else 'neutral'
                ),
                'strength': (
                    'strong' if self.lines.strength[0] > 0.7
                    else 'moderate' if self.lines.strength[0] > 0.3
                    else 'weak'
                ),
                'trend_quality': (
                    'high' if abs(self.lines.trend[0]) > 0.7
                    else 'medium' if abs(self.lines.trend[0]) > 0.3
                    else 'low'
                )
            },
            'momentum': {
                'direction': np.sign(
                    self.lines.ema_slope[0] + self.lines.macd_slope[0]
                ),
                'acceleration': (
                    self.lines.strength[0] - self.strength_history[-2]
                    if len(self.strength_history) > 1
                    else 0
                ),
                'consistency': np.std(self.impulse_history) if self.impulse_history else 0
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.strength[0],
                'reliability': (
                    self.lines.strength[0] *
                    (1 - abs(np.std(self.impulse_history) if self.impulse_history else 0))
                )
            },
            'risk': {
                'volatility': self.atr[0] / self.data[0] if self.data[0] != 0 else 0,
                'trend_stability': np.std(self.trend_history) if self.trend_history else 0,
                'impulse_stability': np.std(self.impulse_history) if self.impulse_history else 0
            }
        }
