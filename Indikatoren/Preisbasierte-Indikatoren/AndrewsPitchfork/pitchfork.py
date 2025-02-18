import backtrader as bt
import numpy as np

class AndrewsPitchfork(bt.Indicator):
    """
    Andrews Pitchfork
    
    Berechnet die Andrews Pitchfork Linien basierend auf drei Pivotpunkten.
    Unterstützt verschiedene Pitchfork-Varianten und zusätzliche Median Lines.
    
    Der Indikator:
    - Median Line (ML)
    - Upper Parallel (UML)
    - Lower Parallel (LML)
    - Warning Lines
    - Schild Lines
    
    Parameter:
    - method ('standard'): 'standard', 'schiff', 'modified'
    - pivot_period (20): Periode für Pivot-Erkennung
    - warning_levels (True): Warning Lines aktivieren
    - schild_lines (True): Schild Lines aktivieren
    """
    
    lines = ('median_line', 'upper_parallel', 'lower_parallel',
             'warning_upper', 'warning_lower', 'schild_upper', 'schild_lower')
             
    params = (
        ('method', 'standard'),
        ('pivot_period', 20),
        ('warning_levels', True),
        ('schild_lines', True)
    )
    
    plotlines = dict(
        median_line=dict(color='blue', _name='Median'),
        upper_parallel=dict(color='green', _name='Upper'),
        lower_parallel=dict(color='red', _name='Lower'),
        warning_upper=dict(color='orange', _name='Warning Up'),
        warning_lower=dict(color='purple', _name='Warning Down'),
        schild_upper=dict(color='gray', _name='Schild Up'),
        schild_lower=dict(color='darkgray', _name='Schild Down')
    )
    
    def __init__(self):
        super(AndrewsPitchfork, self).__init__()
        
        # Pivot Points
        self.pivot_high = bt.indicators.Highest(
            self.data.high,
            period=self.p.pivot_period
        )
        self.pivot_low = bt.indicators.Lowest(
            self.data.low,
            period=self.p.pivot_period
        )
        
        # Pivot Speicher
        self.pivots = []
        
    def calculate_median_line(self, p0, p1, p2):
        """Berechnet die Median Line basierend auf drei Punkten."""
        # Mittelpunkt zwischen P1 und P2
        mid_point = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
        
        # Steigung der Median Line
        if mid_point[0] - p0[0] != 0:
            slope = (mid_point[1] - p0[1]) / (mid_point[0] - p0[0])
        else:
            slope = float('inf')
            
        return slope, p0
        
    def calculate_parallel_lines(self, slope, p1, p2):
        """Berechnet die parallelen Linien."""
        # Vertikale Distanz zwischen P1 und P2
        distance = abs(p2[1] - p1[1])
        
        # Parallele Linien
        upper_line = (slope, (p1[0], p1[1] + distance))
        lower_line = (slope, (p2[0], p2[1] - distance))
        
        return upper_line, lower_line
        
    def calculate_warning_lines(self, slope, p0, distance):
        """Berechnet die Warning Lines."""
        warning_distance = distance * 0.382  # Fibonacci Ratio
        
        upper = (slope, (p0[0], p0[1] + warning_distance))
        lower = (slope, (p0[0], p0[1] - warning_distance))
        
        return upper, lower
        
    def calculate_schild_lines(self, slope, p0, distance):
        """Berechnet die Schild Lines."""
        schild_distance = distance * 0.618  # Fibonacci Ratio
        
        upper = (slope, (p0[0], p0[1] + schild_distance))
        lower = (slope, (p0[0], p0[1] - schild_distance))
        
        return upper, lower
        
    def calculate_modified_pitchfork(self, p0, p1, p2):
        """Berechnet die modifizierte Pitchfork."""
        # Mittelpunkt zwischen P0 und P1
        mid_p0_p1 = ((p0[0] + p1[0])/2, (p0[1] + p1[1])/2)
        
        # Neue Median Line von mid_p0_p1 zu P2
        if p2[0] - mid_p0_p1[0] != 0:
            slope = (p2[1] - mid_p0_p1[1]) / (p2[0] - mid_p0_p1[0])
        else:
            slope = float('inf')
            
        return slope, mid_p0_p1
        
    def calculate_schiff_pitchfork(self, p0, p1, p2):
        """Berechnet die Schiff Pitchfork."""
        # Mittelpunkt zwischen P1 und P2
        mid_p1_p2 = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
        
        # Steigung von P0 zu mid_p1_p2
        if mid_p1_p2[0] - p0[0] != 0:
            slope = (mid_p1_p2[1] - p0[1]) / (mid_p1_p2[0] - p0[0])
        else:
            slope = float('inf')
            
        return slope, p0
        
    def next(self):
        current_bar = len(self)
        
        # Neue Pivot Points identifizieren
        if self.pivot_high[0] > self.pivot_high[-1]:
            self.pivots.append((current_bar, self.data.high[0], 'high'))
        elif self.pivot_low[0] < self.pivot_low[-1]:
            self.pivots.append((current_bar, self.data.low[0], 'low'))
            
        # Mindestens 3 Pivots benötigt
        if len(self.pivots) < 3:
            return
            
        # Letzte 3 Pivots extrahieren
        p0 = self.pivots[-3][:2]  # Zeit, Preis
        p1 = self.pivots[-2][:2]
        p2 = self.pivots[-1][:2]
        
        # Pitchfork berechnen basierend auf Methode
        if self.p.method == 'schiff':
            slope, base_point = self.calculate_schiff_pitchfork(p0, p1, p2)
        elif self.p.method == 'modified':
            slope, base_point = self.calculate_modified_pitchfork(p0, p1, p2)
        else:  # standard
            slope, base_point = self.calculate_median_line(p0, p1, p2)
            
        # Median Line
        self.lines.median_line[0] = slope * (current_bar - base_point[0]) + \
                                   base_point[1]
                                   
        # Parallele Linien
        upper, lower = self.calculate_parallel_lines(slope, p1, p2)
        self.lines.upper_parallel[0] = slope * (current_bar - upper[1][0]) + \
                                     upper[1][1]
        self.lines.lower_parallel[0] = slope * (current_bar - lower[1][0]) + \
                                     lower[1][1]
                                     
        # Warning Lines
        if self.p.warning_levels:
            distance = abs(p2[1] - p1[1])
            warning_up, warning_down = self.calculate_warning_lines(
                slope, base_point, distance
            )
            self.lines.warning_upper[0] = slope * \
                                        (current_bar - warning_up[1][0]) + \
                                        warning_up[1][1]
            self.lines.warning_lower[0] = slope * \
                                        (current_bar - warning_down[1][0]) + \
                                        warning_down[1][1]
        else:
            self.lines.warning_upper[0] = float('nan')
            self.lines.warning_lower[0] = float('nan')
            
        # Schild Lines
        if self.p.schild_lines:
            distance = abs(p2[1] - p1[1])
            schild_up, schild_down = self.calculate_schild_lines(
                slope, base_point, distance
            )
            self.lines.schild_upper[0] = slope * \
                                       (current_bar - schild_up[1][0]) + \
                                       schild_up[1][1]
            self.lines.schild_lower[0] = slope * \
                                       (current_bar - schild_down[1][0]) + \
                                       schild_down[1][1]
        else:
            self.lines.schild_upper[0] = float('nan')
            self.lines.schild_lower[0] = float('nan')
