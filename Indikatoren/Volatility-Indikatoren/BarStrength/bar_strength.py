import backtrader as bt
import numpy as np

class BarStrength(bt.Indicator):
    """
    Bar Strength Indicator
    
    Ein Volatilitätsindikator, der die Stärke einzelner Preisbalken
    basierend auf mehreren Faktoren analysiert.
    
    Features:
    - Preisbereichsanalyse
    - Volumengewichtung
    - Trendstärkeberechnung
    - Relative Stärkebestimmung
    
    Parameter:
    - period (14): Analysezeitraum
    - volume_factor (0.5): Volumengewichtung
    - strength_threshold (0.7): Stärkeschwelle
    """
    
    lines = ('bar_strength', 'relative_strength',
             'trend_strength', 'volume_impact',
             'strength_signal')
             
    params = (
        ('period', 14),
        ('volume_factor', 0.5),
        ('strength_threshold', 0.7)
    )
    
    plotlines = dict(
        bar_strength=dict(color='blue', _name='Bar Strength'),
        relative_strength=dict(color='red', _name='Relative Strength'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volume_impact=dict(color='purple', _name='Volume Impact'),
        strength_signal=dict(color='orange', _name='Strength Signal')
    )
    
    def __init__(self):
        super(BarStrength, self).__init__()
        
        # Historie
        self.strength_history = []
        self.volume_history = []
        
    def calculate_bar_strength(self):
        """
        Berechnet die Balkenstärke.
        """
        if len(self.data) < 2:
            return 0
            
        # Preisbereich
        price_range = self.data.high[0] - self.data.low[0]
        
        # Schlusskursposition
        if price_range > 0:
            close_position = (
                (self.data.close[0] - self.data.low[0]) /
                price_range
            )
        else:
            close_position = 0.5
            
        # Volumeneinfluss
        if len(self.volume_history) > 0:
            volume_ratio = (
                self.data.volume[0] /
                np.mean(self.volume_history)
                if np.mean(self.volume_history) > 0
                else 1.0
            )
        else:
            volume_ratio = 1.0
            
        # Balkenstärke
        strength = (
            close_position * (1 - self.p.volume_factor) +
            volume_ratio * self.p.volume_factor
        )
        
        return strength
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.data) < 2:
            return 0
            
        # Preisänderung
        price_change = (
            self.data.close[0] - self.data.close[-1]
        ) / self.data.close[-1] if self.data.close[-1] != 0 else 0
        
        # Stärkeänderung
        strength_change = (
            self.lines.bar_strength[0] - self.lines.bar_strength[-1]
        ) if len(self.strength_history) > 1 else 0
        
        return price_change * strength_change
        
    def next(self):
        # Balkenstärke berechnen
        self.lines.bar_strength[0] = self.calculate_bar_strength()
        self.strength_history.append(self.lines.bar_strength[0])
        
        # Relative Stärke
        if len(self.strength_history) >= self.p.period:
            mean_strength = np.mean(self.strength_history[-self.p.period:])
            std_strength = np.std(self.strength_history[-self.p.period:])
            
            self.lines.relative_strength[0] = (
                (self.lines.bar_strength[0] - mean_strength) /
                std_strength if std_strength != 0 else 0
            )
        else:
            self.lines.relative_strength[0] = 0
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volumeneinfluss
        if len(self.volume_history) > 0:
            self.lines.volume_impact[0] = (
                self.data.volume[0] /
                np.mean(self.volume_history)
                if np.mean(self.volume_history) > 0
                else 1.0
            )
        else:
            self.lines.volume_impact[0] = 1.0
            
        # Stärkesignal
        self.lines.strength_signal[0] = (
            1 if self.lines.relative_strength[0] > self.p.strength_threshold
            else -1 if self.lines.relative_strength[0] < -self.p.strength_threshold
            else 0
        )
        
        # Historie aktualisieren
        self.volume_history.append(self.data.volume[0])
        
        # Historie begrenzen
        max_period = self.p.period
        for hist in [self.strength_history, self.volume_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'strength': {
                'current': self.lines.bar_strength[0],
                'relative': self.lines.relative_strength[0],
                'trend': self.lines.trend_strength[0],
                'volume_impact': self.lines.volume_impact[0]
            },
            'signal': {
                'value': self.lines.strength_signal[0],
                'type': (
                    'strong' if self.lines.strength_signal[0] > 0
                    else 'weak' if self.lines.strength_signal[0] < 0
                    else 'neutral'
                ),
                'confidence': abs(self.lines.relative_strength[0])
            },
            'trend': {
                'direction': (
                    'up' if self.lines.trend_strength[0] > 0
                    else 'down'
                ),
                'strength': abs(self.lines.trend_strength[0]),
                'persistence': (
                    np.mean([
                        1 if s > 0 else -1
                        for s in self.strength_history[-5:]
                    ]) if len(self.strength_history) >= 5
                    else 0
                )
            },
            'volume': {
                'impact': self.lines.volume_impact[0],
                'trend': (
                    'increasing' if self.lines.volume_impact[0] > 1
                    else 'decreasing'
                ),
                'significance': (
                    self.p.volume_factor * self.lines.volume_impact[0]
                )
            },
            'risk': {
                'current': abs(self.lines.relative_strength[0]),
                'trend_risk': abs(self.lines.trend_strength[0]),
                'volume_risk': (
                    1 - (1 / self.lines.volume_impact[0])
                    if self.lines.volume_impact[0] > 0
                    else 0
                )
            }
        }
