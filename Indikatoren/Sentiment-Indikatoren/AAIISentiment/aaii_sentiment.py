import backtrader as bt
import numpy as np
from datetime import datetime, timedelta

class AAIISentiment(bt.Indicator):
    """
    AAII Bull/Bear Ratio Indicator
    
    Simuliert den AAII Sentiment Survey basierend auf Marktdaten.
    Der originale AAII Sentiment Survey misst wöchentlich die
    Stimmung der privaten Investoren (Bullish, Bearish, Neutral).
    
    Features:
    - Bull/Bear Ratio
    - Sentiment Extrema
    - Konträre Signale
    - Trendbestätigung
    
    Parameter:
    - period (20): Berechnungsperiode
    - ma_period (8): Glättungsperiode
    - extreme_threshold (2.0): Schwelle für Extreme
    """
    
    lines = ('bull_ratio', 'bear_ratio', 'neutral_ratio',
             'bull_bear_ratio', 'bull_bear_ma',
             'bullish_signal', 'bearish_signal',
             'extreme_bullish', 'extreme_bearish')
             
    params = (
        ('period', 20),
        ('ma_period', 8),
        ('extreme_threshold', 2.0)
    )
    
    plotlines = dict(
        bull_ratio=dict(color='green', _name='Bulls %'),
        bear_ratio=dict(color='red', _name='Bears %'),
        neutral_ratio=dict(color='gray', _name='Neutral %'),
        bull_bear_ratio=dict(color='blue', _name='Bull/Bear Ratio'),
        bull_bear_ma=dict(color='orange', _name='Ratio MA'),
        bullish_signal=dict(_name='Bullish', color='green', marker='^'),
        bearish_signal=dict(_name='Bearish', color='red', marker='v'),
        extreme_bullish=dict(_name='Extreme Bull', color='darkgreen'),
        extreme_bearish=dict(_name='Extreme Bear', color='darkred')
    )
    
    def __init__(self):
        super(AAIISentiment, self).__init__()
        
        # Trend Indikatoren
        self.sma20 = bt.indicators.SMA(period=20)
        self.sma50 = bt.indicators.SMA(period=50)
        
        # Momentum
        self.rsi = bt.indicators.RSI(period=14)
        
        # Volatilität
        self.atr = bt.indicators.ATR(period=14)
        
        # Gleitender Durchschnitt
        self.ma = bt.indicators.SMA(period=self.p.ma_period)
        
        # Historische Mittelwerte (basierend auf AAII Daten)
        self.historical_bull_avg = 38.0
        self.historical_bear_avg = 30.0
        self.historical_neutral_avg = 32.0
        
    def calculate_sentiment_ratios(self):
        """
        Berechnet die Sentiment Ratios basierend auf technischen Indikatoren.
        """
        # Trend-Komponente
        trend = 1 if self.sma20[0] > self.sma50[0] else -1
        
        # Momentum-Komponente
        rsi = self.rsi[0]
        momentum = (rsi - 50) / 50  # -1 bis +1
        
        # Volatilitäts-Komponente
        norm_atr = self.atr[0] / self.data.close[0]
        volatility = 1 - min(norm_atr * 10, 1)  # Invertiert, 0 bis 1
        
        # Preisänderung
        price_change = (self.data.close[0] / self.data.close[-5] - 1) * 100
        
        # Basis-Sentiment berechnen
        base_bull = self.historical_bull_avg
        base_bear = self.historical_bear_avg
        base_neutral = self.historical_neutral_avg
        
        # Sentiment-Anpassungen
        if trend > 0:
            bull_adj = 10 * momentum * volatility
            bear_adj = -5 * momentum * volatility
        else:
            bull_adj = -5 * momentum * volatility
            bear_adj = 10 * momentum * volatility
            
        # Finale Ratios (mit Grenzen)
        bull_ratio = max(0, min(100, base_bull + bull_adj +
                              price_change * 2))
        bear_ratio = max(0, min(100, base_bear + bear_adj -
                              price_change * 2))
        neutral_ratio = max(0, min(100, 100 - bull_ratio - bear_ratio))
        
        return bull_ratio, bear_ratio, neutral_ratio
        
    def calculate_bull_bear_ratio(self, bull_ratio, bear_ratio):
        """Berechnet das Bull/Bear Ratio."""
        if bear_ratio != 0:
            return bull_ratio / bear_ratio
        return 1.0
        
    def next(self):
        # Sentiment Ratios berechnen
        bull, bear, neutral = self.calculate_sentiment_ratios()
        
        self.lines.bull_ratio[0] = bull
        self.lines.bear_ratio[0] = bear
        self.lines.neutral_ratio[0] = neutral
        
        # Bull/Bear Ratio
        ratio = self.calculate_bull_bear_ratio(bull, bear)
        self.lines.bull_bear_ratio[0] = ratio
        
        # Gleitender Durchschnitt
        self.lines.bull_bear_ma[0] = self.ma(self.lines.bull_bear_ratio)[0]
        
        # Signale generieren
        current_ratio = self.lines.bull_bear_ratio[0]
        ratio_ma = self.lines.bull_bear_ma[0]
        
        # Extreme Levels
        if current_ratio > self.p.extreme_threshold:
            self.lines.extreme_bullish[0] = current_ratio
            self.lines.extreme_bearish[0] = float('nan')
        elif current_ratio < 1/self.p.extreme_threshold:
            self.lines.extreme_bearish[0] = current_ratio
            self.lines.extreme_bullish[0] = float('nan')
        else:
            self.lines.extreme_bullish[0] = float('nan')
            self.lines.extreme_bearish[0] = float('nan')
            
        # Konträre Signale
        if (current_ratio < ratio_ma and
            self.lines.extreme_bullish[-1] is not float('nan')):
            # Bearish Signal nach extremem Bullish Sentiment
            self.lines.bearish_signal[0] = self.data.high[0]
        else:
            self.lines.bearish_signal[0] = float('nan')
            
        if (current_ratio > ratio_ma and
            self.lines.extreme_bearish[-1] is not float('nan')):
            # Bullish Signal nach extremem Bearish Sentiment
            self.lines.bullish_signal[0] = self.data.low[0]
        else:
            self.lines.bullish_signal[0] = float('nan')
