import backtrader as bt
import numpy as np

class GannFans(bt.Indicator):
    """
    Gann Fans
    
    Berechnet Gann-Fan-Linien basierend auf einem Pivot-Punkt. Die Linien
    repräsentieren verschiedene Steigungswinkel nach Gann's Theorie.
    
    Der Indikator:
    - Berechnet 1x1, 2x1, 3x1, 4x1, 8x1 Aufwärtslinien
    - Berechnet 1x2, 1x3, 1x4, 1x8 Abwärtslinien
    - Unterstützt automatische Pivot-Erkennung
    
    Parameter:
    - pivot_point (None): Manueller Pivot-Punkt (Preis, Zeit)
    - period (20): Periode für automatische Pivot-Erkennung
    - price_unit (1.0): Einheit für Preisskalierung
    """
    
    lines = ('up_1x1', 'up_2x1', 'up_3x1', 'up_4x1', 'up_8x1',
             'down_1x2', 'down_1x3', 'down_1x4', 'down_1x8')
             
    params = (
        ('pivot_point', None),  # (price, time) Tuple
        ('period', 20),
        ('price_unit', 1.0)
    )
    
    plotlines = dict(
        up_1x1=dict(color='darkblue', _name='1x1'),
        up_2x1=dict(color='blue', _name='2x1'),
        up_3x1=dict(color='green', _name='3x1'),
        up_4x1=dict(color='darkgreen', _name='4x1'),
        up_8x1=dict(color='red', _name='8x1'),
        down_1x2=dict(color='orange', _name='1x2'),
        down_1x3=dict(color='yellow', _name='1x3'),
        down_1x4=dict(color='purple', _name='1x4'),
        down_1x8=dict(color='gray', _name='1x8')
    )
    
    def __init__(self):
        super(GannFans, self).__init__()
        
        if self.p.pivot_point is not None:
            self.pivot_price, self.pivot_time = self.p.pivot_point
        else:
            # Automatische Pivot-Erkennung
            self.pivot_price = bt.indicators.Lowest(
                self.data.low,
                period=self.p.period
            )
            self.pivot_time = len(self) - self.p.period
            
        # Gann-Winkel (in Grad)
        self.angles = {
            'up_1x1': 45,    # 1:1
            'up_2x1': 63.43, # 2:1
            'up_3x1': 71.57, # 3:1
            'up_4x1': 75.96, # 4:1
            'up_8x1': 82.87, # 8:1
            'down_1x2': 26.57, # 1:2
            'down_1x3': 18.43, # 1:3
            'down_1x4': 14.04, # 1:4
            'down_1x8': 7.13   # 1:8
        }
        
    def next(self):
        current_bar = len(self)
        time_diff = current_bar - self.pivot_time
        
        for line_name, angle in self.angles.items():
            # Berechne Steigung basierend auf Winkel
            slope = np.tan(np.radians(angle))
            
            # Skaliere Steigung mit Preiseinheit
            scaled_slope = slope * self.p.price_unit
            
            # Berechne Linienwert
            if line_name.startswith('up'):
                self.lines[line_name][0] = self.pivot_price + \
                                         scaled_slope * time_diff
            else:
                self.lines[line_name][0] = self.pivot_price - \
                                         scaled_slope * time_diff
                                         
class GannAngles(bt.Indicator):
    """
    Gann Angles
    
    Berechnet den aktuellen Winkel der Preisbewegung relativ zu
    Gann's kritischen Winkeln.
    
    Parameter:
    - period (20): Berechnungsperiode
    - normalize (True): Ob die Winkel normalisiert werden sollen
    """
    
    lines = ('angle', 'critical_angle')
    params = (
        ('period', 20),
        ('normalize', True)
    )
    
    plotlines = dict(
        angle=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_45=0.0, color='green'),
            _fill_lt=dict(_45=0.0, color='red'),
        ),
        critical_angle=dict(color='blue', _name='Critical')
    )
    
    def __init__(self):
        # Preisänderung
        price_change = self.data.close - self.data.close(-self.p.period)
        
        # Zeit ist immer period Bars
        time_change = self.p.period
        
        # Winkel berechnen
        self.lines.angle = bt.DivByZero(
            price_change,
            time_change,
            zero=0.0
        )
        
        if self.p.normalize:
            self.lines.angle = np.degrees(np.arctan(self.lines.angle))
            
        # Kritischer 45-Grad Winkel
        self.lines.critical_angle = 45.0
