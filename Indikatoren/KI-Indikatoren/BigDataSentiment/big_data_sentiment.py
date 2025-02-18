import backtrader as bt
import numpy as np
from textblob import TextBlob
from collections import defaultdict
import re

class BigDataSentiment(bt.Indicator):
    """
    Big Data Sentiment Analysis Indicator
    
    Ein KI-basierter Indikator zur Analyse von
    Marktstimmungen aus verschiedenen Datenquellen.
    
    Features:
    - Sentiment-Analyse
    - Stimmungstrends
    - Quellengewichtung
    - Signalgenerierung
    
    Parameter:
    - sentiment_period (20): Sentimentperiode
    - source_weight (0.5): Quellengewichtung
    - confidence_threshold (0.7): Konfidenzschwelle
    """
    
    lines = ('sentiment_score', 'sentiment_trend',
             'source_impact', 'sentiment_quality',
             'signal')
             
    params = (
        ('sentiment_period', 20),
        ('source_weight', 0.5),
        ('confidence_threshold', 0.7)
    )
    
    plotlines = dict(
        sentiment_score=dict(color='blue', _name='Sentiment Score'),
        sentiment_trend=dict(color='red', _name='Sentiment Trend'),
        source_impact=dict(color='green', _name='Source Impact'),
        sentiment_quality=dict(color='purple', _name='Sentiment Quality'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(BigDataSentiment, self).__init__()
        
        # Sentiment Tracking
        self.sentiment_history = []
        self.source_history = []
        self.impact_history = []
        self.quality_history = []
        
        # Sentiment Quellen
        self.sources = defaultdict(list)
        
    def analyze_text_sentiment(self, text):
        """
        Analysiert das Sentiment eines Textes.
        """
        if not text:
            return 0, 0
            
        # TextBlob für Sentiment-Analyse
        blob = TextBlob(text)
        
        # Sentiment und Subjektivität
        sentiment = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        return sentiment, subjectivity
        
    def calculate_source_impact(self, sentiments):
        """
        Berechnet den Impact verschiedener Quellen.
        """
        if not sentiments:
            return 0
            
        # Gewichteter Impact
        impacts = []
        for source, values in sentiments.items():
            if values:
                avg_sentiment = np.mean([v[0] for v in values])
                avg_subjectivity = np.mean([v[1] for v in values])
                
                impact = (
                    avg_sentiment *
                    (1 - avg_subjectivity) *
                    self.p.source_weight
                )
                impacts.append(impact)
                
        if not impacts:
            return 0
            
        return np.mean(impacts)
        
    def analyze_sentiment_trend(self):
        """
        Analysiert den Sentiment-Trend.
        """
        if len(self.sentiment_history) < 2:
            return 0
            
        # Trend über Historie
        recent_sentiment = self.sentiment_history[
            -self.p.sentiment_period:
        ]
        
        if len(recent_sentiment) < 2:
            return 0
            
        # Trendberechnung
        trend = np.polyfit(
            range(len(recent_sentiment)),
            recent_sentiment,
            1
        )[0]
        
        return trend
        
    def calculate_sentiment_quality(self, impact):
        """
        Berechnet die Qualität des Sentiments.
        """
        if not self.quality_history:
            return impact
            
        # Qualität basierend auf Historie
        historical_quality = np.mean(
            self.quality_history[-self.p.sentiment_period:]
        )
        
        quality = (impact + historical_quality) / 2
        self.quality_history.append(quality)
        
        return quality
        
    def next(self):
        # Beispiel-Sentimentdaten (in der Praxis: externe API)
        current_sources = {
            'news': [
                ('Positive market outlook', 0.8),
                ('Economic growth continues', 0.6)
            ],
            'social': [
                ('Bullish sentiment rising', 0.7),
                ('Market momentum strong', 0.5)
            ]
        }
        
        # Sentiment für jede Quelle analysieren
        source_sentiments = {}
        for source, texts in current_sources.items():
            sentiments = []
            for text, confidence in texts:
                sentiment, subjectivity = self.analyze_text_sentiment(
                    text
                )
                sentiments.append((
                    sentiment * confidence,
                    subjectivity
                ))
            source_sentiments[source] = sentiments
            
        # Impact berechnen
        source_impact = self.calculate_source_impact(
            source_sentiments
        )
        
        # Gesamtscore berechnen
        sentiment_score = np.mean([
            np.mean([s[0] for s in sentiments])
            for sentiments in source_sentiments.values()
        ])
        
        self.sentiment_history.append(sentiment_score)
        self.impact_history.append(source_impact)
        
        # Trend und Qualität
        sentiment_trend = self.analyze_sentiment_trend()
        sentiment_quality = self.calculate_sentiment_quality(
            source_impact
        )
        
        # Linien aktualisieren
        self.lines.sentiment_score[0] = sentiment_score
        self.lines.sentiment_trend[0] = sentiment_trend
        self.lines.source_impact[0] = source_impact
        self.lines.sentiment_quality[0] = sentiment_quality
        
        # Signal
        if sentiment_quality > self.p.confidence_threshold:
            if (sentiment_score > 0.2 and
                sentiment_trend > 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (sentiment_score < -0.2 and
                  sentiment_trend < 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_length = max(
            self.p.sentiment_period,
            len(self.data)
        )
        for hist in [self.sentiment_history,
                    self.impact_history,
                    self.quality_history]:
            if len(hist) > max_length:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'sentiment_metrics': {
                'score': self.lines.sentiment_score[0],
                'trend': self.lines.sentiment_trend[0],
                'impact': self.lines.source_impact[0],
                'quality': self.lines.sentiment_quality[0]
            },
            'sentiment_analysis': {
                'state': (
                    'bullish'
                    if self.lines.sentiment_score[0] > 0.2
                    else 'bearish'
                    if self.lines.sentiment_score[0] < -0.2
                    else 'neutral'
                ),
                'strength': abs(self.lines.sentiment_score[0]),
                'consistency': (
                    'consistent'
                    if len(self.sentiment_history) > 1 and
                    all(s * self.sentiment_history[-1] > 0
                        for s in self.sentiment_history[-3:])
                    else 'inconsistent'
                )
            },
            'trend_analysis': {
                'direction': (
                    'improving'
                    if self.lines.sentiment_trend[0] > 0
                    else 'deteriorating'
                    if self.lines.sentiment_trend[0] < 0
                    else 'stable'
                ),
                'strength': abs(self.lines.sentiment_trend[0]),
                'reliability': (
                    'reliable'
                    if self.lines.sentiment_quality[0] >
                       self.p.confidence_threshold
                    else 'unreliable'
                )
            },
            'impact_analysis': {
                'level': (
                    'high'
                    if self.lines.source_impact[0] > 0.7
                    else 'moderate'
                    if self.lines.source_impact[0] > 0.4
                    else 'low'
                ),
                'trend': (
                    'increasing'
                    if len(self.impact_history) > 1 and
                    self.impact_history[-1] >
                    self.impact_history[-2]
                    else 'decreasing'
                ),
                'quality': (
                    'high'
                    if self.lines.sentiment_quality[0] > 0.7
                    else 'moderate'
                    if self.lines.sentiment_quality[0] > 0.4
                    else 'low'
                )
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'reliability': (
                    self.lines.sentiment_quality[0] *
                    abs(self.lines.sentiment_score[0])
                )
            },
            'market_conditions': {
                'sentiment_quality': (
                    'high'
                    if self.lines.sentiment_quality[0] > 0.7
                    else 'moderate'
                    if self.lines.sentiment_quality[0] > 0.4
                    else 'low'
                ),
                'trend_clarity': (
                    'clear'
                    if abs(self.lines.sentiment_trend[0]) > 0.2
                    else 'unclear'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.sentiment_quality[0] >
                        self.p.confidence_threshold and
                        abs(self.lines.sentiment_score[0]) > 0.2)
                    else 'unfavorable'
                )
            }
        }
