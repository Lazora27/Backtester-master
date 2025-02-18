import backtrader as bt
import numpy as np
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import defaultdict, deque

class SentimentScore(bt.Indicator):
    """
    Sentiment Score Indicator
    
    Ein Indikator zur Analyse von Marktstimmungen
    aus verschiedenen Textquellen.
    
    Features:
    - Multi-Source Sentiment Analysis
    - Gewichtete Stimmungsaggregation
    - Sentiment-Trend-Erkennung
    - Adaptive Gewichtung
    
    Parameter:
    - sentiment_period (30): Sentimentperiode
    - source_weights (None): Quellengewichte
    - min_confidence (0.6): Minimale Konfidenz
    """
    
    lines = ('sentiment_score', 'source_impact',
             'sentiment_trend', 'confidence',
             'signal')
             
    params = (
        ('sentiment_period', 30),
        ('source_weights', None),
        ('min_confidence', 0.6)
    )
    
    plotlines = dict(
        sentiment_score=dict(color='blue', _name='Sentiment Score'),
        source_impact=dict(color='green', _name='Source Impact'),
        sentiment_trend=dict(color='red', _name='Sentiment Trend'),
        confidence=dict(color='purple', _name='Confidence'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(SentimentScore, self).__init__()
        
        # Sentiment Analyzer
        self.textblob_analyzer = TextBlob
        self.vader_analyzer = SentimentIntensityAnalyzer()
        
        # Standardgewichte falls nicht angegeben
        self.source_weights = (
            self.p.source_weights or
            {
                'news': 0.4,
                'social': 0.3,
                'analysis': 0.3
            }
        )
        
        # Sentiment Tracking
        self.sentiment_history = deque(
            maxlen=self.p.sentiment_period
        )
        self.source_history = defaultdict(
            lambda: deque(maxlen=self.p.sentiment_period)
        )
        
    def analyze_text(self, text, method='combined'):
        """
        Analysiert Text mit verschiedenen Methoden.
        """
        if not text:
            return 0, 0
            
        if method == 'textblob':
            blob = self.textblob_analyzer(text)
            score = blob.sentiment.polarity
            confidence = 1 - abs(blob.sentiment.subjectivity)
            
        elif method == 'vader':
            scores = self.vader_analyzer.polarity_scores(text)
            score = scores['compound']
            confidence = 1 - (
                scores['neu'] /
                sum(scores.values())
            )
            
        else:  # combined
            blob = self.textblob_analyzer(text)
            vader_scores = self.vader_analyzer.polarity_scores(
                text
            )
            
            # Gewichteter Durchschnitt
            score = (
                blob.sentiment.polarity +
                vader_scores['compound']
            ) / 2
            
            confidence = (
                (1 - abs(blob.sentiment.subjectivity)) +
                (1 - vader_scores['neu'] /
                 sum(vader_scores.values()))
            ) / 2
            
        return score, confidence
        
    def calculate_source_impact(self, sentiments):
        """
        Berechnet den Impact verschiedener Quellen.
        """
        impacts = {}
        for source, data in sentiments.items():
            if data:
                scores, confidences = zip(*data)
                
                # Gewichteter Score
                impact = (
                    np.mean(scores) *
                    np.mean(confidences) *
                    self.source_weights.get(source, 0.3)
                )
                impacts[source] = impact
                
        return impacts
        
    def analyze_sentiment_trend(self):
        """
        Analysiert den Sentiment-Trend.
        """
        if len(self.sentiment_history) < 2:
            return 0
            
        # Trend über Historie
        trend = np.polyfit(
            range(len(self.sentiment_history)),
            self.sentiment_history,
            1
        )[0]
        
        return trend
        
    def calculate_confidence(self, impacts):
        """
        Berechnet die Gesamtkonfidenz.
        """
        if not impacts:
            return 0
            
        # Gewichtete Konfidenz
        total_weight = sum(
            self.source_weights.get(source, 0.3)
            for source in impacts.keys()
        )
        
        if total_weight == 0:
            return 0
            
        confidence = sum(
            abs(impact) * self.source_weights.get(source, 0.3)
            for source, impact in impacts.items()
        ) / total_weight
        
        return confidence
        
    def next(self):
        # Beispiel-Sentimentdaten (in der Praxis: externe API)
        current_sources = {
            'news': [
                'Market outlook remains positive',
                'Strong earnings reported'
            ],
            'social': [
                'Bullish sentiment growing',
                'Technical indicators positive'
            ],
            'analysis': [
                'Upward trend confirmed',
                'Support levels holding'
            ]
        }
        
        # Sentiment für jede Quelle analysieren
        source_sentiments = defaultdict(list)
        for source, texts in current_sources.items():
            for text in texts:
                score, confidence = self.analyze_text(text)
                if confidence >= self.p.min_confidence:
                    source_sentiments[source].append(
                        (score, confidence)
                    )
                    
        # Impact berechnen
        impacts = self.calculate_source_impact(
            source_sentiments
        )
        
        # Gesamtscore berechnen
        if impacts:
            sentiment_score = sum(impacts.values())
            
            # Historie aktualisieren
            self.sentiment_history.append(sentiment_score)
            for source, impact in impacts.items():
                self.source_history[source].append(impact)
                
            # Trend und Konfidenz
            sentiment_trend = self.analyze_sentiment_trend()
            confidence = self.calculate_confidence(impacts)
            
            # Linien aktualisieren
            self.lines.sentiment_score[0] = sentiment_score
            self.lines.source_impact[0] = max(
                abs(impact) for impact in impacts.values()
            )
            self.lines.sentiment_trend[0] = sentiment_trend
            self.lines.confidence[0] = confidence
            
            # Trading Signal
            if confidence > self.p.min_confidence:
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
        else:
            # Standardwerte
            self.lines.sentiment_score[0] = 0
            self.lines.source_impact[0] = 0
            self.lines.sentiment_trend[0] = 0
            self.lines.confidence[0] = 0
            self.lines.signal[0] = 0
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'sentiment_metrics': {
                'score': self.lines.sentiment_score[0],
                'impact': self.lines.source_impact[0],
                'trend': self.lines.sentiment_trend[0],
                'confidence': self.lines.confidence[0]
            },
            'source_analysis': {
                source: {
                    'current_impact': (
                        list(self.source_history[source])[-1]
                        if self.source_history[source]
                        else 0
                    ),
                    'trend': (
                        'improving'
                        if (len(self.source_history[source]) > 1 and
                            self.source_history[source][-1] >
                            self.source_history[source][-2])
                        else 'deteriorating'
                        if len(self.source_history[source]) > 1
                        else 'neutral'
                    ),
                    'weight': self.source_weights.get(source, 0.3)
                }
                for source in self.source_weights.keys()
            },
            'trend_analysis': {
                'direction': (
                    'positive'
                    if self.lines.sentiment_trend[0] > 0
                    else 'negative'
                    if self.lines.sentiment_trend[0] < 0
                    else 'neutral'
                ),
                'strength': abs(self.lines.sentiment_trend[0]),
                'consistency': (
                    'consistent'
                    if len(self.sentiment_history) > 3 and
                    all(s * self.sentiment_history[-1] > 0
                        for s in list(self.sentiment_history)[-3:])
                    else 'inconsistent'
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
                    'high'
                    if self.lines.confidence[0] >
                       self.p.min_confidence
                    else 'low'
                )
            },
            'market_sentiment': {
                'overall': (
                    'bullish'
                    if self.lines.sentiment_score[0] > 0.2
                    else 'bearish'
                    if self.lines.sentiment_score[0] < -0.2
                    else 'neutral'
                ),
                'confidence': (
                    'high'
                    if self.lines.confidence[0] > 0.7
                    else 'moderate'
                    if self.lines.confidence[0] > 0.5
                    else 'low'
                ),
                'trend_quality': (
                    'strong'
                    if abs(self.lines.sentiment_trend[0]) > 0.02
                    else 'weak'
                )
            }
        }
