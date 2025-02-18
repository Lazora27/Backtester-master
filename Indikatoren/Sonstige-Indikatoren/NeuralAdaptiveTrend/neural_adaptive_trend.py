import backtrader as bt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
import tensorflow as tf

class NeuralAdaptiveTrendIndicator(bt.Indicator):
    """
    Neural Adaptive Trend Indicator
    
    Ein KI-basierter Indikator, der Markttrends durch
    neuronale Netze erkennt und adaptiv anpasst.
    
    Features:
    - LSTM-basierte Trendvorhersage
    - Adaptive Gewichtung
    - Online-Learning
    - Konfidenzmetrik
    - Multi-Feature-Analyse
    
    Parameter:
    - lookback (50): Rückblickperiode
    - hidden_units (64): Neuronen im Hidden Layer
    - dropout (0.2): Dropout-Rate
    - learning_rate (0.001): Lernrate
    """
    
    lines = ('trend', 'confidence', 'prediction')
    params = (
        ('lookback', 50),
        ('hidden_units', 64),
        ('dropout', 0.2),
        ('learning_rate', 0.001),
    )
    
    plotlines = dict(
        trend=dict(color='blue', _name='Trend'),
        confidence=dict(color='green', _name='Confidence'),
        prediction=dict(color='red', _name='Prediction')
    )
    
    def __init__(self):
        super(NeuralAdaptiveTrendIndicator, self).__init__()
        
        # Feature-Engineering
        self.feature_indicators = {
            'rsi': bt.indicators.RSI(self.data, period=14),
            'macd': bt.indicators.MACD(self.data),
            'bbands': bt.indicators.BollingerBands(self.data),
            'atr': bt.indicators.ATR(self.data)
        }
        
        # Datenpuffer
        self.price_history = []
        self.feature_history = []
        
        # Scaler für Normalisierung
        self.price_scaler = MinMaxScaler()
        self.feature_scaler = MinMaxScaler()
        
        # LSTM-Modell erstellen
        self.model = self._build_model()
        
        # Online-Learning-Puffer
        self.training_buffer = []
        self.training_labels = []
        
    def _build_model(self):
        """Erstellt das LSTM-Modell"""
        model = Sequential([
            LSTM(
                self.p.hidden_units,
                input_shape=(self.p.lookback, 5),
                return_sequences=True
            ),
            Dropout(self.p.dropout),
            LSTM(
                self.p.hidden_units // 2,
                return_sequences=False
            ),
            Dropout(self.p.dropout),
            Dense(32, activation='relu'),
            Dense(1, activation='tanh')
        ])
        
        model.compile(
            optimizer=Adam(learning_rate=self.p.learning_rate),
            loss='mse',
            metrics=['mae']
        )
        
        return model
        
    def _prepare_features(self):
        """Bereitet Features für das Modell vor"""
        current_features = np.array([
            self.data[0],  # Close
            self.feature_indicators['rsi'][0],
            self.feature_indicators['macd'].lines.macd[0],
            self.feature_indicators['bbands'].lines.mid[0],
            self.feature_indicators['atr'][0]
        ])
        
        self.feature_history.append(current_features)
        
        if len(self.feature_history) > self.p.lookback:
            self.feature_history.pop(0)
            
        return current_features
        
    def _prepare_sequence(self):
        """Bereitet Sequenz für LSTM vor"""
        if len(self.feature_history) < self.p.lookback:
            return None
            
        # Normalisierung
        sequence = np.array(self.feature_history)
        sequence = self.feature_scaler.fit_transform(sequence)
        
        return sequence.reshape(1, self.p.lookback, 5)
        
    def _calculate_confidence(self, prediction, features):
        """Berechnet Konfidenzmetrik"""
        # Volatilität berücksichtigen
        volatility = self.feature_indicators['atr'][0]
        norm_volatility = volatility / self.data[0]
        
        # Trend-Konsistenz
        trend_consistency = np.mean([
            1 if prediction > 0 and f > 0 else
            1 if prediction < 0 and f < 0 else
            0
            for f in features
        ])
        
        # Konfidenz basierend auf Volatilität und Konsistenz
        confidence = (
            (1 - norm_volatility) * 0.5 +
            trend_consistency * 0.5
        )
        
        return max(0, min(1, confidence))
        
    def _online_learning(self, features, actual_change):
        """Führt Online-Learning durch"""
        self.training_buffer.append(features)
        self.training_labels.append(actual_change)
        
        if len(self.training_buffer) >= 32:  # Mini-Batch
            X = np.array(self.training_buffer)
            y = np.array(self.training_labels)
            
            # Normalisierung
            X = self.feature_scaler.transform(X)
            X = X.reshape(-1, self.p.lookback, 5)
            
            # Training
            self.model.train_on_batch(X, y)
            
            # Buffer leeren
            self.training_buffer = []
            self.training_labels = []
            
    def next(self):
        # Features vorbereiten
        current_features = self._prepare_features()
        
        if len(self.feature_history) < self.p.lookback:
            return
            
        # Sequenz für Vorhersage vorbereiten
        sequence = self._prepare_sequence()
        if sequence is None:
            return
            
        # Vorhersage
        with tf.device('/CPU:0'):  # CPU-Ausführung
            prediction = self.model.predict(
                sequence,
                verbose=0
            )[0][0]
            
        # Konfidenz berechnen
        confidence = self._calculate_confidence(
            prediction,
            current_features
        )
        
        # Online-Learning
        if len(self.data) > 1:
            actual_change = (
                self.data[0] - self.data[-1]
            ) / self.data[-1]
            self._online_learning(
                current_features,
                actual_change
            )
            
        # Linien aktualisieren
        self.lines.trend[0] = np.sign(prediction)
        self.lines.confidence[0] = confidence
        self.lines.prediction[0] = prediction
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        current_trend = self.lines.trend[0]
        current_conf = self.lines.confidence[0]
        current_pred = self.lines.prediction[0]
        
        return {
            'trend_analysis': {
                'direction': (
                    'aufwärts' if current_trend > 0
                    else 'abwärts' if current_trend < 0
                    else 'neutral'
                ),
                'strength': abs(current_pred),
                'confidence': current_conf
            },
            'predictions': {
                'raw_value': current_pred,
                'normalized': current_pred * current_conf,
                'reliability': (
                    'hoch' if current_conf > 0.8
                    else 'mittel' if current_conf > 0.5
                    else 'niedrig'
                )
            },
            'learning_metrics': {
                'buffer_size': len(self.training_buffer),
                'training_status': (
                    'aktiv' if self.training_buffer else
                    'wartend'
                )
            },
            'trading_signals': {
                'primary': (
                    'strong_buy' if (
                        current_trend > 0 and
                        current_conf > 0.8
                    )
                    else 'buy' if (
                        current_trend > 0 and
                        current_conf > 0.5
                    )
                    else 'strong_sell' if (
                        current_trend < 0 and
                        current_conf > 0.8
                    )
                    else 'sell' if (
                        current_trend < 0 and
                        current_conf > 0.5
                    )
                    else 'neutral'
                ),
                'confidence_level': current_conf,
                'prediction_magnitude': abs(current_pred)
            }
        }
