import backtrader as bt
import numpy as np
from datetime import datetime, timedelta

class GannAngles(bt.Indicator):
    """
    Gann Angles Indicator
    
    Ein fortgeschrittener geometrischer Indikator basierend auf W.D. Ganns
    Theorie der Zeit-Preis-Beziehungen.
    
    Features:
    - Klassische Gann Winkel (1x1, 2x1, 3x1, 4x1, 8x1)
    - Dynamische Pivot-Punkt Erkennung
    - Zeit-Preis-Quadrat Analyse
    - Support/Resistance Levels
    - Trend-Stärke Berechnung
    
    Parameter:
    - base_period (20): Basisperiode für Berechnungen
    - pivot_lookback (50): Rückblickperiode für Pivot-Punkte
    - angle_sensitivity (0.1): Sensitivität für Winkelberechnungen
    - time_factor (1.0): Zeitfaktor für Gann-Quadrat
    - price_factor (1.0): Preisfaktor für Gann-Quadrat
    """
    
    lines = ('gann_1x1', 'gann_2x1', 'gann_3x1', 'gann_4x1', 'gann_8x1',
             'support', 'resistance', 'trend_strength',
             'price_target', 'time_target',
             'buy_signal', 'sell_signal')
             
    params = (
        ('base_period', 20),
        ('pivot_lookback', 50),
        ('angle_sensitivity', 0.1),
        ('time_factor', 1.0),
        ('price_factor', 1.0)
    )
    
    plotlines = dict(
        gann_1x1=dict(color='blue', _name='1x1 Angle'),
        gann_2x1=dict(color='green', _name='2x1 Angle'),
        gann_3x1=dict(color='red', _name='3x1 Angle'),
        gann_4x1=dict(color='purple', _name='4x1 Angle'),
        gann_8x1=dict(color='orange', _name='8x1 Angle'),
        support=dict(color='gray', _name='Support'),
        resistance=dict(color='gray', _name='Resistance'),
        trend_strength=dict(color='brown', _name='Trend Strength'),
        price_target=dict(_name='Price Target', color='blue', marker='o'),
        time_target=dict(_name='Time Target', color='green', marker='s'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(GannAngles, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.ema = bt.indicators.EMA(period=20)
        
        # Historie
        self.price_history = []
        self.time_history = []
        self.pivot_points = []
        
    def calculate_gann_angle(self, angle_type):
        """
        Berechnet Gann Winkel basierend auf Typ.
        
        Parameter:
        - angle_type: Winkeltyp (1x1, 2x1, etc.)
        """
        if len(self.price_history) < 2:
            return self.data[0]
            
        base_price = self.pivot_points[-1][1] if self.pivot_points else self.price_history[0]
        time_diff = len(self.price_history) - 1
        
        # Winkel-Faktoren
        angle_factors = {
            '1x1': 1.0,
            '2x1': 2.0,
            '3x1': 3.0,
            '4x1': 4.0,
            '8x1': 8.0
        }
        
        factor = angle_factors.get(angle_type, 1.0)
        angle_value = base_price + (time_diff * self.p.price_factor * factor)
        
        return angle_value
        
    def find_pivot_points(self):
        """
        Identifiziert wichtige Pivot-Punkte im Preisverlauf.
        """
        if len(self.price_history) < self.p.pivot_lookback:
            return
            
        window = self.price_history[-self.p.pivot_lookback:]
        
        # Lokale Maxima und Minima
        for i in range(2, len(window)-2):
            # Hoch
            if (window[i] > window[i-1] and
                window[i] > window[i-2] and
                window[i] > window[i+1] and
                window[i] > window[i+2]):
                self.pivot_points.append(
                    (len(self.price_history)-self.p.pivot_lookback+i,
                     window[i], 'high')
                )
                
            # Tief
            if (window[i] < window[i-1] and
                window[i] < window[i-2] and
                window[i] < window[i+1] and
                window[i] < window[i+2]):
                self.pivot_points.append(
                    (len(self.price_history)-self.p.pivot_lookback+i,
                     window[i], 'low')
                )
                
        # Historie begrenzen
        if len(self.pivot_points) > 10:
            self.pivot_points = self.pivot_points[-10:]
            
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke basierend auf Gann Winkeln.
        """
        if len(self.price_history) < self.p.base_period:
            return 0
            
        current_price = self.data[0]
        gann_1x1 = self.lines.gann_1x1[0]
        
        # Abweichung vom 1x1 Winkel
        deviation = abs(current_price - gann_1x1)
        normalized_dev = deviation / (self.atr[0] if self.atr[0] != 0 else 1)
        
        # Trendstärke (0-1)
        strength = 1 / (1 + normalized_dev)
        
        return strength
        
    def calculate_price_targets(self):
        """
        Berechnet Preis-Ziele basierend auf Gann-Quadrat.
        """
        if not self.pivot_points:
            return None
            
        last_pivot = self.pivot_points[-1]
        time_diff = len(self.price_history) - last_pivot[0]
        
        # Gann Preis-Projektion
        price_target = last_pivot[1] + (
            time_diff * self.p.price_factor *
            (2 if last_pivot[2] == 'low' else -2)
        )
        
        return price_target
        
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.data[0])
        self.time_history.append(len(self))
        
        # Pivot-Punkte aktualisieren
        self.find_pivot_points()
        
        # Gann Winkel berechnen
        self.lines.gann_1x1[0] = self.calculate_gann_angle('1x1')
        self.lines.gann_2x1[0] = self.calculate_gann_angle('2x1')
        self.lines.gann_3x1[0] = self.calculate_gann_angle('3x1')
        self.lines.gann_4x1[0] = self.calculate_gann_angle('4x1')
        self.lines.gann_8x1[0] = self.calculate_gann_angle('8x1')
        
        # Support/Resistance
        if self.pivot_points:
            recent_pivots = sorted([p[1] for p in self.pivot_points[-3:]])
            self.lines.support[0] = min(recent_pivots)
            self.lines.resistance[0] = max(recent_pivots)
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Preis-Ziele
        price_target = self.calculate_price_targets()
        if price_target is not None:
            self.lines.price_target[0] = price_target
            self.lines.time_target[0] = len(self) + self.p.base_period
        else:
            self.lines.price_target[0] = float('nan')
            self.lines.time_target[0] = float('nan')
            
        # Signal-Generierung
        current_price = self.data[0]
        
        # Buy Signal
        if (current_price > self.lines.gann_1x1[0] and
            self.lines.trend_strength[0] > 0.7):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (current_price < self.lines.gann_1x1[0] and
            self.lines.trend_strength[0] > 0.7):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'gann_angles': {
                '1x1': self.lines.gann_1x1[0],
                '2x1': self.lines.gann_2x1[0],
                '3x1': self.lines.gann_3x1[0],
                '4x1': self.lines.gann_4x1[0],
                '8x1': self.lines.gann_8x1[0]
            },
            'levels': {
                'support': self.lines.support[0],
                'resistance': self.lines.resistance[0],
                'price_target': self.lines.price_target[0]
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': ('up' if self.data[0] > self.lines.gann_1x1[0]
                            else 'down'),
                'angle_alignment': sum(1 for x in [
                    self.lines.gann_1x1[0],
                    self.lines.gann_2x1[0],
                    self.lines.gann_3x1[0]
                ] if self.data[0] > x) / 3
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'target_hit': (
                    abs(self.data[0] - self.lines.price_target[0]) <
                    self.atr[0] if self.atr[0] != 0 else False
                )
            },
            'time_analysis': {
                'current_square': len(self) % self.p.base_period,
                'next_target': self.lines.time_target[0],
                'pivot_count': len(self.pivot_points)
            }
        }
