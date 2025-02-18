import backtrader as bt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
import tensorflow as tf

class NeuralPricePredictor(bt.Indicator):
    """
    Neural Network Price Predictor mit AI/ML-basierter Sentiment-Analyse
    
    Kombiniert LSTM Neural Networks mit technischer und Sentiment-Analyse
    für fortgeschrittene Preisvorhersagen.
    
    Features:
    - LSTM-basierte Preisvorhersage
    - Technische Indikatoren Integration
    - Sentiment-Analyse Integration
    - Adaptive Gewichtung
    - Dynamisches Retraining
    
    Parameter:
    - sequence_length (10): Länge der Input-Sequenz
    - prediction_length (5): Länge der Vorhersage
    - lstm_units (50): Anzahl LSTM-Einheiten
    - dropout_rate (0.2): Dropout-Rate
    - learning_rate (0.001): Lernrate
    - batch_size (32): Batch-Größe für Training
    - epochs (100): Trainingsepochen
    - retrain_interval (500): Intervall für Retraining
    """
    
    lines = ('predicted_price', 'prediction_upper',
             'prediction_lower', 'sentiment_score',
             'confidence', 'buy_signal', 'sell_signal')
             
    params = (
        ('sequence_length', 10),
        ('prediction_length', 5),
        ('lstm_units', 50),
        ('dropout_rate', 0.2),
        ('learning_rate', 0.001),
        ('batch_size', 32),
        ('epochs', 100),
        ('retrain_interval', 500),
        ('confidence_threshold', 0.7)
    )
    
    plotlines = dict(
        predicted_price=dict(color='blue', _name='Predicted'),
        prediction_upper=dict(color='green', _name='Upper Band'),
        prediction_lower=dict(color='red', _name='Lower Band'),
        sentiment_score=dict(color='purple', _name='Sentiment'),
        confidence=dict(color='orange', _name='Confidence'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(NeuralPricePredictor, self).__init__()
        
        # Technische Indikatoren
        self.rsi = bt.indicators.RSI(period=14)
        self.macd = bt.indicators.MACD()
        self.bbands = bt.indicators.BollingerBands()
        
        # Daten-Scaler
        self.price_scaler = MinMaxScaler()
        self.tech_scaler = MinMaxScaler()
        
        # Neural Network Model
        self.model = self.build_model()
        
        # Training History
        self.price_history = []
        self.tech_history = []
        self.sentiment_history = []
        
        # Letzte Vorhersagen
        self.last_predictions = []
        
        # Counter für Retraining
        self.counter = 0
        
    def build_model(self):
        """
        Erstellt das LSTM Neural Network Model.
        """
        model = Sequential([
            LSTM(units=self.p.lstm_units,
                 return_sequences=True,
                 input_shape=(self.p.sequence_length,
                            self.feature_dimension())),
            Dropout(self.p.dropout_rate),
            LSTM(units=self.p.lstm_units//2,
                 return_sequences=False),
            Dropout(self.p.dropout_rate),
            Dense(units=self.p.prediction_length)
        ])
        
        model.compile(
            optimizer=Adam(learning_rate=self.p.learning_rate),
            loss='mse',
            metrics=['mae']
        )
        
        return model
        
    def feature_dimension(self):
        """
        Berechnet die Feature-Dimension für das Model.
        """
        return 7  # Preis + RSI + MACD + BB + Volumen + Sentiment
        
    def prepare_features(self):
        """
        Bereitet Features für das Model vor.
        """
        # Preis-Features
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        # Technische Indikatoren
        rsi = self.rsi[0]
        macd = self.macd.macd[0]
        bb_top = self.bbands.top[0]
        bb_bottom = self.bbands.bot[0]
        
        # Sentiment (simuliert)
        sentiment = self.calculate_sentiment()
        
        features = np.array([
            price, rsi, macd,
            bb_top, bb_bottom, volume,
            sentiment
        ])
        
        return features
        
    def calculate_sentiment(self):
        """
        Berechnet einen Sentiment-Score basierend auf technischen Indikatoren
        und Marktdaten.
        """
        # Preis-Momentum
        price_momentum = (
            self.data.close[0] - self.data.close[-5]
        ) / self.data.close[-5]
        
        # RSI Sentiment
        rsi_sentiment = (self.rsi[0] - 50) / 50
        
        # MACD Sentiment
        macd_sentiment = 1 if self.macd.macd[0] > self.macd.signal[0] else -1
        
        # Volumen Sentiment
        volume_sma = bt.indicators.SMA(
            self.data.volume, period=20
        )[0]
        volume_sentiment = (
            self.data.volume[0] - volume_sma
        ) / volume_sma if volume_sma != 0 else 0
        
        # Kombinierter Sentiment-Score
        sentiment = (
            0.3 * price_momentum +
            0.3 * rsi_sentiment +
            0.2 * macd_sentiment +
            0.2 * volume_sentiment
        )
        
        return max(min(sentiment, 1), -1)
        
    def prepare_batch(self):
        """
        Bereitet einen Batch von Sequenzen für das Training vor.
        """
        features = []
        targets = []
        
        if len(self.price_history) >= self.p.sequence_length:
            # Features vorbereiten
            sequence = np.array(
                self.price_history[-self.p.sequence_length:]
            )
            features.append(sequence)
            
            # Ziel-Preise
            if len(self.price_history) >= (
                self.p.sequence_length + self.p.prediction_length
            ):
                target = np.array(
                    self.price_history[
                        -self.p.sequence_length-self.p.prediction_length:
                        -self.p.sequence_length
                    ]
                )
                targets.append(target)
        
        return np.array(features), np.array(targets)
        
    def train_model(self):
        """
        Trainiert das Neural Network Model.
        """
        features, targets = self.prepare_batch()
        
        if len(features) > 0 and len(targets) > 0:
            self.model.fit(
                features, targets,
                batch_size=self.p.batch_size,
                epochs=self.p.epochs,
                verbose=0
            )
            
    def make_prediction(self):
        """
        Macht eine Vorhersage für zukünftige Preise.
        """
        if len(self.price_history) >= self.p.sequence_length:
            # Sequenz vorbereiten
            sequence = np.array(
                self.price_history[-self.p.sequence_length:]
            )
            sequence = sequence.reshape(
                (1, self.p.sequence_length, self.feature_dimension())
            )
            
            # Vorhersage
            prediction = self.model.predict(sequence, verbose=0)
            
            # Confidence berechnen
            confidence = self.calculate_confidence(prediction[0])
            
            return prediction[0], confidence
            
        return None, 0.0
        
    def calculate_confidence(self, prediction):
        """
        Berechnet die Konfidenz der Vorhersage.
        """
        if len(self.last_predictions) > 0:
            # Vergleich mit letzter Vorhersage
            last_pred = self.last_predictions[-1]
            diff = np.mean(np.abs(prediction - last_pred))
            
            # Konfidenz basierend auf Stabilität
            confidence = 1.0 - min(diff, 1.0)
            
            # Sentiment-Einfluss
            sentiment_factor = abs(self.lines.sentiment_score[0])
            
            return (confidence * 0.7 + sentiment_factor * 0.3)
            
        return 0.5
        
    def next(self):
        # Features sammeln
        current_features = self.prepare_features()
        self.price_history.append(current_features)
        
        # Sentiment berechnen
        self.lines.sentiment_score[0] = self.calculate_sentiment()
        
        # Retraining Check
        self.counter += 1
        if self.counter >= self.p.retrain_interval:
            self.train_model()
            self.counter = 0
            
        # Vorhersage
        prediction, confidence = self.make_prediction()
        
        if prediction is not None:
            # Vorhersage-Werte setzen
            self.lines.predicted_price[0] = prediction[0]
            self.lines.prediction_upper[0] = prediction[0] * (1 + confidence * 0.1)
            self.lines.prediction_lower[0] = prediction[0] * (1 - confidence * 0.1)
            self.lines.confidence[0] = confidence
            
            # Signale generieren
            if (confidence > self.p.confidence_threshold and
                self.lines.sentiment_score[0] > 0.5):
                self.lines.buy_signal[0] = self.data.low[0]
                self.lines.sell_signal[0] = float('nan')
            elif (confidence > self.p.confidence_threshold and
                  self.lines.sentiment_score[0] < -0.5):
                self.lines.buy_signal[0] = float('nan')
                self.lines.sell_signal[0] = self.data.high[0]
            else:
                self.lines.buy_signal[0] = float('nan')
                self.lines.sell_signal[0] = float('nan')
                
            # Historie aktualisieren
            self.last_predictions.append(prediction)
            if len(self.last_predictions) > self.p.prediction_length:
                self.last_predictions.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse der Vorhersagen.
        """
        return {
            'current_prediction': {
                'price': self.lines.predicted_price[0],
                'upper_band': self.lines.prediction_upper[0],
                'lower_band': self.lines.prediction_lower[0],
                'confidence': self.lines.confidence[0]
            },
            'sentiment': {
                'score': self.lines.sentiment_score[0],
                'signal': ('bullish' if self.lines.sentiment_score[0] > 0.5
                          else 'bearish' if self.lines.sentiment_score[0] < -0.5
                          else 'neutral')
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan')
            },
            'model_state': {
                'samples_seen': len(self.price_history),
                'last_retrain': self.counter,
                'next_retrain': self.p.retrain_interval - self.counter
            }
        }
