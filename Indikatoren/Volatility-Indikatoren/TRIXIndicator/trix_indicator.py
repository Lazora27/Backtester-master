import backtrader as bt
import numpy as np

class TRIXIndicator(bt.Indicator):
    """
    TRIX Indicator
    
    Ein Volatilitätsindikator, der dreifach geglättete exponentielle
    Durchschnitte verwendet, um Trends und Volatilität zu analysieren.
    
    Features:
    - Dreifache EMA-Glättung
    - Trendstärkeberechnung
    - Volatilitätsnormalisierung
    - Signalgenerierung
    
    Parameter:
    - period (15): Analysezeitraum
    - signal_period (9): Signallinienperiode
    - smooth_period (5): Zusätzliche Glättungsperiode
    """
    
    lines = ('trix', 'signal',
             'trend_strength', 'volatility_ratio',
             'buy_sell_signal')
             
    params = (
        ('period', 15),
        ('signal_period', 9),
        ('smooth_period', 5)
    )
    
    plotlines = dict(
        trix=dict(color='blue', _name='TRIX'),
        signal=dict(color='red', _name='Signal'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volatility_ratio=dict(color='purple', _name='Volatility Ratio'),
        buy_sell_signal=dict(_name='Trade Signal',
                            color='black', marker='o')
    )
    
    def __init__(self):
        super(TRIXIndicator, self).__init__()
        
        # Historie
        self.ema1_history = []
        self.ema2_history = []
        self.ema3_history = []
        self.trix_history = []
        
    def calculate_ema(self, price, period, history):
        """
        Berechnet den exponentiellen gleitenden Durchschnitt.
        """
        alpha = 2.0 / (period + 1)
        
        if not history:
            return price
            
        return (
            alpha * price +
            (1 - alpha) * history[-1]
        )
        
    def calculate_trix(self):
        """
        Berechnet den TRIX-Wert.
        """
        if len(self.ema3_history) < 2:
            return 0
            
        return (
            (self.ema3_history[-1] -
             self.ema3_history[-2]) /
            self.ema3_history[-2] * 100
            if self.ema3_history[-2] != 0
            else 0
        )
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.trix_history) < 2:
            return 0
            
        return (
            self.trix_history[-1] -
            self.trix_history[-2]
        )
        
    def calculate_volatility_ratio(self):
        """
        Berechnet das Volatilitätsverhältnis.
        """
        if len(self.trix_history) < self.p.period:
            return 1.0
            
        current_vol = np.std(self.trix_history[-5:])
        historical_vol = np.std(
            self.trix_history[-self.p.period:]
        )
        
        return (
            current_vol / historical_vol
            if historical_vol != 0 else 1.0
        )
        
    def next(self):
        # Erste EMA
        ema1 = self.calculate_ema(
            self.data.close[0],
            self.p.period,
            self.ema1_history
        )
        self.ema1_history.append(ema1)
        
        # Zweite EMA
        ema2 = self.calculate_ema(
            ema1,
            self.p.period,
            self.ema2_history
        )
        self.ema2_history.append(ema2)
        
        # Dritte EMA
        ema3 = self.calculate_ema(
            ema2,
            self.p.period,
            self.ema3_history
        )
        self.ema3_history.append(ema3)
        
        # TRIX berechnen
        self.lines.trix[0] = self.calculate_trix()
        self.trix_history.append(self.lines.trix[0])
        
        # Signallinie
        if len(self.trix_history) >= self.p.signal_period:
            self.lines.signal[0] = np.mean(
                self.trix_history[-self.p.signal_period:]
            )
        else:
            self.lines.signal[0] = self.lines.trix[0]
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volatilitätsverhältnis
        self.lines.volatility_ratio[0] = self.calculate_volatility_ratio()
        
        # Handelssignal
        if (self.lines.trix[0] > self.lines.signal[0] and
            self.lines.trend_strength[0] > 0):
            self.lines.buy_sell_signal[0] = 1  # Kaufsignal
        elif (self.lines.trix[0] < self.lines.signal[0] and
              self.lines.trend_strength[0] < 0):
            self.lines.buy_sell_signal[0] = -1  # Verkaufssignal
        else:
            self.lines.buy_sell_signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.signal_period,
            self.p.smooth_period
        )
        for hist in [self.ema1_history, self.ema2_history,
                    self.ema3_history, self.trix_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'trix': {
                'value': self.lines.trix[0],
                'signal': self.lines.signal[0],
                'trend': (
                    'up' if self.lines.trix[0] > 0
                    else 'down'
                ),
                'divergence': (
                    self.lines.trix[0] -
                    self.lines.signal[0]
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': (
                    'up' if self.lines.trend_strength[0] > 0
                    else 'down'
                ),
                'quality': (
                    abs(self.lines.trend_strength[0])
                    if abs(self.lines.trend_strength[0]) <= 1
                    else 1
                )
            },
            'volatility': {
                'ratio': self.lines.volatility_ratio[0],
                'state': (
                    'increasing'
                    if self.lines.volatility_ratio[0] > 1
                    else 'decreasing'
                ),
                'relative_level': (
                    'high'
                    if self.lines.volatility_ratio[0] > 1.5
                    else 'low'
                    if self.lines.volatility_ratio[0] < 0.5
                    else 'normal'
                )
            },
            'signals': {
                'current': (
                    'buy'
                    if self.lines.buy_sell_signal[0] > 0
                    else 'sell'
                    if self.lines.buy_sell_signal[0] < 0
                    else 'none'
                ),
                'strength': abs(
                    self.lines.buy_sell_signal[0]
                ),
                'reliability': (
                    abs(self.lines.trend_strength[0]) *
                    abs(
                        self.lines.trix[0] -
                        self.lines.signal[0]
                    )
                )
            },
            'risk': {
                'trix_risk': (
                    abs(self.lines.trix[0]) / 100
                    if abs(self.lines.trix[0]) <= 100
                    else 1
                ),
                'trend_risk': (
                    1 - abs(self.lines.trend_strength[0])
                    if abs(self.lines.trend_strength[0]) <= 1
                    else 0
                ),
                'volatility_risk': (
                    self.lines.volatility_ratio[0]
                    if self.lines.volatility_ratio[0] > 1
                    else 1 / self.lines.volatility_ratio[0]
                    if self.lines.volatility_ratio[0] > 0
                    else 1
                )
            }
        }
