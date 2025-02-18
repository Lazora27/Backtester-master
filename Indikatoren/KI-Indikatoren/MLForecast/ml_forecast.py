import backtrader as bt
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from collections import deque

class MLForecast(bt.Indicator):
    """
    Machine Learning Forecast Indicator
    
    Ein ML-basierter Indikator zur Vorhersage
    von Preisbewegungen und Markttrends.
    
    Features:
    - Random Forest Regression
    - Feature Engineering
    - Ensemble Learning
    - Adaptive Vorhersagen
    
    Parameter:
    - lookback_period (30): Rückblickperiode
    - n_estimators (100): Anzahl der Bäume
    - forecast_horizon (5): Vorhersagehorizont
    """
    
    lines = ('forecast', 'confidence',
             'trend_strength', 'forecast_quality',
             'signal')
             
    params = (
        ('lookback_period', 30),
        ('n_estimators', 100),
        ('forecast_horizon', 5)
    )
    
    plotlines = dict(
        forecast=dict(color='blue', _name='Forecast'),
        confidence=dict(color='green', _name='Confidence'),
        trend_strength=dict(color='red', _name='Trend Strength'),
        forecast_quality=dict(color='purple', _name='Forecast Quality'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(MLForecast, self).__init__()
        
        # ML Setup
        self.model = RandomForestRegressor(
            n_estimators=self.p.n_estimators,
            random_state=42
        )
        
        self.scaler = StandardScaler()
        
        # Daten-Tracking
        self.price_history = deque(maxlen=self.p.lookback_period)
        self.volume_history = deque(maxlen=self.p.lookback_period)
        self.forecast_history = []
        self.confidence_history = []
        
    def calculate_features(self):
        """
        Berechnet Features für das ML-Modell.
        """
        if len(self.price_history) < self.p.lookback_period:
            return None
            
        prices = np.array(self.price_history)
        volumes = np.array(self.volume_history)
        
        # Technische Features
        returns = np.diff(prices) / prices[:-1]
        volatility = np.std(returns)
        momentum = prices[-1] / prices[0] - 1
        volume_trend = volumes[-1] / np.mean(volumes) - 1
        
        # Feature Matrix
        features = np.column_stack((
            returns,
            np.full_like(returns, volatility),
            np.full_like(returns, momentum),
            np.full_like(returns, volume_trend)
        ))
        
        return self.scaler.fit_transform(features)
        
    def train_model(self, features, targets):
        """
        Trainiert das ML-Modell.
        """
        if features is None or targets is None:
            return
            
        self.model.fit(features, targets)
        
    def make_forecast(self, features):
        """
        Erstellt eine Vorhersage.
        """
        if features is None:
            return None, 0
            
        # Vorhersage und Confidence
        predictions = []
        for estimator in self.model.estimators_:
            pred = estimator.predict(features[-1:])
            predictions.append(pred[0])
            
        forecast = np.mean(predictions)
        confidence = 1 - np.std(predictions)
        
        return forecast, confidence
        
    def calculate_trend_strength(self, forecast):
        """
        Berechnet die Stärke des vorhergesagten Trends.
        """
        if not self.forecast_history:
            return 0
            
        current_price = self.price_history[-1]
        trend = (forecast - current_price) / current_price
        
        return abs(trend)
        
    def calculate_forecast_quality(self, confidence):
        """
        Berechnet die Qualität der Vorhersage.
        """
        if len(self.forecast_history) < self.p.forecast_horizon:
            return confidence
            
        # Qualität basierend auf historischer Genauigkeit
        recent_forecasts = np.array(
            self.forecast_history[-self.p.forecast_horizon:]
        )
        recent_actuals = np.array(
            list(self.price_history)[-self.p.forecast_horizon:]
        )
        
        forecast_error = np.mean(
            np.abs(recent_forecasts - recent_actuals)
        )
        quality = 1 / (1 + forecast_error)
        
        return (quality + confidence) / 2
        
    def next(self):
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        # Historie aktualisieren
        self.price_history.append(price)
        self.volume_history.append(volume)
        
        # Features berechnen
        features = self.calculate_features()
        
        if features is not None:
            # Targets für Training
            targets = np.array(list(self.price_history)[1:])
            
            # Modell trainieren
            self.train_model(features, targets)
            
            # Vorhersage
            forecast, confidence = self.make_forecast(features)
            
            if forecast is not None:
                # Metriken berechnen
                trend_strength = self.calculate_trend_strength(
                    forecast
                )
                forecast_quality = self.calculate_forecast_quality(
                    confidence
                )
                
                # Historie aktualisieren
                self.forecast_history.append(forecast)
                self.confidence_history.append(confidence)
                
                # Linien aktualisieren
                self.lines.forecast[0] = forecast
                self.lines.confidence[0] = confidence
                self.lines.trend_strength[0] = trend_strength
                self.lines.forecast_quality[0] = forecast_quality
                
                # Trading Signal
                if forecast_quality > 0.7:
                    if forecast > price * 1.01:
                        self.lines.signal[0] = 1  # Kaufsignal
                    elif forecast < price * 0.99:
                        self.lines.signal[0] = -1  # Verkaufssignal
                    else:
                        self.lines.signal[0] = 0
                else:
                    self.lines.signal[0] = 0
            else:
                # Standardwerte
                self.lines.forecast[0] = price
                self.lines.confidence[0] = 0
                self.lines.trend_strength[0] = 0
                self.lines.forecast_quality[0] = 0
                self.lines.signal[0] = 0
        else:
            # Standardwerte
            self.lines.forecast[0] = price
            self.lines.confidence[0] = 0
            self.lines.trend_strength[0] = 0
            self.lines.forecast_quality[0] = 0
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_history = max(
            self.p.lookback_period,
            len(self.data)
        )
        if len(self.forecast_history) > max_history:
            self.forecast_history.pop(0)
        if len(self.confidence_history) > max_history:
            self.confidence_history.pop(0)
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'forecast_metrics': {
                'current_forecast': self.lines.forecast[0],
                'confidence': self.lines.confidence[0],
                'trend_strength': self.lines.trend_strength[0],
                'quality': self.lines.forecast_quality[0]
            },
            'trend_analysis': {
                'direction': (
                    'upward'
                    if self.lines.forecast[0] >
                       self.data.close[0]
                    else 'downward'
                    if self.lines.forecast[0] <
                       self.data.close[0]
                    else 'neutral'
                ),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    'high'
                    if self.lines.forecast_quality[0] > 0.7
                    else 'moderate'
                    if self.lines.forecast_quality[0] > 0.5
                    else 'low'
                )
            },
            'model_performance': {
                'forecast_accuracy': (
                    'high'
                    if self.lines.forecast_quality[0] > 0.7
                    else 'moderate'
                    if self.lines.forecast_quality[0] > 0.5
                    else 'low'
                ),
                'confidence_level': (
                    'high'
                    if self.lines.confidence[0] > 0.7
                    else 'moderate'
                    if self.lines.confidence[0] > 0.5
                    else 'low'
                ),
                'trend_quality': (
                    'strong'
                    if self.lines.trend_strength[0] > 0.02
                    else 'moderate'
                    if self.lines.trend_strength[0] > 0.01
                    else 'weak'
                )
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'reliability': self.lines.forecast_quality[0]
            },
            'market_conditions': {
                'forecast_quality': (
                    'reliable'
                    if self.lines.forecast_quality[0] > 0.7
                    else 'unreliable'
                ),
                'trend_clarity': (
                    'clear'
                    if self.lines.trend_strength[0] > 0.01
                    else 'unclear'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.forecast_quality[0] > 0.7 and
                        self.lines.trend_strength[0] > 0.01)
                    else 'unfavorable'
                )
            }
        }
