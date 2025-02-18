import backtrader as bt
import numpy as np

class HeikenAshiSmoothed(bt.Indicator):
    """
    Heiken Ashi Smoothed Indicator
    
    Eine fortgeschrittene Version des Heiken Ashi mit zusätzlicher
    Glättung und Trendanalyse.
    
    Features:
    - Mehrfache Glättung der HA Werte
    - Trend-Stärke Berechnung
    - Momentum-Analyse
    - Signal-Generierung
    - Multi-Timeframe Unterstützung
    
    Parameter:
    - smooth_period (10): Glättungsperiode
    - trend_period (20): Trendperiode
    - momentum_period (14): Momentum-Periode
    - sensitivity (2.0): Sensitivität für Signale
    """
    
    lines = ('ha_open', 'ha_high', 'ha_low', 'ha_close',
             'smooth_open', 'smooth_high', 'smooth_low', 'smooth_close',
             'trend_strength', 'momentum',
             'buy_signal', 'sell_signal')
             
    params = (
        ('smooth_period', 10),
        ('trend_period', 20),
        ('momentum_period', 14),
        ('sensitivity', 2.0)
    )
    
    plotlines = dict(
        ha_open=dict(color='gray', _name='HA Open'),
        ha_high=dict(color='gray', _name='HA High'),
        ha_low=dict(color='gray', _name='HA Low'),
        ha_close=dict(color='gray', _name='HA Close'),
        smooth_open=dict(color='blue', _name='Smooth Open'),
        smooth_high=dict(color='green', _name='Smooth High'),
        smooth_low=dict(color='red', _name='Smooth Low'),
        smooth_close=dict(color='purple', _name='Smooth Close'),
        trend_strength=dict(color='brown', _name='Trend Strength'),
        momentum=dict(color='orange', _name='Momentum'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(HeikenAshiSmoothed, self).__init__()
        
        # Erste Glättung
        self.ema1 = bt.indicators.EMA(period=self.p.smooth_period)
        self.ema2 = bt.indicators.EMA(period=self.p.trend_period)
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.rsi = bt.indicators.RSI(period=14)
        
        # Historie
        self.ha_history = []
        self.trend_history = []
        
    def calculate_heiken_ashi(self):
        """
        Berechnet die Heiken Ashi Werte.
        """
        if len(self) < 2:
            self.lines.ha_open[0] = self.data.open[0]
            self.lines.ha_close[0] = self.data.close[0]
            self.lines.ha_high[0] = self.data.high[0]
            self.lines.ha_low[0] = self.data.low[0]
            return
            
        # HA Close
        self.lines.ha_close[0] = (
            self.data.open[0] +
            self.data.high[0] +
            self.data.low[0] +
            self.data.close[0]
        ) / 4
        
        # HA Open
        self.lines.ha_open[0] = (
            self.lines.ha_open[-1] +
            self.lines.ha_close[-1]
        ) / 2
        
        # HA High/Low
        self.lines.ha_high[0] = max(
            self.data.high[0],
            self.lines.ha_open[0],
            self.lines.ha_close[0]
        )
        self.lines.ha_low[0] = min(
            self.data.low[0],
            self.lines.ha_open[0],
            self.lines.ha_close[0]
        )
        
    def smooth_values(self):
        """
        Glättet die Heiken Ashi Werte.
        """
        # EMA Glättung
        self.lines.smooth_open[0] = self.ema1(self.lines.ha_open)
        self.lines.smooth_high[0] = self.ema1(self.lines.ha_high)
        self.lines.smooth_low[0] = self.ema1(self.lines.ha_low)
        self.lines.smooth_close[0] = self.ema1(self.lines.ha_close)
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self) < self.p.trend_period:
            return 0
            
        # Trend-Richtung
        direction = 1 if self.lines.smooth_close[0] > self.lines.smooth_open[0] else -1
        
        # Preisdifferenz
        price_range = self.lines.smooth_high[0] - self.lines.smooth_low[0]
        if price_range == 0:
            return 0
            
        # Candlestick-Größe
        body_size = abs(
            self.lines.smooth_close[0] -
            self.lines.smooth_open[0]
        )
        
        # Trendstärke (0-1)
        strength = (body_size / price_range) * direction
        
        return strength
        
    def calculate_momentum(self):
        """
        Berechnet den Momentum-Indikator.
        """
        if len(self) < self.p.momentum_period:
            return 0
            
        # Rate of Change
        roc = (
            (self.lines.smooth_close[0] -
             self.lines.smooth_close[-self.p.momentum_period]) /
            self.lines.smooth_close[-self.p.momentum_period]
        )
        
        # RSI Einfluss
        rsi_factor = (self.rsi[0] - 50) / 50
        
        # Kombinierter Momentum-Wert
        momentum = (roc + rsi_factor) / 2
        
        return momentum
        
    def next(self):
        # Heiken Ashi berechnen
        self.calculate_heiken_ashi()
        
        # Werte glätten
        self.smooth_values()
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Momentum
        self.lines.momentum[0] = self.calculate_momentum()
        
        # Historie aktualisieren
        self.ha_history.append({
            'open': self.lines.smooth_open[0],
            'high': self.lines.smooth_high[0],
            'low': self.lines.smooth_low[0],
            'close': self.lines.smooth_close[0]
        })
        if len(self.ha_history) > self.p.trend_period:
            self.ha_history.pop(0)
            
        self.trend_history.append(self.lines.trend_strength[0])
        if len(self.trend_history) > self.p.trend_period:
            self.trend_history.pop(0)
            
        # Signal-Generierung
        # Buy Signal
        if (self.lines.trend_strength[0] > 0 and
            self.lines.momentum[0] > 0 and
            abs(self.lines.trend_strength[0]) > self.p.sensitivity / 10):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.trend_strength[0] < 0 and
            self.lines.momentum[0] < 0 and
            abs(self.lines.trend_strength[0]) > self.p.sensitivity / 10):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'heiken_ashi': {
                'current': {
                    'open': self.lines.smooth_open[0],
                    'high': self.lines.smooth_high[0],
                    'low': self.lines.smooth_low[0],
                    'close': self.lines.smooth_close[0]
                },
                'trend': {
                    'strength': self.lines.trend_strength[0],
                    'momentum': self.lines.momentum[0],
                    'direction': ('up' if self.lines.trend_strength[0] > 0
                                else 'down'),
                    'consistency': np.std(self.trend_history)
                }
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(self.lines.trend_strength[0]),
                'momentum_aligned': (
                    self.lines.trend_strength[0] *
                    self.lines.momentum[0] > 0
                )
            },
            'analysis': {
                'volatility': self.atr[0],
                'rsi': self.rsi[0],
                'trend_quality': abs(
                    sum(self.trend_history) /
                    len(self.trend_history)
                ) if self.trend_history else 0
            }
        }
