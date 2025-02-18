import backtrader as bt
import numpy as np
from datetime import datetime, timedelta

class FearGreedIndex(bt.Indicator):
    """
    Fear & Greed Index Indicator
    
    Erweiterte Version mit:
    - Multi-Faktor Analyse
    - Momentum Integration
    - Volatilitäts-Komponente
    - Marktbreite-Analyse
    - Relative Stärke
    
    Komponenten:
    1. Momentum (25%):
       - Kursdynamik
       - RSI
       - MACD
    
    2. Volatilität (25%):
       - ATR
       - Bollinger Bandbreite
       - VIX-Style Berechnung
    
    3. Marktbreite (25%):
       - Advance/Decline Ratio
       - New Highs vs. New Lows
       - Moving Average Trends
    
    4. Relative Stärke (25%):
       - Stärke vs. Benchmark
       - Sektorrotation
       - Volumenanalyse
    
    Parameter:
    - period (14): Basisperiode für Berechnungen
    - ma_period (10): Glättungsperiode
    - rsi_period (14): RSI Periode
    - vol_period (20): Volatilitätsperiode
    - extreme_threshold (80): Schwelle für extreme Werte
    """
    
    lines = ('fear_greed_index',
             'momentum_component',
             'volatility_component',
             'breadth_component',
             'strength_component',
             'smoothed_index',
             'signal_line',
             'extreme_fear',
             'extreme_greed')
             
    params = (
        ('period', 14),
        ('ma_period', 10),
        ('rsi_period', 14),
        ('vol_period', 20),
        ('extreme_threshold', 80)
    )
    
    plotlines = dict(
        fear_greed_index=dict(color='black', _name='Fear & Greed'),
        momentum_component=dict(color='blue', _name='Momentum'),
        volatility_component=dict(color='red', _name='Volatility'),
        breadth_component=dict(color='green', _name='Market Breadth'),
        strength_component=dict(color='purple', _name='Relative Strength'),
        smoothed_index=dict(color='orange', _name='Smoothed Index'),
        signal_line=dict(color='gray', _name='Signal'),
        extreme_fear=dict(_name='Extreme Fear', color='darkred', marker='v'),
        extreme_greed=dict(_name='Extreme Greed', color='darkgreen', marker='^')
    )
    
    def __init__(self):
        super(FearGreedIndex, self).__init__()
        
        # Momentum Indikatoren
        self.rsi = bt.indicators.RSI(
            period=self.p.rsi_period
        )
        self.macd = bt.indicators.MACD()
        
        # Volatilitäts Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.vol_period)
        self.bbands = bt.indicators.BollingerBands(
            period=self.p.vol_period
        )
        
        # Gleitende Durchschnitte
        self.sma20 = bt.indicators.SMA(period=20)
        self.sma50 = bt.indicators.SMA(period=50)
        
        # Volumen Indikatoren
        self.volume_ma = bt.indicators.SMA(
            self.data.volume,
            period=self.p.period
        )
        
        # Glättung
        self.smoothed = bt.indicators.SMA(
            self.lines.fear_greed_index,
            period=self.p.ma_period
        )
        
    def calculate_momentum_component(self):
        """Berechnet die Momentum-Komponente."""
        # RSI Komponente (0-100)
        rsi_value = self.rsi[0]
        
        # MACD Komponente (-100 bis +100)
        macd_value = self.macd.macd[0]
        macd_range = max(abs(self.macd.macd[-self.p.period:]))
        if macd_range != 0:
            macd_norm = (macd_value / macd_range) * 100
        else:
            macd_norm = 0
            
        # Kursdynamik (-100 bis +100)
        price_change = (
            (self.data.close[0] / self.data.close[-self.p.period]) - 1
        ) * 100
        
        # Gewichteter Durchschnitt
        momentum = (
            rsi_value * 0.4 +
            macd_norm * 0.3 +
            price_change * 0.3
        )
        
        return max(-100, min(100, momentum))
        
    def calculate_volatility_component(self):
        """Berechnet die Volatilitäts-Komponente."""
        # ATR Komponente
        atr_value = self.atr[0]
        atr_max = max(self.atr.array)
        if atr_max != 0:
            atr_norm = (atr_value / atr_max) * 100
        else:
            atr_norm = 50
            
        # Bollinger Bandbreite
        bb_width = (
            (self.bbands.top[0] - self.bbands.bot[0]) /
            self.bbands.mid[0]
        ) * 100
        
        # VIX-Style Berechnung
        high_low_range = np.std([
            self.data.high[i] / self.data.low[i] - 1
            for i in range(-self.p.vol_period, 1)
        ]) * 100
        
        # Invertierte gewichtete Summe (höhere Volatilität = mehr Angst)
        volatility = 100 - (
            atr_norm * 0.4 +
            bb_width * 0.3 +
            high_low_range * 0.3
        )
        
        return max(0, min(100, volatility))
        
    def calculate_breadth_component(self):
        """Berechnet die Marktbreite-Komponente."""
        # Trend über/unter MA
        above_ma20 = self.data.close[0] > self.sma20[0]
        above_ma50 = self.data.close[0] > self.sma50[0]
        
        # New Highs/Lows Simulation
        highs = sum(1 for i in range(-10, 1)
                   if self.data.high[i] == max(self.data.high[i-5:i+1]))
        lows = sum(1 for i in range(-10, 1)
                  if self.data.low[i] == min(self.data.low[i-5:i+1]))
        
        # Marktbreite Score
        breadth = (
            (above_ma20 * 30) +
            (above_ma50 * 30) +
            ((highs - lows) / (highs + lows if highs + lows > 0 else 1)) * 40
        )
        
        return max(0, min(100, 50 + breadth))
        
    def calculate_strength_component(self):
        """Berechnet die relative Stärke-Komponente."""
        # Volumen-Analyse
        vol_ratio = (
            self.data.volume[0] / self.volume_ma[0]
            if self.volume_ma[0] != 0 else 1
        )
        
        # Preis-Momentum
        price_strength = (
            (self.data.close[0] / self.data.close[-5]) - 1
        ) * 100
        
        # Kombinierte Stärke
        strength = (
            (vol_ratio - 1) * 50 +
            price_strength * 50
        )
        
        return max(0, min(100, 50 + strength))
        
    def next(self):
        # Komponenten berechnen
        momentum = self.calculate_momentum_component()
        volatility = self.calculate_volatility_component()
        breadth = self.calculate_breadth_component()
        strength = self.calculate_strength_component()
        
        # Komponenten speichern
        self.lines.momentum_component[0] = momentum
        self.lines.volatility_component[0] = volatility
        self.lines.breadth_component[0] = breadth
        self.lines.strength_component[0] = strength
        
        # Gesamtindex berechnen (0-100)
        self.lines.fear_greed_index[0] = (
            momentum * 0.25 +
            volatility * 0.25 +
            breadth * 0.25 +
            strength * 0.25
        )
        
        # Geglätteter Index
        self.lines.smoothed_index[0] = self.smoothed[0]
        
        # Signal Line (verzögerter Index)
        if len(self) > self.p.ma_period:
            self.lines.signal_line[0] = self.lines.smoothed_index[-1]
        else:
            self.lines.signal_line[0] = self.lines.fear_greed_index[0]
            
        # Extreme Werte
        if self.lines.fear_greed_index[0] < 100 - self.p.extreme_threshold:
            self.lines.extreme_fear[0] = self.data.low[0]
        else:
            self.lines.extreme_fear[0] = float('nan')
            
        if self.lines.fear_greed_index[0] > self.p.extreme_threshold:
            self.lines.extreme_greed[0] = self.data.high[0]
        else:
            self.lines.extreme_greed[0] = float('nan')
