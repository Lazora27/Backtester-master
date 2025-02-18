import backtrader as bt
import numpy as np

class ChandeKrollStop(bt.Indicator):
    """
    Chande Kroll Stop Indicator
    
    Ein fortgeschrittener Trend-Following Indikator, der adaptive Stops
    basierend auf Volatilität und Trend-Stärke berechnet.
    
    Features:
    - Adaptive Stop Levels
    - Volatilitäts-Anpassung
    - Trend-Stärke Integration
    - Multi-Timeframe Analyse
    - Signal Generation
    
    Parameter:
    - p_short (10): Kurze Periode für ATR
    - p_long (20): Lange Periode für ATR
    - k_short (1.5): Kurzer Multiplikator
    - k_long (2.0): Langer Multiplikator
    - ma_period (10): Glättungsperiode
    """
    
    lines = ('long_stop', 'short_stop', 'trend_strength',
             'stop_band', 'volatility_index',
             'trend_signal', 'reversal_signal')
             
    params = (
        ('p_short', 10),
        ('p_long', 20),
        ('k_short', 1.5),
        ('k_long', 2.0),
        ('ma_period', 10)
    )
    
    plotlines = dict(
        long_stop=dict(color='green', _name='Long Stop'),
        short_stop=dict(color='red', _name='Short Stop'),
        trend_strength=dict(color='blue', _name='Trend Strength'),
        stop_band=dict(color='gray', _name='Stop Band'),
        volatility_index=dict(color='purple', _name='Volatility'),
        trend_signal=dict(_name='Trend', color='blue', marker='o'),
        reversal_signal=dict(_name='Reversal', color='red', marker='v')
    )
    
    def __init__(self):
        super(ChandeKrollStop, self).__init__()
        
        # ATR Berechnung
        self.atr_short = bt.indicators.ATR(period=self.p.p_short)
        self.atr_long = bt.indicators.ATR(period=self.p.p_long)
        
        # Gleitende Durchschnitte
        self.ema = bt.indicators.EMA(period=self.p.ma_period)
        
        # Highest/Lowest
        self.highest = bt.indicators.Highest(self.data.high,
                                           period=self.p.p_long)
        self.lowest = bt.indicators.Lowest(self.data.low,
                                         period=self.p.p_long)
        
        # Historie für Trend-Analyse
        self.trend_history = []
        self.stop_history = []
        
    def calculate_stops(self):
        """
        Berechnet die Long und Short Stops.
        """
        # Basis Stop Levels
        long_stop = (self.highest[-1] -
                    self.atr_long[0] * self.p.k_long)
        short_stop = (self.lowest[-1] +
                     self.atr_long[0] * self.p.k_long)
        
        # Fein-Adjustierung mit kurzem ATR
        long_stop -= self.atr_short[0] * self.p.k_short
        short_stop += self.atr_short[0] * self.p.k_short
        
        return long_stop, short_stop
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.trend_history) < 2:
            return 0
            
        # Trend Direction
        current_trend = (1 if self.data.close[0] > self.ema[0]
                        else -1)
        
        # Trend Consistency
        trend_consistency = sum(1 for x in self.trend_history[-5:]
                              if x == current_trend) / 5
        
        # Volatility Impact
        volatility_ratio = (self.atr_short[0] /
                          self.atr_long[0]
                          if self.atr_long[0] != 0
                          else 1)
        
        # Combined Strength
        strength = trend_consistency * (1 / volatility_ratio)
        
        return max(min(strength, 1), 0)
        
    def calculate_volatility_index(self):
        """
        Berechnet einen Volatilitäts-Index.
        """
        if self.atr_long[0] != 0:
            return (self.atr_short[0] / self.atr_long[0] - 1) * 100
        return 0
        
    def next(self):
        # Stops berechnen
        long_stop, short_stop = self.calculate_stops()
        
        # Stop Levels setzen
        self.lines.long_stop[0] = long_stop
        self.lines.short_stop[0] = short_stop
        
        # Stop Band
        self.lines.stop_band[0] = short_stop - long_stop
        
        # Trend Direction
        current_trend = (1 if self.data.close[0] > self.ema[0]
                        else -1)
        self.trend_history.append(current_trend)
        
        # Historie begrenzen
        if len(self.trend_history) > self.p.p_long:
            self.trend_history.pop(0)
            
        # Trend Strength
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volatility Index
        self.lines.volatility_index[0] = self.calculate_volatility_index()
        
        # Signal Generation
        current_price = self.data.close[0]
        prev_price = self.data.close[-1]
        
        # Trend Signal
        if (current_price > self.lines.short_stop[0] and
            self.lines.trend_strength[0] > 0.6):
            self.lines.trend_signal[0] = self.data.low[0]
        elif (current_price < self.lines.long_stop[0] and
              self.lines.trend_strength[0] > 0.6):
            self.lines.trend_signal[0] = self.data.high[0]
        else:
            self.lines.trend_signal[0] = float('nan')
            
        # Reversal Signal
        if (prev_price > self.lines.short_stop[-1] and
            current_price < self.lines.short_stop[0]):
            self.lines.reversal_signal[0] = self.data.high[0]
        elif (prev_price < self.lines.long_stop[-1] and
              current_price > self.lines.long_stop[0]):
            self.lines.reversal_signal[0] = self.data.low[0]
        else:
            self.lines.reversal_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'stops': {
                'long': self.lines.long_stop[0],
                'short': self.lines.short_stop[0],
                'band_width': self.lines.stop_band[0]
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': ('up' if self.data.close[0] > self.ema[0]
                            else 'down'),
                'volatility': self.lines.volatility_index[0]
            },
            'signals': {
                'trend': self.lines.trend_signal[0] != float('nan'),
                'reversal': self.lines.reversal_signal[0] != float('nan')
            },
            'risk_metrics': {
                'short_volatility': self.atr_short[0],
                'long_volatility': self.atr_long[0],
                'volatility_ratio': (self.atr_short[0] / self.atr_long[0]
                                   if self.atr_long[0] != 0 else 1)
            }
        }
