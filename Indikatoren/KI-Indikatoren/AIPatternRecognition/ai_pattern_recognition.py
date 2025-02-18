import backtrader as bt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
from collections import defaultdict

class AIPatternRecognition(bt.Indicator):
    """
    AI Pattern Recognition Indicator
    
    Ein fortgeschrittener KI-basierter Indikator zur
    Erkennung von Preismustern.
    
    Features:
    - KI-gestützte Mustererkennung
    - Dimensionsreduktion
    - Clustering-Analyse
    - Signalgenerierung
    
    Parameter:
    - pattern_length (20): Musterlänge
    - min_confidence (0.7): Minimale Konfidenz
    - cluster_eps (0.3): Clustering-Epsilon
    """
    
    lines = ('pattern_score', 'pattern_confidence',
             'cluster_strength', 'recognition_quality',
             'signal')
             
    params = (
        ('pattern_length', 20),
        ('min_confidence', 0.7),
        ('cluster_eps', 0.3)
    )
    
    plotlines = dict(
        pattern_score=dict(color='blue', _name='Pattern Score'),
        pattern_confidence=dict(color='red', _name='Pattern Confidence'),
        cluster_strength=dict(color='green', _name='Cluster Strength'),
        recognition_quality=dict(color='purple', _name='Recognition Quality'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(AIPatternRecognition, self).__init__()
        
        # KI-Komponenten
        self.scaler = StandardScaler()
        self.pca = PCA(n_components=2)
        self.clusterer = DBSCAN(
            eps=self.p.cluster_eps,
            min_samples=5
        )
        
        # Pattern Tracking
        self.price_history = []
        self.pattern_history = []
        self.cluster_history = []
        self.confidence_history = []
        
    def extract_features(self):
        """
        Extrahiert Features aus den Preisdaten.
        """
        if len(self.price_history) < self.p.pattern_length:
            return None
            
        # Preismuster extrahieren
        pattern = self.price_history[-self.p.pattern_length:]
        pattern = np.array(pattern).reshape(1, -1)
        
        # Normalisierung
        pattern_scaled = self.scaler.fit_transform(pattern)
        
        # Dimensionsreduktion
        pattern_reduced = self.pca.fit_transform(
            pattern_scaled
        )
        
        return pattern_reduced
        
    def recognize_pattern(self, features):
        """
        Erkennt Muster in den Features.
        """
        if features is None:
            return 0, 0
            
        # Clustering durchführen
        clusters = self.clusterer.fit_predict(features)
        
        # Clusterstärke berechnen
        n_clusters = len(set(clusters)) - (
            1 if -1 in clusters else 0
        )
        
        if n_clusters == 0:
            return 0, 0
            
        # Konfidenz berechnen
        confidence = 1 - (
            np.sum(clusters == -1) / len(clusters)
        )
        
        return n_clusters, confidence
        
    def calculate_pattern_score(self, n_clusters, confidence):
        """
        Berechnet den Pattern-Score.
        """
        if n_clusters == 0:
            return 0
            
        # Score basierend auf Clusters und Konfidenz
        base_score = n_clusters * confidence
        
        # Historie berücksichtigen
        if self.pattern_history:
            historical_avg = np.mean(self.pattern_history)
            score = (base_score + historical_avg) / 2
        else:
            score = base_score
            
        self.pattern_history.append(score)
        return score
        
    def calculate_cluster_strength(self, n_clusters):
        """
        Berechnet die Cluster-Stärke.
        """
        if n_clusters == 0:
            return 0
            
        # Stärke basierend auf Cluster-Anzahl
        strength = n_clusters / self.p.pattern_length
        self.cluster_history.append(strength)
        
        return strength
        
    def calculate_recognition_quality(self, confidence):
        """
        Berechnet die Erkennungsqualität.
        """
        if confidence == 0:
            return 0
            
        # Qualität basierend auf Konfidenz
        quality = confidence
        if self.confidence_history:
            historical_avg = np.mean(
                self.confidence_history
            )
            quality = (confidence + historical_avg) / 2
            
        self.confidence_history.append(quality)
        return quality
        
    def next(self):
        # Preis speichern
        price = self.data.close[0]
        self.price_history.append(price)
        
        # Features extrahieren
        features = self.extract_features()
        
        # Muster erkennen
        n_clusters, confidence = self.recognize_pattern(
            features
        )
        
        # Metriken berechnen
        pattern_score = self.calculate_pattern_score(
            n_clusters, confidence
        )
        pattern_confidence = confidence
        cluster_strength = self.calculate_cluster_strength(
            n_clusters
        )
        recognition_quality = self.calculate_recognition_quality(
            confidence
        )
        
        # Linien aktualisieren
        self.lines.pattern_score[0] = pattern_score
        self.lines.pattern_confidence[0] = pattern_confidence
        self.lines.cluster_strength[0] = cluster_strength
        self.lines.recognition_quality[0] = recognition_quality
        
        # Signal
        if recognition_quality > self.p.min_confidence:
            if (pattern_score > 0.5 and
                cluster_strength > 0.3):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (pattern_score < -0.5 and
                  cluster_strength > 0.3):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_length = max(
            self.p.pattern_length,
            len(self.data)
        )
        for hist in [self.price_history,
                    self.pattern_history,
                    self.cluster_history,
                    self.confidence_history]:
            if len(hist) > max_length:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'pattern_metrics': {
                'score': self.lines.pattern_score[0],
                'confidence': self.lines.pattern_confidence[0],
                'strength': self.lines.cluster_strength[0],
                'quality': self.lines.recognition_quality[0]
            },
            'pattern_analysis': {
                'type': (
                    'strong'
                    if self.lines.pattern_score[0] > 0.7
                    else 'moderate'
                    if self.lines.pattern_score[0] > 0.4
                    else 'weak'
                ),
                'reliability': (
                    'high'
                    if self.lines.pattern_confidence[0] >
                       self.p.min_confidence
                    else 'low'
                ),
                'consistency': (
                    'consistent'
                    if len(self.pattern_history) > 1 and
                    all(p > 0.5 for p in self.pattern_history[-3:])
                    else 'inconsistent'
                )
            },
            'cluster_analysis': {
                'strength': self.lines.cluster_strength[0],
                'quality': (
                    'high'
                    if self.lines.cluster_strength[0] > 0.7
                    else 'moderate'
                    if self.lines.cluster_strength[0] > 0.4
                    else 'low'
                ),
                'stability': (
                    'stable'
                    if len(self.cluster_history) > 1 and
                    np.std(self.cluster_history[-5:]) < 0.2
                    else 'volatile'
                )
            },
            'recognition_analysis': {
                'quality': (
                    'high'
                    if self.lines.recognition_quality[0] > 0.8
                    else 'moderate'
                    if self.lines.recognition_quality[0] > 0.5
                    else 'low'
                ),
                'confidence': (
                    'confident'
                    if self.lines.pattern_confidence[0] >
                       self.p.min_confidence
                    else 'uncertain'
                ),
                'reliability': (
                    self.lines.recognition_quality[0] *
                    self.lines.pattern_confidence[0]
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
                    self.lines.recognition_quality[0] *
                    self.lines.cluster_strength[0]
                )
            },
            'market_conditions': {
                'pattern_quality': (
                    'high'
                    if self.lines.pattern_score[0] > 0.7
                    else 'moderate'
                    if self.lines.pattern_score[0] > 0.4
                    else 'low'
                ),
                'recognition_state': (
                    'reliable'
                    if self.lines.recognition_quality[0] >
                       self.p.min_confidence
                    else 'unreliable'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.recognition_quality[0] >
                        self.p.min_confidence and
                        self.lines.cluster_strength[0] > 0.3)
                    else 'unfavorable'
                )
            }
        }
