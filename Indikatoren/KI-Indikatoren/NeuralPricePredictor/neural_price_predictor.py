import backtrader as bt
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler
from collections import deque

class NeuralPricePredictor(bt.Indicator):
    """
    Neural Network Price Predictor
    
    Ein neuronales Netzwerk zur Vorhersage von
    Preisbewegungen mit mehrschichtiger Architektur.
    
    Features:
    - Deep Neural Network
    - Preisvorhersage
    - Adaptive Learning
    - Konfidenzmetrik
    
    Parameter:
    - lookback (50): Rückblickperiode
    - hidden_layers (3): Anzahl versteckter Schichten
    - neurons_per_layer (64): Neuronen pro Schicht
    - learning_rate (0.001): Lernrate
    """
    
    lines = ('price_prediction', 'prediction_error',
             'confidence_score', 'learning_rate',
             'signal')
             
    params = (
        ('lookback', 50),
        ('hidden_layers', 3),
        ('neurons_per_layer', 64),
        ('learning_rate', 0.001)
    )
    
    plotlines = dict(
        price_prediction=dict(color='blue', _name='Price Prediction'),
        prediction_error=dict(color='red', _name='Prediction Error'),
        confidence_score=dict(color='green', _name='Confidence Score'),
        learning_rate=dict(color='purple', _name='Learning Rate'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(NeuralPricePredictor, self).__init__()
        
        # Datenverarbeitung
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.price_history = deque(maxlen=self.p.lookback)
        self.volume_history = deque(maxlen=self.p.lookback)
        
        # Modell Setup
        self.model = self.build_model()
        self.prediction_history = []
        self.error_history = []
        
        # Optimizer mit adaptiver Lernrate
        self.optimizer = Adam(learning_rate=self.p.learning_rate)
        
    def build_model(self):
        """
        Erstellt das neuronale Netzwerk.
        """
        model = Sequential()
        
        # Eingabeschicht
        model.add(Dense(
            self.p.neurons_per_layer,
            input_shape=(self.p.lookback * 2,),
            activation='relu'
        ))
        model.add(BatchNormalization())
        
        # Versteckte Schichten
        for _ in range(self.p.hidden_layers):
            model.add(Dense(
                self.p.neurons_per_layer,
                activation='relu'
            ))
            model.add(BatchNormalization())
        
        # Ausgabeschicht
        model.add(Dense(1, activation='linear'))
        
        model.compile(
            optimizer=self.optimizer,
            loss='mse',
            metrics=['mae']
        )
        
        return model
        
    def prepare_data(self):
        """
        Bereitet die Daten für das Modell vor.
        """
        if len(self.price_history) < self.p.lookback:
            return None
            
        # Preis- und Volumendaten normalisieren
        prices = np.array(self.price_history)
        volumes = np.array(self.volume_history)
        
        normalized_prices = self.scaler.fit_transform(
            prices.reshape(-1, 1)
        ).flatten()
        
        normalized_volumes = self.scaler.fit_transform(
            volumes.reshape(-1, 1)
        ).flatten()
        
        # Features kombinieren
        features = np.concatenate([
            normalized_prices,
            normalized_volumes
        ])
        
        return features.reshape(1, -1)
        
    def calculate_confidence(self, prediction, error):
        """
        Berechnet den Confidence Score.
        """
        if len(self.prediction_history) < 2:
            return 0.5
            
        # Confidence basierend auf Vorhersagegenauigkeit
        confidence = 1 / (1 + error)
        
        # Trend-Konsistenz
        recent_predictions = np.array(
            self.prediction_history[-5:]
        )
        trend_consistency = 1 - np.std(recent_predictions)
        
        return (confidence + trend_consistency) / 2
        
    def adapt_learning_rate(self, error):
        """
        Passt die Lernrate basierend auf dem Fehler an.
        """
        if len(self.error_history) < 2:
            return self.p.learning_rate
            
        error_change = (
            error - self.error_history[-1]
        ) / self.error_history[-1]
        
        # Lernrate anpassen
        if error_change > 0.1:
            new_rate = self.optimizer.learning_rate * 0.8
        elif error_change < -0.1:
            new_rate = self.optimizer.learning_rate * 1.2
        else:
            new_rate = self.optimizer.learning_rate
            
        # Grenzen setzen
        return np.clip(
            new_rate,
            0.0001,
            0.01
        )
        
    def next(self):
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        # Historie aktualisieren
        self.price_history.append(price)
        self.volume_history.append(volume)
        
        # Daten vorbereiten
        features = self.prepare_data()
        
        if features is not None:
            # Vorhersage
            prediction = self.model.predict(
                features, verbose=0
            )[0][0]
            
            # Fehler berechnen
            prediction_error = abs(prediction - price) / price
            
            # Confidence berechnen
            confidence = self.calculate_confidence(
                prediction,
                prediction_error
            )
            
            # Lernrate anpassen
            new_learning_rate = self.adapt_learning_rate(
                prediction_error
            )
            
            # Historie aktualisieren
            self.prediction_history.append(prediction)
            self.error_history.append(prediction_error)
            
            # Modell aktualisieren
            if len(self.price_history) > 1:
                target = np.array([[self.price_history[-1]]])
                self.model.train_on_batch(features, target)
            
            # Linien aktualisieren
            self.lines.price_prediction[0] = prediction
            self.lines.prediction_error[0] = prediction_error
            self.lines.confidence_score[0] = confidence
            self.lines.learning_rate[0] = new_learning_rate
            
            # Trading Signal
            if confidence > 0.7:
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
            self.lines.price_prediction[0] = price
            self.lines.prediction_error[0] = 0
            self.lines.confidence_score[0] = 0
            self.lines.learning_rate[0] = self.p.learning_rate
            self.lines.signal[0] = 0
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'prediction_metrics': {
                'current_prediction': self.lines.price_prediction[0],
                'error': self.lines.prediction_error[0],
                'confidence': self.lines.confidence_score[0],
                'learning_rate': self.lines.learning_rate[0]
            },
            'model_performance': {
                'accuracy': (
                    'high'
                    if self.lines.prediction_error[0] < 0.01
                    else 'moderate'
                    if self.lines.prediction_error[0] < 0.03
                    else 'low'
                ),
                'confidence_level': (
                    'high'
                    if self.lines.confidence_score[0] > 0.7
                    else 'moderate'
                    if self.lines.confidence_score[0] > 0.5
                    else 'low'
                ),
                'learning_status': (
                    'optimal'
                    if 0.0005 < self.lines.learning_rate[0] < 0.005
                    else 'adjusting'
                )
            },
            'prediction_analysis': {
                'direction': (
                    'upward'
                    if self.lines.price_prediction[0] >
                       self.data.close[0]
                    else 'downward'
                    if self.lines.price_prediction[0] <
                       self.data.close[0]
                    else 'neutral'
                ),
                'magnitude': abs(
                    self.lines.price_prediction[0] -
                    self.data.close[0]
                ) / self.data.close[0],
                'reliability': (
                    'reliable'
                    if self.lines.confidence_score[0] > 0.7
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
                'confidence': self.lines.confidence_score[0]
            },
            'model_status': {
                'learning_phase': (
                    'stable'
                    if len(self.error_history) > 10 and
                    np.std(self.error_history[-10:]) < 0.01
                    else 'learning'
                ),
                'prediction_quality': (
                    'improving'
                    if len(self.error_history) > 1 and
                    self.error_history[-1] < self.error_history[-2]
                    else 'deteriorating'
                ),
                'adaptation_status': (
                    'adapting'
                    if self.lines.learning_rate[0] !=
                       self.p.learning_rate
                    else 'stable'
                )
            }
        }
