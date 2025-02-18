import backtrader as bt
import numpy as np

class PercentagePriceOscillator(bt.Indicator):
    """
    Percentage Price Oscillator (PPO)
    
    Ein Momentum-Indikator, der die prozentuale Differenz zwischen
    zwei exponentiellen gleitenden Durchschnitten berechnet.
    
    Features:
    - Prozentuale Preisoszillation
    - Signallinie und Histogramm
    - Divergenz-Erkennung
    - Trendstärke-Analyse
    - Signal-Validierung
    
    Parameter:
    - fast_period (12): Schnelle EMA Periode
    - slow_period (26): Langsame EMA Periode
    - signal_period (9): Signal EMA Periode
    - upper_threshold (2.0): Obere Schwelle
    - lower_threshold (-2.0): Untere Schwelle
    """
    
    lines = ('ppo', 'signal', 'histogram',
             'divergence', 'trend_strength',
             'upper', 'lower',
             'buy_signal', 'sell_signal')
             
    params = (
        ('fast_period', 12),
        ('slow_period', 26),
        ('signal_period', 9),
        ('upper_threshold', 2.0),
        ('lower_threshold', -2.0)
    )
    
    plotlines = dict(
        ppo=dict(color='blue', _name='PPO'),
        signal=dict(color='red', _name='Signal'),
        histogram=dict(color='green', _name='Histogram'),
        divergence=dict(color='purple', _name='Divergence'),
        trend_strength=dict(color='orange', _name='Trend Strength'),
        upper=dict(color='gray', _name='Upper'),
        lower=dict(color='gray', _name='Lower'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(PercentagePriceOscillator, self).__init__()
        
        # EMAs
        self.fast_ma = bt.indicators.EMA(period=self.p.fast_period)
        self.slow_ma = bt.indicators.EMA(period=self.p.slow_period)
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Historie
        self.ppo_history = []
        self.histogram_history = []
        self.price_history = []
        
    def calculate_ppo(self):
        """
        Berechnet den PPO-Wert.
        """
        if self.slow_ma[0] == 0:
            return 0
            
        return (
            (self.fast_ma[0] - self.slow_ma[0]) /
            self.slow_ma[0] * 100
        )
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und PPO.
        """
        if len(self.price_history) < self.p.signal_period or len(self.ppo_history) < self.p.signal_period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.signal_period:])
        price_low = min(self.price_history[-self.p.signal_period:])
        
        # PPO-Hochs/-Tiefs
        ppo_high = max(self.ppo_history[-self.p.signal_period:])
        ppo_low = min(self.ppo_history[-self.p.signal_period:])
        
        # Bullische Divergenz
        if price_low < price_high and ppo_low > ppo_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and ppo_low < ppo_high:
            return -1
            
        return 0
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.histogram_history) < 2:
            return 0
            
        # Histogramm-Momentum
        momentum = self.histogram_history[-1] - self.histogram_history[-2]
        
        # Relative Stärke
        strength = abs(momentum)
        if self.data[0] != 0:
            strength = strength / self.data[0]
            
        return min(1.0, strength)
        
    def next(self):
        # PPO berechnen
        self.lines.ppo[0] = self.calculate_ppo()
        
        # Signal-Linie
        self.lines.signal[0] = bt.indicators.EMA(
            self.lines.ppo, period=self.p.signal_period
        )[0]
        
        # Histogramm
        self.lines.histogram[0] = (
            self.lines.ppo[0] - self.lines.signal[0]
        )
        
        # Historie aktualisieren
        self.ppo_history.append(self.lines.ppo[0])
        self.histogram_history.append(self.lines.histogram[0])
        self.price_history.append(self.data[0])
        
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Bänder
        self.lines.upper[0] = self.p.upper_threshold
        self.lines.lower[0] = self.p.lower_threshold
        
        # Historie begrenzen
        max_period = max(self.p.slow_period, self.p.signal_period)
        for hist in [self.ppo_history, self.histogram_history, self.price_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.ppo[0] < self.p.lower_threshold and
            self.lines.histogram[0] > 0 and
            self.lines.trend_strength[0] > 0.3 and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.ppo[0] > self.p.upper_threshold and
            self.lines.histogram[0] < 0 and
            self.lines.trend_strength[0] > 0.3 and
            self.lines.divergence[0] <= 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'oscillator': {
                'ppo': self.lines.ppo[0],
                'signal': self.lines.signal[0],
                'histogram': self.lines.histogram[0],
                'trend_strength': self.lines.trend_strength[0]
            },
            'trend': {
                'direction': np.sign(self.lines.histogram[0]),
                'strength': abs(self.lines.histogram[0]),
                'momentum': (
                    self.lines.histogram[0] -
                    self.histogram_history[-2]
                    if len(self.histogram_history) > 1
                    else 0
                )
            },
            'divergence': {
                'type': (
                    'bullish' if self.lines.divergence[0] > 0
                    else 'bearish' if self.lines.divergence[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.divergence[0])
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    self.lines.trend_strength[0] *
                    (1 + abs(self.lines.divergence[0])) *
                    abs(self.lines.histogram[0])
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'histogram_stability': (
                    np.std(self.histogram_history)
                    if len(self.histogram_history) > 1
                    else 0
                ),
                'trend_consistency': (
                    np.mean([
                        1 if np.sign(h) == np.sign(self.lines.histogram[0])
                        else 0
                        for h in self.histogram_history[-5:]
                    ]) if len(self.histogram_history) >= 5
                    else 0
                )
            }
        }
