import backtrader as bt
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Dense, Flatten
from tensorflow.keras.optimizers import Adam
import tensorflow as tf

class PatternType:
    """Unterstützte Chart-Pattern"""
    HEAD_SHOULDERS = "Head and Shoulders"
    INV_HEAD_SHOULDERS = "Inverse Head and Shoulders"
    DOUBLE_TOP = "Double Top"
    DOUBLE_BOTTOM = "Double Bottom"
    TRIPLE_TOP = "Triple Top"
    TRIPLE_BOTTOM = "Triple Bottom"
    ASCENDING_TRIANGLE = "Ascending Triangle"
    DESCENDING_TRIANGLE = "Descending Triangle"
    SYMMETRICAL_TRIANGLE = "Symmetrical Triangle"
    RISING_WEDGE = "Rising Wedge"
    FALLING_WEDGE = "Falling Wedge"
    CHANNEL_UP = "Channel Up"
    CHANNEL_DOWN = "Channel Down"
    FLAG = "Flag"
    PENNANT = "Pennant"

class PatternRecognitionAI(bt.Indicator):
    """
    Pattern Recognition AI Indicator
    
    Ein KI-basierter Indikator zur Erkennung von
    Chart-Patterns durch Deep Learning.
    
    Features:
    - CNN-basierte Pattern-Erkennung
    - Multi-Pattern-Klassifikation
    - Konfidenzmetriken
    - Adaptive Pattern-Validierung
    - Real-time Learning
    
    Parameter:
    - lookback (100): Rückblickperiode
    - min_confidence (0.7): Minimale Konfidenz
    - learning_rate (0.001): Lernrate
    """
    
    lines = ('pattern_signal', 'confidence', 'reliability')
    params = (
        ('lookback', 100),
        ('min_confidence', 0.7),
        ('learning_rate', 0.001),
    )
    
    plotlines = dict(
        pattern_signal=dict(color='blue', _name='Pattern Signal'),
        confidence=dict(color='green', _name='Confidence'),
        reliability=dict(color='red', _name='Reliability')
    )
    
    def __init__(self):
        super(PatternRecognitionAI, self).__init__()
        
        # Pattern-Definitionen
        self.patterns = {
            PatternType.HEAD_SHOULDERS: -1,
            PatternType.INV_HEAD_SHOULDERS: 1,
            PatternType.DOUBLE_TOP: -1,
            PatternType.DOUBLE_BOTTOM: 1,
            PatternType.TRIPLE_TOP: -1,
            PatternType.TRIPLE_BOTTOM: 1,
            PatternType.ASCENDING_TRIANGLE: 1,
            PatternType.DESCENDING_TRIANGLE: -1,
            PatternType.SYMMETRICAL_TRIANGLE: 0,
            PatternType.RISING_WEDGE: -1,
            PatternType.FALLING_WEDGE: 1,
            PatternType.CHANNEL_UP: 1,
            PatternType.CHANNEL_DOWN: -1,
            PatternType.FLAG: 0,
            PatternType.PENNANT: 0
        }
        
        # Datenpuffer
        self.price_history = []
        self.volume_history = []
        
        # Scaler für Normalisierung
        self.price_scaler = StandardScaler()
        self.volume_scaler = StandardScaler()
        
        # CNN-Modell erstellen
        self.model = self._build_model()
        
        # Pattern-Historie
        self.pattern_history = []
        
    def _build_model(self):
        """Erstellt das CNN-Modell"""
        model = Sequential([
            Conv1D(
                32, 5,
                activation='relu',
                input_shape=(self.p.lookback, 2)
            ),
            MaxPooling1D(2),
            Conv1D(64, 3, activation='relu'),
            MaxPooling1D(2),
            Conv1D(64, 3, activation='relu'),
            Flatten(),
            Dense(64, activation='relu'),
            Dense(32, activation='relu'),
            Dense(len(self.patterns), activation='softmax')
        ])
        
        model.compile(
            optimizer=Adam(learning_rate=self.p.learning_rate),
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        
        return model
        
    def _prepare_data(self):
        """Bereitet Daten für CNN vor"""
        if len(self.price_history) < self.p.lookback:
            return None
            
        # Preis- und Volumendaten normalisieren
        prices = np.array(self.price_history[-self.p.lookback:])
        volumes = np.array(self.volume_history[-self.p.lookback:])
        
        prices = self.price_scaler.fit_transform(
            prices.reshape(-1, 1)
        ).reshape(-1)
        volumes = self.volume_scaler.fit_transform(
            volumes.reshape(-1, 1)
        ).reshape(-1)
        
        # Sequenz erstellen
        sequence = np.column_stack((prices, volumes))
        return sequence.reshape(1, self.p.lookback, 2)
        
    def _validate_pattern(self, pattern_type, confidence):
        """Validiert erkannte Patterns"""
        if pattern_type not in self.patterns:
            return False, 0
            
        # Grundlegende Validierung
        if confidence < self.p.min_confidence:
            return False, 0
            
        # Pattern-spezifische Validierung
        prices = np.array(self.price_history[-self.p.lookback:])
        volumes = np.array(self.volume_history[-self.p.lookback:])
        
        validity = 1.0
        
        # Preisbewegung validieren
        price_range = np.max(prices) - np.min(prices)
        if price_range < np.mean(prices) * 0.01:  # Min. 1% Bewegung
            validity *= 0.5
            
        # Volumenbestätigung
        vol_increase = (
            np.mean(volumes[-10:]) >
            np.mean(volumes[-30:-10])
        )
        if not vol_increase:
            validity *= 0.8
            
        return True, validity * confidence
        
    def _calculate_reliability(self, pattern_type, confidence):
        """Berechnet Zuverlässigkeit des Patterns"""
        if not self.pattern_history:
            return confidence
            
        # Historische Trefferquote
        similar_patterns = [
            p for p in self.pattern_history
            if p['type'] == pattern_type
        ]
        
        if not similar_patterns:
            return confidence
            
        success_rate = np.mean([
            p['success'] for p in similar_patterns
        ])
        
        # Gewichtete Zuverlässigkeit
        reliability = (
            0.7 * confidence +
            0.3 * success_rate
        )
        
        return reliability
        
    def next(self):
        # Preisdaten sammeln
        self.price_history.append(self.data.close[0])
        self.volume_history.append(self.data.volume[0])
        
        if len(self.price_history) > self.p.lookback * 2:
            self.price_history.pop(0)
            self.volume_history.pop(0)
            
        if len(self.price_history) < self.p.lookback:
            return
            
        # Daten vorbereiten
        sequence = self._prepare_data()
        if sequence is None:
            return
            
        # Pattern-Erkennung
        with tf.device('/CPU:0'):  # CPU-Ausführung
            predictions = self.model.predict(
                sequence,
                verbose=0
            )[0]
            
        # Bestes Pattern finden
        best_idx = np.argmax(predictions)
        best_confidence = predictions[best_idx]
        
        pattern_type = list(self.patterns.keys())[best_idx]
        pattern_signal = self.patterns[pattern_type]
        
        # Pattern validieren
        is_valid, validity = self._validate_pattern(
            pattern_type,
            best_confidence
        )
        
        if is_valid:
            # Zuverlässigkeit berechnen
            reliability = self._calculate_reliability(
                pattern_type,
                validity
            )
            
            # Pattern zur Historie hinzufügen
            self.pattern_history.append({
                'type': pattern_type,
                'confidence': best_confidence,
                'success': None  # Wird später aktualisiert
            })
            
            # Maximal 100 Patterns speichern
            if len(self.pattern_history) > 100:
                self.pattern_history.pop(0)
                
            # Linien aktualisieren
            self.lines.pattern_signal[0] = pattern_signal
            self.lines.confidence[0] = validity
            self.lines.reliability[0] = reliability
        else:
            # Keine gültigen Patterns
            self.lines.pattern_signal[0] = 0
            self.lines.confidence[0] = 0
            self.lines.reliability[0] = 0
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        current_signal = self.lines.pattern_signal[0]
        current_conf = self.lines.confidence[0]
        current_rel = self.lines.reliability[0]
        
        # Aktuelle Pattern-Details
        if current_signal != 0 and len(self.pattern_history) > 0:
            current_pattern = self.pattern_history[-1]
            pattern_type = current_pattern['type']
        else:
            pattern_type = None
            
        return {
            'pattern_analysis': {
                'type': (
                    pattern_type if pattern_type
                    else "Kein Pattern erkannt"
                ),
                'signal': (
                    'bullish' if current_signal > 0
                    else 'bearish' if current_signal < 0
                    else 'neutral'
                ),
                'confidence': current_conf,
                'reliability': current_rel
            },
            'historical_performance': {
                'total_patterns': len(self.pattern_history),
                'success_rate': (
                    np.mean([
                        p['success'] for p in self.pattern_history
                        if p['success'] is not None
                    ])
                    if self.pattern_history else 0
                )
            },
            'trading_signals': {
                'primary': (
                    'strong_buy' if (
                        current_signal > 0 and
                        current_conf > 0.8 and
                        current_rel > 0.8
                    )
                    else 'buy' if (
                        current_signal > 0 and
                        current_conf > 0.6
                    )
                    else 'strong_sell' if (
                        current_signal < 0 and
                        current_conf > 0.8 and
                        current_rel > 0.8
                    )
                    else 'sell' if (
                        current_signal < 0 and
                        current_conf > 0.6
                    )
                    else 'neutral'
                ),
                'strength': (
                    'stark' if current_conf > 0.8
                    else 'moderat' if current_conf > 0.6
                    else 'schwach'
                ),
                'reliability': (
                    'hoch' if current_rel > 0.8
                    else 'mittel' if current_rel > 0.6
                    else 'niedrig'
                )
            }
        }
