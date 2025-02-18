import backtrader as bt
import numpy as np
from datetime import timedelta

class WolfeWaves(bt.Indicator):
    """
    Wolfe Waves Pattern Detector
    
    Identifiziert potenzielle Wolfe Wave Muster im Chart.
    Ein Wolfe Wave ist ein natürliches Handelsmuster, das aus 5 Wellen besteht
    und symmetrische Zeit- und Preisprojektionen aufweist.
    
    Der Indikator:
    - Erkennt 1-2-3-4-5 Wellenmuster
    - Berechnet Zeitsymmetrie
    - Projiziert Punkt 6 (Preisziel)
    - Bewertet Musterqualität
    
    Parameter:
    - min_wave_length (5): Minimale Länge einer Welle
    - max_wave_length (50): Maximale Länge einer Welle
    - symmetry_tolerance (0.2): Toleranz für Zeitsymmetrie
    - price_tolerance (0.1): Toleranz für Preissymmetrie
    """
    
    lines = ('wave_1', 'wave_2', 'wave_3', 'wave_4', 'wave_5',
             'target_6', 'pattern_quality')
             
    params = (
        ('min_wave_length', 5),
        ('max_wave_length', 50),
        ('symmetry_tolerance', 0.2),
        ('price_tolerance', 0.1)
    )
    
    plotlines = dict(
        wave_1=dict(color='blue', _name='Wave 1'),
        wave_2=dict(color='green', _name='Wave 2'),
        wave_3=dict(color='red', _name='Wave 3'),
        wave_4=dict(color='purple', _name='Wave 4'),
        wave_5=dict(color='orange', _name='Wave 5'),
        target_6=dict(color='black', _name='Target 6'),
        pattern_quality=dict(_name='Quality', color='gray')
    )
    
    def __init__(self):
        super(WolfeWaves, self).__init__()
        
        # Swing High/Low Punkte
        self.highs = bt.indicators.Highest(self.data.high,
                                         period=self.p.min_wave_length)
        self.lows = bt.indicators.Lowest(self.data.low,
                                       period=self.p.min_wave_length)
                                       
        # Wave Points Speicher
        self.wave_points = []
        self.current_pattern = None
        
    def is_valid_wave_length(self, length):
        """Überprüft ob die Wellenlänge im gültigen Bereich liegt."""
        return self.p.min_wave_length <= length <= self.p.max_wave_length
        
    def is_time_symmetric(self, wave1_time, wave2_time):
        """Überprüft die Zeitsymmetrie zwischen zwei Wellen."""
        ratio = abs(wave2_time / wave1_time - 1)
        return ratio <= self.p.symmetry_tolerance
        
    def is_price_symmetric(self, wave1_price, wave2_price):
        """Überprüft die Preissymmetrie zwischen zwei Wellen."""
        ratio = abs(wave2_price / wave1_price - 1)
        return ratio <= self.p.price_tolerance
        
    def calculate_target_6(self):
        """Berechnet das Preisziel (Punkt 6) basierend auf dem Muster."""
        if len(self.wave_points) < 5:
            return None
            
        # Zeit- und Preisdifferenzen
        time_1_3 = self.wave_points[2][0] - self.wave_points[0][0]
        time_3_5 = self.wave_points[4][0] - self.wave_points[2][0]
        
        # Projektion für Punkt 6
        target_time = self.wave_points[4][0] + time_1_3
        price_range = self.wave_points[4][1] - self.wave_points[2][1]
        target_price = self.wave_points[4][1] + price_range
        
        return target_time, target_price
        
    def calculate_pattern_quality(self):
        """Bewertet die Qualität des Wolfe Wave Musters."""
        if len(self.wave_points) < 5:
            return 0.0
            
        # Zeit- und Preissymmetrie
        time_symmetry = self.is_time_symmetric(
            self.wave_points[2][0] - self.wave_points[0][0],
            self.wave_points[4][0] - self.wave_points[2][0]
        )
        
        price_symmetry = self.is_price_symmetric(
            self.wave_points[2][1] - self.wave_points[0][1],
            self.wave_points[4][1] - self.wave_points[2][1]
        )
        
        # Gesamtqualität
        quality = (time_symmetry + price_symmetry) / 2.0
        return quality
        
    def next(self):
        current_bar = len(self)
        
        # Neue Swing Points identifizieren
        if self.highs[0] > self.highs[-1]:
            self.wave_points.append((current_bar, self.data.high[0]))
        elif self.lows[0] < self.lows[-1]:
            self.wave_points.append((current_bar, self.data.low[0]))
            
        # Alte Punkte entfernen
        while (len(self.wave_points) > 0 and
               current_bar - self.wave_points[0][0] > self.p.max_wave_length):
            self.wave_points.pop(0)
            
        # Pattern analysieren
        if len(self.wave_points) >= 5:
            # Wave Points setzen
            for i in range(5):
                getattr(self.lines, f'wave_{i+1}')[0] = self.wave_points[i][1]
                
            # Ziel berechnen
            target = self.calculate_target_6()
            if target:
                self.lines.target_6[0] = target[1]
            else:
                self.lines.target_6[0] = float('nan')
                
            # Qualität berechnen
            self.lines.pattern_quality[0] = self.calculate_pattern_quality()
        else:
            # Keine vollständiges Muster
            for i in range(5):
                getattr(self.lines, f'wave_{i+1}')[0] = float('nan')
            self.lines.target_6[0] = float('nan')
            self.lines.pattern_quality[0] = 0.0
