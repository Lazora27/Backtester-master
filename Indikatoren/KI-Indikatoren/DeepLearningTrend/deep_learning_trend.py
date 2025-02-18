import backtrader as bt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from collections import deque

class DeepLearningTrend(bt.Indicator):
    """
    Deep Learning Trend Predictor
    
    Ein fortgeschrittener Indikator, der Deep Learning
    verwendet, um Markttrends vorherzusagen.
    
    Features:
    - LSTM-basierte Trendvorhersage
    - Adaptive Gewichtung
    - Konfidenzmetrik
    - Dynamische Anpassung
    
    Parameter:
    - sequence_length (60): Sequenzlänge
    - prediction_steps (5): Vorhersageschritte
    - confidence_threshold (0.7): Konfidenzschwelle
    """
    
    lines = ('trend_prediction', 'prediction_confidence',
             'model_accuracy', 'signal_strength',
             'signal')
             
    params = (
        ('sequence_length', 60),
        ('prediction_steps', 5),
        ('confidence_threshold', 0.7)
    )
    
    plotlines = dict(
        trend_prediction=dict(color='blue', _name='Trend Prediction'),
        prediction_confidence=dict(color='green', _name='Prediction Confidence'),
        model_accuracy=dict(color='red', _name='Model Accuracy'),
        signal_strength=dict(color='purple', _name='Signal Strength'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(DeepLearningTrend, self).__init__()
        
        # Datenverarbeitung
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.price_history = deque(maxlen=self.p.sequence_length)
        self.volume_history = deque(maxlen=self.p.sequence_length)
        
        # Model Setup
        self.model = self.build_model()
        self.prediction_history = []
        self.confidence_history = []
        self.accuracy_history = []
        
    def build_model(self):
        """
        Erstellt das LSTM-Modell.
        """
        model = Sequential([
            LSTM(50, return_sequences=True,
                 input_shape=(self.p.sequence_length, 2)),
            Dropout(0.2),
            LSTM(50, return_sequences=False),
            Dropout(0.2),
            Dense(self.p.prediction_steps)
        ])
        
        model.compile(
            optimizer='adam',
            loss='mse',
            metrics=['mae']
        )
        
        return model
        
    def prepare_sequence(self):
        """
        Bereitet die Sequenz für das Modell vor.
        """
        if len(self.price_history) < self.p.sequence_length:
            return None
            
        # Daten normalisieren
        prices = np.array(self.price_history)
        volumes = np.array(self.volume_history)
        
        # Features kombinieren
        features = np.column_stack((
            self.scaler.fit_transform(
                prices.reshape(-1, 1)
            ).flatten(),
            self.scaler.fit_transform(
                volumes.reshape(-1, 1)
            ).flatten()
        ))
        
        return features.reshape(1, self.p.sequence_length, 2)
        
    def calculate_confidence(self, prediction):
        """
        Berechnet die Vorhersageconfidence.
        """
        if len(self.prediction_history) < 2:
            return 0.5
            
        # Confidence basierend auf Vorhersagegenauigkeit
        recent_predictions = np.array(
            self.prediction_history[-self.p.prediction_steps:]
        )
        recent_actuals = np.array(
            list(self.price_history)[-self.p.prediction_steps:]
        )
        
        prediction_error = np.mean(
            np.abs(recent_predictions - recent_actuals)
        )
        confidence = 1 / (1 + prediction_error)
        
        return confidence
        
    def update_model(self, sequence, actual):
        """
        Aktualisiert das Modell mit neuen Daten.
        """
        if sequence is None or actual is None:
            return
            
        # Modell mit einem Schritt trainieren
        target = np.array([actual])
        self.model.train_on_batch(sequence, target)
        
    def calculate_accuracy(self):
        """
        Berechnet die Modellgenauigkeit.
        """
        if len(self.prediction_history) < self.p.prediction_steps:
            return 0.5
            
        # MAE der letzten Vorhersagen
        predictions = np.array(
            self.prediction_history[-self.p.prediction_steps:]
        )
        actuals = np.array(
            list(self.price_history)[-self.p.prediction_steps:]
        )
        
        mae = np.mean(np.abs(predictions - actuals))
        accuracy = 1 / (1 + mae)
        
        return accuracy
        
    def next(self):
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        # Historie aktualisieren
        self.price_history.append(price)
        self.volume_history.append(volume)
        
        # Sequenz vorbereiten
        sequence = self.prepare_sequence()
        
        if sequence is not None:
            # Vorhersage
            prediction = self.model.predict(
                sequence, verbose=0
            )[0][0]
            
            # Metriken berechnen
            confidence = self.calculate_confidence(prediction)
            accuracy = self.calculate_accuracy()
            
            # Historie aktualisieren
            self.prediction_history.append(prediction)
            self.confidence_history.append(confidence)
            self.accuracy_history.append(accuracy)
            
            # Modell aktualisieren
            self.update_model(sequence, price)
            
            # Signal-Stärke
            signal_strength = confidence * accuracy
            
            # Linien aktualisieren
            self.lines.trend_prediction[0] = prediction
            self.lines.prediction_confidence[0] = confidence
            self.lines.model_accuracy[0] = accuracy
            self.lines.signal_strength[0] = signal_strength
            
            # Trading Signal
            if signal_strength > self.p.confidence_threshold:
                if prediction > price * 1.01:
                    self.lines.signal[0] = 1  # Kaufsignal
                elif prediction < price * 0.99:
                    self.lines.signal[0] = -1  # Verkaufssignal
                else:
                    self.lines.signal[0] = 0
            else:
                self.lines.signal[0] = 0
        else:
            # Standardwerte
            self.lines.trend_prediction[0] = price
            self.lines.prediction_confidence[0] = 0
            self.lines.model_accuracy[0] = 0
            self.lines.signal_strength[0] = 0
            self.lines.signal[0] = 0
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'prediction_metrics': {
                'current_prediction': self.lines.trend_prediction[0],
                'confidence': self.lines.prediction_confidence[0],
                'accuracy': self.lines.model_accuracy[0],
                'signal_strength': self.lines.signal_strength[0]
            },
            'trend_analysis': {
                'direction': (
                    'upward'
                    if self.lines.trend_prediction[0] >
                       self.data.close[0]
                    else 'downward'
                    if self.lines.trend_prediction[0] <
                       self.data.close[0]
                    else 'neutral'
                ),
                'strength': abs(
                    self.lines.trend_prediction[0] -
                    self.data.close[0]
                ),
                'reliability': (
                    'high'
                    if self.lines.prediction_confidence[0] >
                       self.p.confidence_threshold
                    else 'moderate'
                    if self.lines.prediction_confidence[0] > 0.5
                    else 'low'
                )
            },
            'model_performance': {
                'accuracy_level': (
                    'high'
                    if self.lines.model_accuracy[0] > 0.7
                    else 'moderate'
                    if self.lines.model_accuracy[0] > 0.5
                    else 'low'
                ),
                'confidence_level': (
                    'high'
                    if self.lines.prediction_confidence[0] > 0.7
                    else 'moderate'
                    if self.lines.prediction_confidence[0] > 0.5
                    else 'low'
                ),
                'overall_quality': (
                    'excellent'
                    if self.lines.signal_strength[0] > 0.8
                    else 'good'
                    if self.lines.signal_strength[0] > 0.6
                    else 'fair'
                    if self.lines.signal_strength[0] > 0.4
                    else 'poor'
                )
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'reliability': self.lines.signal_strength[0]
            },
            'market_conditions': {
                'prediction_quality': (
                    'reliable'
                    if self.lines.prediction_confidence[0] >
                       self.p.confidence_threshold
                    else 'unreliable'
                ),
                'trend_clarity': (
                    'clear'
                    if self.lines.signal_strength[0] >
                       self.p.confidence_threshold
                    else 'unclear'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.prediction_confidence[0] >
                        self.p.confidence_threshold and
                        self.lines.model_accuracy[0] > 0.6)
                    else 'unfavorable'
                )
            }
        }
