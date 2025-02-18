import backtrader as bt
import numpy as np
from datetime import datetime, timedelta

class MarketSentimentIndicator(bt.Indicator):
    """
    Comprehensive Market Sentiment Indicator
    
    Kombiniert mehrere Sentiment-Indikatoren zu einem ganzheitlichen Marktsentiment-Index:
    - Sentix Sentiment (simuliert)
    - AAII Bull/Bear Ratio
    - VIX-basierte Volatilität
    - Put-Call Ratio
    - Volume Flow
    
    Features:
    - Multi-Indikator Sentiment Analyse
    - Gewichtete Aggregation
    - Extremwert-Erkennung
    - Trendbasierte Signale
    - Volumen-Bestätigung
    
    Parameter:
    - sentiment_period (14): Basisperiode für Sentiment-Berechnung
    - vix_period (10): VIX Berechnungsperiode
    - smooth_period (5): Glättungsperiode
    - extreme_threshold (80): Schwelle für extreme Sentiment-Werte
    - volume_impact (0.3): Gewichtung des Volumen-Einflusses
    """
    
    lines = ('sentiment_index', 'sentix', 'aaii_ratio',
             'vix', 'put_call_ratio', 'volume_flow',
             'extreme_bullish', 'extreme_bearish',
             'trend_signal', 'composite_signal')
             
    params = (
        ('sentiment_period', 14),
        ('vix_period', 10),
        ('smooth_period', 5),
        ('extreme_threshold', 80),
        ('volume_impact', 0.3),
        ('weights', {
            'sentix': 0.2,
            'aaii': 0.2,
            'vix': 0.2,
            'pcr': 0.2,
            'volume': 0.2
        })
    )
    
    plotlines = dict(
        sentiment_index=dict(color='blue', _name='Sentiment Index'),
        sentix=dict(color='green', _name='Sentix'),
        aaii_ratio=dict(color='red', _name='AAII Ratio'),
        vix=dict(color='purple', _name='VIX'),
        put_call_ratio=dict(color='orange', _name='PCR'),
        volume_flow=dict(color='brown', _name='Volume Flow'),
        extreme_bullish=dict(_name='Extreme Bullish', color='green', marker='^'),
        extreme_bearish=dict(_name='Extreme Bearish', color='red', marker='v'),
        trend_signal=dict(_name='Trend', color='blue', marker='o'),
        composite_signal=dict(_name='Composite', color='purple', marker='s')
    )
    
    def __init__(self):
        super(MarketSentimentIndicator, self).__init__()
        
        # Glättung
        self.sentiment_ma = bt.indicators.SMA(
            self.lines.sentiment_index,
            period=self.p.smooth_period
        )
        
        # Volatilitäts-Berechnung
        self.volatility = bt.indicators.StdDev(
            self.data,
            period=self.p.vix_period
        )
        
        # Volumen-Analyse
        self.volume_sma = bt.indicators.SMA(
            self.data.volume,
            period=self.p.sentiment_period
        )
        
        # Historie für Extremwerte
        self.sentiment_history = []
        self.volume_history = []
        
    def simulate_sentix(self):
        """
        Simuliert Sentix Sentiment Daten.
        Basiert auf Preis-, Volumen- und Volatilitätsdaten.
        """
        price_change = (self.data[0] - self.data[-1]) / self.data[-1]
        vol_impact = (self.data.volume[0] / self.volume_sma[0] - 1)
        volatility = self.volatility[0]
        
        # Basis-Sentiment (-100 bis +100)
        base_sentiment = 50 * price_change / volatility if volatility != 0 else 0
        
        # Volumen-Einfluss
        volume_adj = 20 * vol_impact
        
        # Trend-Komponente
        trend = np.sum([
            1 if self.data[i] > self.data[i-1] else -1
            for i in range(-5, 1)
        ]) * 5
        
        sentiment = base_sentiment + volume_adj + trend
        return max(min(sentiment, 100), -100)
        
    def simulate_aaii_ratio(self):
        """
        Simuliert AAII Bull/Bear Ratio.
        Basiert auf Preis-Momentum und Volatilität.
        """
        momentum = (self.data[0] - self.data[-5]) / self.data[-5]
        volatility = self.volatility[0]
        
        # Basis-Ratio (0 bis 3)
        base_ratio = 1.5 + (momentum / volatility if volatility != 0 else 0)
        
        # Trend-Einfluss
        trend_factor = 1 + 0.2 * sum(
            1 if self.data[i] > self.data[i-1] else -1
            for i in range(-3, 1)
        )
        
        ratio = base_ratio * trend_factor
        return max(min(ratio, 3), 0)
        
    def calculate_vix(self):
        """
        Berechnet VIX-ähnlichen Volatilitätsindex.
        """
        # Annualisierte Volatilität
        annual_factor = np.sqrt(252)  # Handelstage pro Jahr
        return self.volatility[0] * annual_factor * 100
        
    def simulate_put_call_ratio(self):
        """
        Simuliert Put-Call Ratio basierend auf Marktbedingungen.
        """
        price = self.data[0]
        momentum = (price - self.data[-5]) / self.data[-5]
        volatility = self.volatility[0]
        
        # Basis PCR (0.5 bis 2.0)
        base_pcr = 1.0 - momentum * 2
        
        # Volatilitäts-Einfluss
        vol_factor = 1 + volatility
        
        pcr = base_pcr * vol_factor
        return max(min(pcr, 2), 0.5)
        
    def calculate_volume_flow(self):
        """
        Berechnet Volume Flow Indicator.
        """
        if self.volume_sma[0] == 0:
            return 0
            
        vol_ratio = self.data.volume[0] / self.volume_sma[0]
        price_change = (self.data[0] - self.data[-1]) / self.data[-1]
        
        return vol_ratio * price_change * 100
        
    def next(self):
        # Komponenten berechnen
        self.lines.sentix[0] = self.simulate_sentix()
        self.lines.aaii_ratio[0] = self.simulate_aaii_ratio()
        self.lines.vix[0] = self.calculate_vix()
        self.lines.put_call_ratio[0] = self.simulate_put_call_ratio()
        self.lines.volume_flow[0] = self.calculate_volume_flow()
        
        # Composite Sentiment Index berechnen
        self.lines.sentiment_index[0] = (
            self.p.weights['sentix'] * (self.lines.sentix[0] / 100) +
            self.p.weights['aaii'] * (self.lines.aaii_ratio[0] / 3) +
            self.p.weights['vix'] * (50 - self.lines.vix[0]) / 50 +
            self.p.weights['pcr'] * (1 - (self.lines.put_call_ratio[0] - 0.5) / 1.5) +
            self.p.weights['volume'] * (self.lines.volume_flow[0] / 100)
        ) * 100
        
        # Historie aktualisieren
        self.sentiment_history.append(self.lines.sentiment_index[0])
        if len(self.sentiment_history) > self.p.sentiment_period:
            self.sentiment_history.pop(0)
            
        # Signal-Generierung
        if self.lines.sentiment_index[0] > self.p.extreme_threshold:
            # Extreme bullish
            self.lines.extreme_bullish[0] = self.data.low[0]
            self.lines.extreme_bearish[0] = float('nan')
        elif self.lines.sentiment_index[0] < -self.p.extreme_threshold:
            # Extreme bearish
            self.lines.extreme_bullish[0] = float('nan')
            self.lines.extreme_bearish[0] = self.data.high[0]
        else:
            self.lines.extreme_bullish[0] = float('nan')
            self.lines.extreme_bearish[0] = float('nan')
            
        # Trend Signal
        sentiment_ma = self.sentiment_ma[0]
        if sentiment_ma is not None:
            if (self.lines.sentiment_index[0] > sentiment_ma and
                self.lines.volume_flow[0] > 0):
                self.lines.trend_signal[0] = self.data.low[0]
            elif (self.lines.sentiment_index[0] < sentiment_ma and
                  self.lines.volume_flow[0] < 0):
                self.lines.trend_signal[0] = self.data.high[0]
            else:
                self.lines.trend_signal[0] = float('nan')
                
        # Composite Signal
        vix_signal = self.lines.vix[0] > 30  # Hohe Volatilität
        pcr_signal = self.lines.put_call_ratio[0] > 1.5  # Hohe Put-Activity
        sentiment_signal = abs(self.lines.sentiment_index[0]) > 50  # Extremes Sentiment
        
        if vix_signal and pcr_signal and sentiment_signal:
            self.lines.composite_signal[0] = (
                self.data.high[0] if self.lines.sentiment_index[0] < 0
                else self.data.low[0]
            )
        else:
            self.lines.composite_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Sentiment-Analyse.
        """
        return {
            'sentiment_index': self.lines.sentiment_index[0],
            'components': {
                'sentix': self.lines.sentix[0],
                'aaii_ratio': self.lines.aaii_ratio[0],
                'vix': self.lines.vix[0],
                'put_call_ratio': self.lines.put_call_ratio[0],
                'volume_flow': self.lines.volume_flow[0]
            },
            'signals': {
                'extreme_bullish': self.lines.sentiment_index[0] > self.p.extreme_threshold,
                'extreme_bearish': self.lines.sentiment_index[0] < -self.p.extreme_threshold,
                'trend': 'bullish' if self.lines.trend_signal[0] != float('nan') else 'bearish',
                'composite': self.lines.composite_signal[0] != float('nan')
            },
            'market_state': {
                'volatility': 'high' if self.lines.vix[0] > 30 else 'normal',
                'volume': 'high' if self.lines.volume_flow[0] > 50 else 'normal',
                'sentiment': ('extreme bullish' if self.lines.sentiment_index[0] > self.p.extreme_threshold
                            else 'extreme bearish' if self.lines.sentiment_index[0] < -self.p.extreme_threshold
                            else 'neutral')
            }
        }
