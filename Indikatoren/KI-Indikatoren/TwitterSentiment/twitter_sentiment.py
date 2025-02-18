import backtrader as bt
import numpy as np
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import defaultdict, deque

class TwitterSentiment(bt.Indicator):
    """
    Twitter Sentiment Trading Indicator
    
    Ein spezialisierter Indikator zur Analyse von
    Twitter-Sentiment für Trading-Entscheidungen.
    
    Features:
    - Twitter-Sentiment-Analyse
    - Hashtag-Tracking
    - Influencer-Gewichtung
    - Trend-Erkennung
    
    Parameter:
    - sentiment_period (30): Sentimentperiode
    - influence_threshold (1000): Follower-Schwelle
    - min_confidence (0.6): Minimale Konfidenz
    """
    
    lines = ('sentiment_score', 'tweet_impact',
             'trend_strength', 'market_mood',
             'signal')
             
    params = (
        ('sentiment_period', 30),
        ('influence_threshold', 1000),
        ('min_confidence', 0.6)
    )
    
    plotlines = dict(
        sentiment_score=dict(color='blue', _name='Sentiment Score'),
        tweet_impact=dict(color='green', _name='Tweet Impact'),
        trend_strength=dict(color='red', _name='Trend Strength'),
        market_mood=dict(color='purple', _name='Market Mood'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(TwitterSentiment, self).__init__()
        
        # Sentiment Analyzer
        self.textblob_analyzer = TextBlob
        self.vader_analyzer = SentimentIntensityAnalyzer()
        
        # Sentiment Tracking
        self.sentiment_history = deque(
            maxlen=self.p.sentiment_period
        )
        self.impact_history = deque(
            maxlen=self.p.sentiment_period
        )
        
        # Hashtag Tracking
        self.hashtag_sentiment = defaultdict(list)
        self.influencer_impact = defaultdict(float)
        
    def analyze_tweet(self, tweet_data):
        """
        Analysiert einen Tweet.
        """
        text = tweet_data.get('text', '')
        followers = tweet_data.get('followers', 0)
        hashtags = tweet_data.get('hashtags', [])
        
        if not text:
            return 0, 0, []
            
        # Sentiment mit TextBlob
        blob = self.textblob_analyzer(text)
        textblob_score = blob.sentiment.polarity
        textblob_conf = 1 - abs(blob.sentiment.subjectivity)
        
        # Sentiment mit VADER
        vader_scores = self.vader_analyzer.polarity_scores(text)
        vader_score = vader_scores['compound']
        vader_conf = 1 - (
            vader_scores['neu'] /
            sum(vader_scores.values())
        )
        
        # Kombiniertes Sentiment
        sentiment = (textblob_score + vader_score) / 2
        confidence = (textblob_conf + vader_conf) / 2
        
        # Influencer Impact
        impact = min(
            followers / self.p.influence_threshold,
            3.0
        ) if followers > 0 else 0.1
        
        return sentiment, confidence, impact, hashtags
        
    def track_hashtags(self, hashtags, sentiment, impact):
        """
        Verfolgt Hashtag-Sentiment.
        """
        for tag in hashtags:
            self.hashtag_sentiment[tag].append(
                (sentiment, impact)
            )
            
            # Historie begrenzen
            if len(self.hashtag_sentiment[tag]) > self.p.sentiment_period:
                self.hashtag_sentiment[tag].pop(0)
                
    def calculate_trend_strength(self):
        """
        Berechnet die Stärke des Sentiment-Trends.
        """
        if len(self.sentiment_history) < 2:
            return 0
            
        # Trend über Historie
        recent_sentiment = list(self.sentiment_history)
        
        if len(recent_sentiment) < 2:
            return 0
            
        # Trendberechnung
        trend = np.polyfit(
            range(len(recent_sentiment)),
            recent_sentiment,
            1
        )[0]
        
        return trend
        
    def analyze_market_mood(self):
        """
        Analysiert die Marktstimmung.
        """
        if not self.sentiment_history:
            return 0
            
        # Gewichtete Stimmung
        weighted_sentiment = np.average(
            self.sentiment_history,
            weights=self.impact_history
        ) if self.impact_history else 0
        
        # Trend-Einfluss
        trend_strength = self.calculate_trend_strength()
        
        return (weighted_sentiment + trend_strength) / 2
        
    def next(self):
        # Beispiel-Tweets (in der Praxis: Twitter API)
        current_tweets = [
            {
                'text': 'Bullish on $MARKET! Strong support levels',
                'followers': 5000,
                'hashtags': ['trading', 'bullish']
            },
            {
                'text': 'Technical analysis shows upward trend',
                'followers': 2000,
                'hashtags': ['technicals', 'analysis']
            },
            {
                'text': 'Market sentiment improving',
                'followers': 3000,
                'hashtags': ['market', 'sentiment']
            }
        ]
        
        # Tweet-Analyse
        sentiments = []
        impacts = []
        all_hashtags = []
        
        for tweet in current_tweets:
            sentiment, confidence, impact, hashtags = self.analyze_tweet(
                tweet
            )
            
            if confidence >= self.p.min_confidence:
                sentiments.append(sentiment)
                impacts.append(impact)
                all_hashtags.extend(hashtags)
                
                # Hashtags tracken
                self.track_hashtags(
                    hashtags,
                    sentiment,
                    impact
                )
                
        if sentiments:
            # Gewichtetes Sentiment
            avg_sentiment = np.average(
                sentiments,
                weights=impacts
            )
            avg_impact = np.mean(impacts)
            
            # Historie aktualisieren
            self.sentiment_history.append(avg_sentiment)
            self.impact_history.append(avg_impact)
            
            # Trend und Stimmung
            trend_strength = self.calculate_trend_strength()
            market_mood = self.analyze_market_mood()
            
            # Linien aktualisieren
            self.lines.sentiment_score[0] = avg_sentiment
            self.lines.tweet_impact[0] = avg_impact
            self.lines.trend_strength[0] = trend_strength
            self.lines.market_mood[0] = market_mood
            
            # Trading Signal
            if avg_impact > 1:  # Signifikanter Impact
                if (avg_sentiment > 0.2 and
                    trend_strength > 0):
                    self.lines.signal[0] = 1  # Kaufsignal
                elif (avg_sentiment < -0.2 and
                      trend_strength < 0):
                    self.lines.signal[0] = -1  # Verkaufssignal
                else:
                    self.lines.signal[0] = 0
            else:
                self.lines.signal[0] = 0
        else:
            # Standardwerte
            self.lines.sentiment_score[0] = 0
            self.lines.tweet_impact[0] = 0
            self.lines.trend_strength[0] = 0
            self.lines.market_mood[0] = 0
            self.lines.signal[0] = 0
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'sentiment_metrics': {
                'score': self.lines.sentiment_score[0],
                'impact': self.lines.tweet_impact[0],
                'trend': self.lines.trend_strength[0],
                'mood': self.lines.market_mood[0]
            },
            'hashtag_analysis': {
                tag: {
                    'sentiment': np.mean([
                        s[0] for s in sentiments
                    ]) if sentiments else 0,
                    'impact': np.mean([
                        s[1] for s in sentiments
                    ]) if sentiments else 0,
                    'count': len(sentiments)
                }
                for tag, sentiments in
                self.hashtag_sentiment.items()
            },
            'trend_analysis': {
                'direction': (
                    'bullish'
                    if self.lines.trend_strength[0] > 0.02
                    else 'bearish'
                    if self.lines.trend_strength[0] < -0.02
                    else 'neutral'
                ),
                'strength': abs(self.lines.trend_strength[0]),
                'momentum': (
                    'increasing'
                    if len(self.sentiment_history) > 1 and
                    self.sentiment_history[-1] >
                    self.sentiment_history[-2]
                    else 'decreasing'
                )
            },
            'market_mood_analysis': {
                'current': (
                    'positive'
                    if self.lines.market_mood[0] > 0.2
                    else 'negative'
                    if self.lines.market_mood[0] < -0.2
                    else 'neutral'
                ),
                'strength': abs(self.lines.market_mood[0]),
                'reliability': (
                    'high'
                    if self.lines.tweet_impact[0] > 1.5
                    else 'moderate'
                    if self.lines.tweet_impact[0] > 1
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
                'confidence': (
                    self.lines.tweet_impact[0] *
                    abs(self.lines.sentiment_score[0])
                )
            },
            'social_metrics': {
                'sentiment_quality': (
                    'reliable'
                    if self.lines.tweet_impact[0] > 1
                    else 'unreliable'
                ),
                'trend_clarity': (
                    'clear'
                    if abs(self.lines.trend_strength[0]) > 0.02
                    else 'unclear'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.tweet_impact[0] > 1 and
                        abs(self.lines.market_mood[0]) > 0.2)
                    else 'unfavorable'
                )
            }
        }
