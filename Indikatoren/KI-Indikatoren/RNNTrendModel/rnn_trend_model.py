import backtrader as bt
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, GRU, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler
from collections import deque

class RNNTrendModel(bt.Indicator):
    """
    Recurrent Neural Network Trend Model
    
    Ein RNN-basierter Indikator zur Analyse und
    Vorhersage von Markttrends.
    
    Features:
    - LSTM/GRU Architektur
    - Sequenzbasierte Analyse
    - Trend-Klassifikation
    - Adaptive Optimierung
    
    Parameter:
    - sequence_length (60): Sequenzlänge
    - hidden_units (50): Versteckte Einheiten
    - dropout_rate (0.2): Dropout-Rate
    - use_gru (False): GRU statt LSTM
    """
    
    lines = ('trend_prediction', 'model_confidence',
             'sequence_quality', 'prediction_strength',
             'signal')
             
    params = (
        ('sequence_length', 60),
        ('hidden_units', 50),
        ('dropout_rate', 0.2),
        ('use_gru', False)
    )
    
    plotlines = dict(
        trend_prediction=dict(color='blue', _name='Trend Prediction'),
        model_confidence=dict(color='green', _name='Model Confidence'),
        sequence_quality=dict(color='red', _name='Sequence Quality'),
        prediction_strength=dict(color='purple', _name='Prediction Strength'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(RNNTrendModel, self).__init__()
        
        # Datenverarbeitung
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.price_history = deque(maxlen=self.p.sequence_length)
        self.volume_history = deque(maxlen=self.p.sequence_length)
        
        # Modell Setup
        self.model = self.build_model()
        self.prediction_history = []
        self.confidence_history = []
        
        # Optimizer
        self.optimizer = Adam(learning_rate=0.001)
        
    def build_model(self):
        """
        Erstellt das RNN-Modell.
        """
        model = Sequential()
        
        # RNN-Layer (LSTM oder GRU)
        if self.p.use_gru:
            model.add(GRU(
                self.p.hidden_units,
                input_shape=(self.p.sequence_length, 2),
                return_sequences=True
            ))
        else:
            model.add(LSTM(
                self.p.hidden_units,
                input_shape=(self.p.sequence_length, 2),
                return_sequences=True
            ))
            
        model.add(Dropout(self.p.dropout_rate))
        
        # Zweiter RNN-Layer
        if self.p.use_gru:
            model.add(GRU(
                self.p.hidden_units,
                return_sequences=False
            ))
        else:
            model.add(LSTM(
                self.p.hidden_units,
                return_sequences=False
            ))
            
        model.add(Dropout(self.p.dropout_rate))
        
        # Dense Layers
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1, activation='tanh'))
        
        model.compile(
            optimizer=self.optimizer,
            loss='mse',
            metrics=['mae']
        )
        
        return model
        
    def prepare_sequence(self):
        """
        Bereitet die Sequenz für das RNN vor.
        """
        if len(self.price_history) < self.p.sequence_length:
            return None
            
        # Daten normalisieren
        prices = np.array(self.price_history)
        volumes = np.array(self.volume_history)
        
        normalized_prices = self.scaler.fit_transform(
            prices.reshape(-1, 1)
        ).flatten()
        
        normalized_volumes = self.scaler.fit_transform(
            volumes.reshape(-1, 1)
        ).flatten()
        
        # Sequenz erstellen
        sequence = np.column_stack((
            normalized_prices,
            normalized_volumes
        ))
        
        return sequence.reshape(1, self.p.sequence_length, 2)
        
    def calculate_confidence(self, prediction):
        """
        Berechnet die Modell-Confidence.
        """
        if len(self.prediction_history) < 2:
            return 0.5
            
        # Prediction Stability
        recent_predictions = np.array(
            self.prediction_history[-5:]
        )
        stability = 1 - np.std(recent_predictions)
        
        # Trend Strength
        trend_strength = abs(prediction)
        
        return (stability + trend_strength) / 2
        
    def evaluate_sequence(self, sequence):
        """
        Bewertet die Qualität der Sequenz.
        """
        if sequence is None:
            return 0
            
        # Volatilität
        price_volatility = np.std(
            sequence[0, :, 0]
        )
        
        # Volumen-Stabilität
        volume_stability = 1 - np.std(
            sequence[0, :, 1]
        )
        
        return (1 - price_volatility + volume_stability) / 2
        
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
            sequence_quality = self.evaluate_sequence(sequence)
            prediction_strength = abs(prediction)
            
            # Historie aktualisieren
            self.prediction_history.append(prediction)
            self.confidence_history.append(confidence)
            
            # Modell aktualisieren
            if len(self.price_history) > 1:
                target = np.array([[
                    (self.price_history[-1] -
                     self.price_history[-2]) /
                    self.price_history[-2]
                ]])
                self.model.train_on_batch(sequence, target)
            
            # Linien aktualisieren
            self.lines.trend_prediction[0] = prediction
            self.lines.model_confidence[0] = confidence
            self.lines.sequence_quality[0] = sequence_quality
            self.lines.prediction_strength[0] = prediction_strength
            
            # Trading Signal
            if (confidence > 0.7 and
                sequence_quality > 0.6):
                if prediction > 0.02:
                    self.lines.signal[0] = 1  # Kaufsignal
                elif prediction < -0.02:
                    self.lines.signal[0] = -1  # Verkaufssignal
                else:
                    self.lines.signal[0] = 0
            else:
                self.lines.signal[0] = 0
        else:
            # Standardwerte
            self.lines.trend_prediction[0] = 0
            self.lines.model_confidence[0] = 0
            self.lines.sequence_quality[0] = 0
            self.lines.prediction_strength[0] = 0
            self.lines.signal[0] = 0
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'trend_metrics': {
                'prediction': self.lines.trend_prediction[0],
                'confidence': self.lines.model_confidence[0],
                'quality': self.lines.sequence_quality[0],
                'strength': self.lines.prediction_strength[0]
            },
            'model_performance': {
                'confidence_level': (
                    'high'
                    if self.lines.model_confidence[0] > 0.7
                    else 'moderate'
                    if self.lines.model_confidence[0] > 0.5
                    else 'low'
                ),
                'sequence_quality': (
                    'high'
                    if self.lines.sequence_quality[0] > 0.7
                    else 'moderate'
                    if self.lines.sequence_quality[0] > 0.5
                    else 'low'
                ),
                'prediction_strength': (
                    'strong'
                    if self.lines.prediction_strength[0] > 0.02
                    else 'moderate'
                    if self.lines.prediction_strength[0] > 0.01
                    else 'weak'
                )
            },
            'trend_analysis': {
                'direction': (
                    'upward'
                    if self.lines.trend_prediction[0] > 0.02
                    else 'downward'
                    if self.lines.trend_prediction[0] < -0.02
                    else 'neutral'
                ),
                'strength': abs(self.lines.trend_prediction[0]),
                'reliability': (
                    'reliable'
                    if (self.lines.model_confidence[0] > 0.7 and
                        self.lines.sequence_quality[0] > 0.6)
                    else 'unreliable'
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
                    self.lines.model_confidence[0] *
                    self.lines.sequence_quality[0]
                )
            },
            'sequence_analysis': {
                'quality_level': (
                    'optimal'
                    if self.lines.sequence_quality[0] > 0.8
                    else 'good'
                    if self.lines.sequence_quality[0] > 0.6
                    else 'poor'
                ),
                'stability': (
                    'stable'
                    if len(self.prediction_history) > 5 and
                    np.std(self.prediction_history[-5:]) < 0.01
                    else 'volatile'
                ),
                'trend_consistency': (
                    'consistent'
                    if len(self.prediction_history) > 3 and
                    all(p * self.lines.trend_prediction[0] > 0
                        for p in self.prediction_history[-3:])
                    else 'inconsistent'
                )
            }
        }
