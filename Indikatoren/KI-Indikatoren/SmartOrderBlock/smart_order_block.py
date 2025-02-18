import backtrader as bt
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from collections import deque

class SmartOrderBlock(bt.Indicator):
    """
    Smart Order Block Indicator
    
    Ein KI-gestützter Indikator zur Identifizierung
    und Analyse von Order Blocks.
    
    Features:
    - Order Block Detection
    - Volumenanalyse
    - Block-Klassifizierung
    - Stärkeanalyse
    
    Parameter:
    - block_period (20): Block-Periode
    - min_block_size (5): Minimale Blockgröße
    - strength_threshold (0.7): Stärkeschwelle
    """
    
    lines = ('block_level', 'block_strength',
             'block_volume', 'block_quality',
             'signal')
             
    params = (
        ('block_period', 20),
        ('min_block_size', 5),
        ('strength_threshold', 0.7)
    )
    
    plotlines = dict(
        block_level=dict(color='blue', _name='Block Level'),
        block_strength=dict(color='green', _name='Block Strength'),
        block_volume=dict(color='red', _name='Block Volume'),
        block_quality=dict(color='purple', _name='Block Quality'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(SmartOrderBlock, self).__init__()
        
        # Datenverarbeitung
        self.scaler = StandardScaler()
        self.clusterer = DBSCAN(
            eps=0.3,
            min_samples=self.p.min_block_size
        )
        
        # Block Tracking
        self.price_history = deque(maxlen=self.p.block_period)
        self.volume_history = deque(maxlen=self.p.block_period)
        self.block_history = []
        
    def detect_blocks(self):
        """
        Erkennt Order Blocks im Preischart.
        """
        if len(self.price_history) < self.p.block_period:
            return None, None
            
        # Daten vorbereiten
        prices = np.array(self.price_history).reshape(-1, 1)
        volumes = np.array(self.volume_history).reshape(-1, 1)
        
        # Normalisierung
        scaled_data = self.scaler.fit_transform(
            np.column_stack((prices, volumes))
        )
        
        # Clustering
        labels = self.clusterer.fit_predict(scaled_data)
        
        if len(np.unique(labels)) < 2:
            return None, None
            
        # Blocks identifizieren
        blocks = []
        strengths = []
        
        for label in np.unique(labels):
            if label == -1:  # Noise
                continue
                
            mask = labels == label
            block_prices = prices[mask]
            block_volumes = volumes[mask]
            
            if len(block_prices) >= self.p.min_block_size:
                block_level = np.mean(block_prices)
                block_strength = (
                    np.sum(block_volumes) /
                    np.sum(volumes)
                )
                
                blocks.append(block_level)
                strengths.append(block_strength)
                
        if not blocks:
            return None, None
            
        return blocks, strengths
        
    def analyze_block_volume(self, block_idx):
        """
        Analysiert das Volumen eines Blocks.
        """
        if not self.volume_history:
            return 0
            
        recent_volume = np.mean(
            list(self.volume_history)[-block_idx:]
        )
        avg_volume = np.mean(self.volume_history)
        
        return recent_volume / avg_volume
        
    def calculate_block_quality(self, strength, volume):
        """
        Berechnet die Qualität eines Blocks.
        """
        if strength is None or volume == 0:
            return 0
            
        # Qualität basierend auf Stärke und Volumen
        quality = (strength + (volume / 2)) / 1.5
        
        return quality
        
    def find_nearest_block(self, price, blocks):
        """
        Findet den nächsten Block zum aktuellen Preis.
        """
        if not blocks:
            return None, None
            
        distances = [abs(b - price) for b in blocks]
        nearest_idx = np.argmin(distances)
        
        return blocks[nearest_idx], nearest_idx
        
    def next(self):
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        # Historie aktualisieren
        self.price_history.append(price)
        self.volume_history.append(volume)
        
        # Blocks erkennen
        blocks, strengths = self.detect_blocks()
        
        if blocks is not None and strengths is not None:
            # Nächsten Block finden
            nearest_block, block_idx = self.find_nearest_block(
                price, blocks
            )
            
            if nearest_block is not None:
                # Block-Metriken
                block_strength = strengths[block_idx]
                block_volume = self.analyze_block_volume(
                    block_idx + 1
                )
                block_quality = self.calculate_block_quality(
                    block_strength,
                    block_volume
                )
                
                # Block speichern
                self.block_history.append({
                    'level': nearest_block,
                    'strength': block_strength,
                    'volume': block_volume,
                    'quality': block_quality
                })
                
                # Linien aktualisieren
                self.lines.block_level[0] = nearest_block
                self.lines.block_strength[0] = block_strength
                self.lines.block_volume[0] = block_volume
                self.lines.block_quality[0] = block_quality
                
                # Trading Signal
                if block_quality > self.p.strength_threshold:
                    if price < nearest_block * 0.99:
                        self.lines.signal[0] = 1  # Kaufsignal
                    elif price > nearest_block * 1.01:
                        self.lines.signal[0] = -1  # Verkaufssignal
                    else:
                        self.lines.signal[0] = 0
                else:
                    self.lines.signal[0] = 0
            else:
                # Standardwerte
                self.lines.block_level[0] = price
                self.lines.block_strength[0] = 0
                self.lines.block_volume[0] = 0
                self.lines.block_quality[0] = 0
                self.lines.signal[0] = 0
        else:
            # Standardwerte
            self.lines.block_level[0] = price
            self.lines.block_strength[0] = 0
            self.lines.block_volume[0] = 0
            self.lines.block_quality[0] = 0
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_history = max(
            self.p.block_period,
            len(self.data)
        )
        if len(self.block_history) > max_history:
            self.block_history.pop(0)
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'block_metrics': {
                'level': self.lines.block_level[0],
                'strength': self.lines.block_strength[0],
                'volume': self.lines.block_volume[0],
                'quality': self.lines.block_quality[0]
            },
            'block_analysis': {
                'type': (
                    'demand'
                    if self.lines.block_level[0] <
                       self.data.close[0]
                    else 'supply'
                    if self.lines.block_level[0] >
                       self.data.close[0]
                    else 'neutral'
                ),
                'strength': (
                    'strong'
                    if self.lines.block_strength[0] > 0.7
                    else 'moderate'
                    if self.lines.block_strength[0] > 0.4
                    else 'weak'
                ),
                'volume_profile': (
                    'high'
                    if self.lines.block_volume[0] > 1.2
                    else 'normal'
                    if self.lines.block_volume[0] > 0.8
                    else 'low'
                )
            },
            'quality_analysis': {
                'level': (
                    'high'
                    if self.lines.block_quality[0] > 0.7
                    else 'moderate'
                    if self.lines.block_quality[0] > 0.4
                    else 'low'
                ),
                'reliability': (
                    'reliable'
                    if self.lines.block_quality[0] >
                       self.p.strength_threshold
                    else 'unreliable'
                ),
                'consistency': (
                    'consistent'
                    if len(self.block_history) > 3 and
                    all(abs(b['quality'] -
                           self.lines.block_quality[0]) < 0.2
                        for b in self.block_history[-3:])
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
                    self.lines.block_quality[0] *
                    self.lines.block_strength[0]
                )
            },
            'market_conditions': {
                'block_presence': (
                    'clear'
                    if self.lines.block_strength[0] > 0.5
                    else 'unclear'
                ),
                'volume_support': (
                    'supported'
                    if self.lines.block_volume[0] > 1
                    else 'unsupported'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.block_quality[0] >
                        self.p.strength_threshold and
                        self.lines.block_volume[0] > 1)
                    else 'unfavorable'
                )
            }
        }
