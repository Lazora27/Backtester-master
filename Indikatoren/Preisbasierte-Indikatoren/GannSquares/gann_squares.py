import backtrader as bt
import numpy as np

class GannSquares(bt.Indicator):
    """
    Gann Squares
    
    Berechnet Gann Square Levels basierend auf einem Pivot-Punkt.
    Implementiert Gann's Konzept der Preis-Zeit-Beziehung.
    
    Der Indikator:
    - Berechnet Gann Square of 9 Levels
    - Identifiziert kritische Preis-Zeit-Punkte
    - Unterstützt Natural Squares und Square Roots
    
    Parameter:
    - pivot_point (None): Manueller Pivot-Punkt (Preis, Zeit)
    - period (20): Periode für automatische Pivot-Erkennung
    - square_type ('9'): '4', '9', '16', '25', '49', '100'
    """
    
    lines = ('square_levels', 'cardinal_levels', 'time_levels')
    params = (
        ('pivot_point', None),  # (price, time) Tuple
        ('period', 20),
        ('square_type', '9')
    )
    
    plotlines = dict(
        square_levels=dict(color='darkblue', _name='Square'),
        cardinal_levels=dict(color='red', _name='Cardinal'),
        time_levels=dict(color='green', _name='Time')
    )
    
    def __init__(self):
        super(GannSquares, self).__init__()
        
        # Square Größe
        self.square_size = int(self.p.square_type)
        
        if self.p.pivot_point is not None:
            self.pivot_price, self.pivot_time = self.p.pivot_point
        else:
            # Automatische Pivot-Erkennung
            self.pivot_price = bt.indicators.Lowest(
                self.data.low,
                period=self.p.period
            )
            self.pivot_time = len(self) - self.p.period
            
        # Gann Numbers
        self.gann_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.cardinal_numbers = [0, 90, 180, 270, 360]
        
    def calculate_square_level(self, number):
        """Berechnet ein Square Level basierend auf einer Zahl."""
        square_root = np.sqrt(number)
        return self.pivot_price * square_root
        
    def calculate_cardinal_level(self, angle):
        """Berechnet ein Cardinal Level basierend auf einem Winkel."""
        return self.pivot_price * (1 + np.sin(np.radians(angle)))
        
    def calculate_time_level(self, number):
        """Berechnet ein Zeit-Level basierend auf einer Zahl."""
        return self.pivot_time + (number * self.square_size)
        
    def next(self):
        # Square Levels
        square_levels = [self.calculate_square_level(n) for n in self.gann_numbers]
        self.lines.square_levels[0] = np.mean(square_levels)
        
        # Cardinal Levels
        cardinal_levels = [self.calculate_cardinal_level(a) 
                         for a in self.cardinal_numbers]
        self.lines.cardinal_levels[0] = np.mean(cardinal_levels)
        
        # Zeit Levels
        current_bar = len(self)
        time_levels = [self.calculate_time_level(n) for n in self.gann_numbers]
        if current_bar in time_levels:
            self.lines.time_levels[0] = self.data.close[0]
        else:
            self.lines.time_levels[0] = float('nan')
            
class GannSquareReversal(bt.Indicator):
    """
    Gann Square Reversal
    
    Identifiziert potenzielle Wendepunkte basierend auf Gann Square Levels.
    
    Parameter:
    - period (20): Berechnungsperiode
    - threshold (0.1): Schwellenwert für Wendepunkte
    """
    
    lines = ('reversal_points', 'strength')
    params = (
        ('period', 20),
        ('threshold', 0.1)
    )
    
    plotlines = dict(
        reversal_points=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_0=0.0, color='green'),
            _fill_lt=dict(_0=0.0, color='red'),
        ),
        strength=dict(color='blue', _name='Strength')
    )
    
    def __init__(self):
        # Gann Squares
        self.squares = GannSquares(
            self.data,
            period=self.p.period
        )
        
        # Preisabstand zu Square Levels
        price_diff = abs(self.data.close - self.squares.square_levels)
        norm_diff = price_diff / self.data.close
        
        # Wendepunkte identifizieren
        self.lines.reversal_points = norm_diff < self.p.threshold
        
        # Stärke der Wendepunkte
        self.lines.strength = 1.0 - norm_diff
