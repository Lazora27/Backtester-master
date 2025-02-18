import backtrader as bt
import numpy as np

class AdaptiveRSI(bt.Indicator):
    """
    Adaptive RSI Indicator
    
    Ein adaptiver RSI-Indikator, der seine Parameter basierend auf
    Marktbedingungen dynamisch anpasst.
    
    Features:
    - Adaptive Periodenberechnung
    - Dynamische Schwellenwerte
    - Volatilitätsanpassung
    - Trend-Erkennung
    - Multi-Timeframe Analyse
    
    Parameter:
    - base_period (14): Basis RSI Periode
    - vol_period (20): Volatilitäts-Berechnungsperiode
    - trend_period (50): Trend-Erkennungsperiode
    - sensitivity (2.0): Anpassungssensitivität
    """
    
    lines = ('adaptive_rsi', 'upper_band', 'lower_band',
             'trend_strength', 'volatility',
             'buy_signal', 'sell_signal')
             
    params = (
        ('base_period', 14),
        ('vol_period', 20),
        ('trend_period', 50),
        ('sensitivity', 2.0)
    )
    
    plotlines = dict(
        adaptive_rsi=dict(color='blue', _name='Adaptive RSI'),
        upper_band=dict(color='gray', _name='Upper Band'),
        lower_band=dict(color='gray', _name='Lower Band'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volatility=dict(color='red', _name='Volatility'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(AdaptiveRSI, self).__init__()
        
        # Basis RSI
        self.rsi = bt.indicators.RSI(
            period=self.p.base_period,
            movav=bt.indicators.ExponentialMovingAverage
        )
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.vol_period)
        self.ema = bt.indicators.EMA(period=self.p.trend_period)
        
        # Historie
        self.period_history = []
        self.volatility_history = []
        self.rsi_history = []
        
    def calculate_adaptive_period(self):
        """
        Berechnet die adaptive Periode basierend auf Marktbedingungen.
        """
        if len(self) < self.p.vol_period:
            return self.p.base_period
            
        # Volatilitätsbasierte Anpassung
        volatility = self.atr[0] / self.data[0] if self.data[0] != 0 else 0
        vol_factor = np.exp(-volatility * self.p.sensitivity)
        
        # Trendbasierte Anpassung
        trend_strength = abs(
            self.data[0] - self.ema[0]
        ) / self.atr[0] if self.atr[0] != 0 else 0
        trend_factor = np.exp(-trend_strength * self.p.sensitivity)
        
        # Kombinierte Anpassung
        adaptive_period = int(
            self.p.base_period * (
                1 + vol_factor * trend_factor
            )
        )
        
        return max(2, min(adaptive_period, self.p.base_period * 2))
        
    def calculate_adaptive_bands(self):
        """
        Berechnet adaptive Überkauft/Überverkauft Bänder.
        """
        if len(self.rsi_history) < self.p.vol_period:
            return 80, 20
            
        # Volatilitätsbasierte Bandbreite
        volatility = np.std(self.rsi_history) / np.mean(self.rsi_history)
        band_width = 30 * (1 + volatility * self.p.sensitivity)
        
        # Zentrum basierend auf Trend
        if len(self) > 1:
            trend = (self.data[0] - self.data[-1]) / self.data[-1] if self.data[-1] != 0 else 0
            center = 50 + (trend * 10)
        else:
            center = 50
            
        upper = min(100, center + band_width)
        lower = max(0, center - band_width)
        
        return upper, lower
        
    def calculate_trend_strength(self):
        """
        Berechnet die aktuelle Trendstärke.
        """
        if len(self) < self.p.trend_period:
            return 0
            
        # Preisbasierte Trendstärke
        price_trend = (
            self.data[0] - self.data[-self.p.trend_period]
        ) / self.data[-self.p.trend_period] if self.data[-self.p.trend_period] != 0 else 0
        
        # RSI-basierte Trendstärke
        rsi_trend = (
            self.rsi[0] - np.mean(self.rsi_history)
        ) / np.std(self.rsi_history) if len(self.rsi_history) > 0 else 0
        
        # Kombinierte Trendstärke (-1 bis 1)
        strength = np.tanh((price_trend + rsi_trend) / 2)
        
        return strength
        
    def next(self):
        # Adaptive Periode berechnen
        adaptive_period = self.calculate_adaptive_period()
        
        # Historie aktualisieren
        self.period_history.append(adaptive_period)
        self.volatility_history.append(self.atr[0])
        self.rsi_history.append(self.rsi[0])
        
        if len(self.period_history) > self.p.trend_period:
            self.period_history.pop(0)
            self.volatility_history.pop(0)
            self.rsi_history.pop(0)
            
        # Adaptive RSI berechnen
        if len(self) >= adaptive_period:
            gains = []
            losses = []
            for i in range(adaptive_period):
                change = self.data[-i] - self.data[-i-1]
                if change > 0:
                    gains.append(change)
                    losses.append(0)
                else:
                    gains.append(0)
                    losses.append(-change)
                    
            avg_gain = np.mean(gains)
            avg_loss = np.mean(losses)
            
            if avg_loss == 0:
                self.lines.adaptive_rsi[0] = 100
            else:
                rs = avg_gain / avg_loss
                self.lines.adaptive_rsi[0] = 100 - (100 / (1 + rs))
        else:
            self.lines.adaptive_rsi[0] = 50
            
        # Bänder und Trendstärke
        upper, lower = self.calculate_adaptive_bands()
        self.lines.upper_band[0] = upper
        self.lines.lower_band[0] = lower
        
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        self.lines.volatility[0] = (
            self.atr[0] / self.data[0] if self.data[0] != 0 else 0
        )
        
        # Signal-Generierung
        # Buy Signal
        if (self.lines.adaptive_rsi[0] < lower and
            self.lines.trend_strength[0] > 0 and
            self.lines.adaptive_rsi[0] > self.lines.adaptive_rsi[-1]):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.adaptive_rsi[0] > upper and
            self.lines.trend_strength[0] < 0 and
            self.lines.adaptive_rsi[0] < self.lines.adaptive_rsi[-1]):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'rsi': {
                'value': self.lines.adaptive_rsi[0],
                'period': self.period_history[-1] if self.period_history else self.p.base_period,
                'bands': {
                    'upper': self.lines.upper_band[0],
                    'lower': self.lines.lower_band[0]
                },
                'condition': (
                    'overbought' if self.lines.adaptive_rsi[0] > self.lines.upper_band[0]
                    else 'oversold' if self.lines.adaptive_rsi[0] < self.lines.lower_band[0]
                    else 'neutral'
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': ('up' if self.lines.trend_strength[0] > 0
                            else 'down'),
                'quality': abs(self.lines.trend_strength[0])
            },
            'volatility': {
                'current': self.lines.volatility[0],
                'average': np.mean(self.volatility_history) if self.volatility_history else 0,
                'stability': np.std(self.volatility_history) if self.volatility_history else 0
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(
                    self.lines.adaptive_rsi[0] - 50
                ) / 50,
                'reliability': (
                    abs(self.lines.trend_strength[0]) *
                    (1 - self.lines.volatility[0])
                )
            }
        }
