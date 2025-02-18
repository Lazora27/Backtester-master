import backtrader as bt
import numpy as np

class FibonacciVolumeRatio(bt.Indicator):
    """
    Fibonacci Volume Ratio
    
    Ein Indikator, der Volumenbeziehungen basierend auf
    Fibonacci-Verhältnissen analysiert.
    
    Features:
    - Fibonacci-Volumenanalyse
    - Trendbestätigung
    - Volumenzyklen-Erkennung
    - Marktstruktur-Analyse
    - Signal-Validierung
    
    Parameter:
    - period (21): Basisperiode
    - fib_levels (3): Anzahl der Fibonacci-Niveaus
    - volume_factor (1.0): Volumenfaktor
    """
    
    lines = ('fib_ratio', 'smoothed_ratio',
             'cycle_phase', 'trend_strength',
             'volume_structure', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 21),
        ('fib_levels', 3),
        ('volume_factor', 1.0),
        ('min_trend_strength', 0.3)
    )
    
    plotlines = dict(
        fib_ratio=dict(color='blue', _name='Fib Ratio'),
        smoothed_ratio=dict(color='red', _name='Smoothed Ratio'),
        cycle_phase=dict(color='purple', _name='Cycle Phase'),
        trend_strength=dict(color='orange', _name='Trend Strength'),
        volume_structure=dict(color='green', _name='Volume Structure'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(FibonacciVolumeRatio, self).__init__()
        
        # Fibonacci-Sequenz generieren
        self.fib_sequence = self.generate_fibonacci(self.p.fib_levels)
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.ratio_history = []
        self.volume_history = []
        self.phase_history = []
        
    def generate_fibonacci(self, levels):
        """
        Generiert Fibonacci-Sequenz.
        """
        fib = [1, 1]
        for i in range(2, levels + 2):
            fib.append(fib[i-1] + fib[i-2])
        return fib
        
    def calculate_fib_ratio(self):
        """
        Berechnet das Fibonacci-Volumenverhältnis.
        """
        if len(self.volume_history) < self.p.fib_levels + 1:
            return 0
            
        # Volumengewichtung mit Fibonacci-Sequenz
        weighted_volume = 0
        total_weight = 0
        
        for i in range(min(self.p.fib_levels, len(self.volume_history))):
            volume = self.volume_history[-(i+1)]
            weight = self.fib_sequence[i]
            weighted_volume += volume * weight
            total_weight += weight
            
        if total_weight == 0:
            return 0
            
        # Normalisiertes Verhältnis
        ratio = weighted_volume / (total_weight * np.mean(self.volume_history))
        
        return ratio
        
    def calculate_cycle_phase(self):
        """
        Berechnet die Zyklusphase.
        """
        if len(self.ratio_history) < self.p.period:
            return 0
            
        # Durchschnittliches Verhältnis
        avg_ratio = np.mean(self.ratio_history[-self.p.period:])
        
        # Zyklusbestimmung
        if avg_ratio > 1.618:  # Goldener Schnitt
            return 1  # Expansionsphase
        elif avg_ratio < 0.618:  # Reziproker goldener Schnitt
            return -1  # Kontraktionsphase
        else:
            return 0  # Übergangsphase
            
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.ratio_history) < 2:
            return 0
            
        # Verhältnismomentum
        momentum = self.ratio_history[-1] - self.ratio_history[-2]
        
        # Relative Stärke
        strength = abs(momentum)
        
        return min(1.0, strength)
        
    def next(self):
        # Volumenhistorie aktualisieren
        self.volume_history.append(self.data.volume[0])
        
        # Fibonacci-Verhältnis berechnen
        self.lines.fib_ratio[0] = self.calculate_fib_ratio()
        self.ratio_history.append(self.lines.fib_ratio[0])
        
        # Geglättetes Verhältnis
        self.lines.smoothed_ratio[0] = bt.indicators.EMA(
            self.lines.fib_ratio, period=self.p.period
        )[0]
        
        # Zyklusphase
        self.lines.cycle_phase[0] = self.calculate_cycle_phase()
        self.phase_history.append(self.lines.cycle_phase[0])
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volumenstruktur
        if len(self.volume_history) >= self.p.period:
            self.lines.volume_structure[0] = (
                self.volume_history[-1] /
                np.mean(self.volume_history[-self.p.period:])
            )
        else:
            self.lines.volume_structure[0] = 1.0
            
        # Historie begrenzen
        max_period = max(self.p.period, self.p.fib_levels + 1)
        for hist in [self.ratio_history, self.volume_history,
                    self.phase_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_ratio[0] > 1.618 and
            self.lines.cycle_phase[0] > 0 and
            self.lines.trend_strength[0] > self.p.min_trend_strength and
            self.lines.volume_structure[0] > 1.0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_ratio[0] < 0.618 and
            self.lines.cycle_phase[0] < 0 and
            self.lines.trend_strength[0] > self.p.min_trend_strength and
            self.lines.volume_structure[0] > 1.0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'fibonacci': {
                'ratio': self.lines.fib_ratio[0],
                'smoothed': self.lines.smoothed_ratio[0],
                'sequence': self.fib_sequence[:self.p.fib_levels],
                'golden_ratio': abs(self.lines.fib_ratio[0] - 1.618)
            },
            'cycle': {
                'phase': (
                    'expansion' if self.lines.cycle_phase[0] > 0
                    else 'contraction' if self.lines.cycle_phase[0] < 0
                    else 'transition'
                ),
                'strength': abs(self.lines.cycle_phase[0]),
                'persistence': (
                    np.mean([
                        1 if phase == self.lines.cycle_phase[0]
                        else 0
                        for phase in self.phase_history[-5:]
                    ]) if len(self.phase_history) >= 5
                    else 0
                )
            },
            'volume': {
                'structure': self.lines.volume_structure[0],
                'trend': (
                    'increasing' if self.lines.volume_structure[0] > 1
                    else 'decreasing'
                ),
                'fibonacci_aligned': (
                    abs(self.lines.volume_structure[0] - 1.618) < 0.1
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': np.sign(
                    self.lines.smoothed_ratio[0] - 1.618
                ),
                'momentum': (
                    self.lines.fib_ratio[0] - self.ratio_history[-2]
                    if len(self.ratio_history) > 1
                    else 0
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    self.lines.trend_strength[0] *
                    abs(self.lines.cycle_phase[0]) *
                    self.lines.volume_structure[0]
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'ratio_stability': (
                    np.std(self.ratio_history)
                    if len(self.ratio_history) > 1
                    else 0
                ),
                'phase_stability': (
                    np.std(self.phase_history)
                    if len(self.phase_history) > 1
                    else 0
                )
            }
        }
