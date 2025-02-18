import backtrader as bt
import numpy as np

class MovingAverageCycleDetector(bt.Indicator):
    """
    Moving Average Cycle Detector
    
    Ein Indikator, der multiple gleitende Durchschnitte verwendet,
    um Marktzyklen zu identifizieren und zu analysieren.
    
    Features:
    - Multi-MA Zykluserkennung
    - Adaptive Zyklusanalyse
    - Trendstärkeberechnung
    - Signalgenerierung
    
    Parameter:
    - ma_periods (20,50,100): MA-Perioden
    - cycle_period (20): Zyklusperiode
    - smooth_period (10): Glättungsperiode
    """
    
    lines = ('cycle', 'ma_spread',
             'cycle_strength', 'cycle_phase',
             'signal')
             
    params = (
        ('ma_periods', (20, 50, 100)),
        ('cycle_period', 20),
        ('smooth_period', 10)
    )
    
    plotlines = dict(
        cycle=dict(color='blue', _name='Cycle'),
        ma_spread=dict(color='red', _name='MA Spread'),
        cycle_strength=dict(color='green', _name='Cycle Strength'),
        cycle_phase=dict(color='purple', _name='Cycle Phase'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(MovingAverageCycleDetector, self).__init__()
        
        # Historie
        self.cycle_history = []
        self.ma_values = []
        
        # Moving Averages initialisieren
        self.mas = [
            bt.indicators.SMA(period=p)
            for p in self.p.ma_periods
        ]
        
    def calculate_ma_spread(self):
        """
        Berechnet die MA-Spreizung.
        """
        if not all(ma[0] for ma in self.mas):
            return 0
            
        ma_values = [ma[0] for ma in self.mas]
        return max(ma_values) - min(ma_values)
        
    def calculate_cycle_strength(self):
        """
        Berechnet die Zyklusstärke.
        """
        if len(self.cycle_history) < self.p.cycle_period:
            return 0
            
        cycles = np.array(
            self.cycle_history[-self.p.cycle_period:]
        )
        return np.std(cycles)
        
    def calculate_cycle_phase(self):
        """
        Berechnet die Zyklusphase.
        """
        if len(self.cycle_history) < 2:
            return 0
            
        current = self.cycle_history[-1]
        previous = self.cycle_history[-2]
        
        if current > previous:
            return 1  # Aufwärtsphase
        elif current < previous:
            return -1  # Abwärtsphase
        return 0  # Neutral
        
    def next(self):
        # MA-Spreizung berechnen
        ma_spread = self.calculate_ma_spread()
        self.ma_values.append(ma_spread)
        
        # Zyklus berechnen
        if len(self.ma_values) >= self.p.smooth_period:
            cycle = np.mean(
                self.ma_values[-self.p.smooth_period:]
            )
        else:
            cycle = ma_spread
            
        self.cycle_history.append(cycle)
        
        # Linien aktualisieren
        self.lines.cycle[0] = cycle
        self.lines.ma_spread[0] = ma_spread
        self.lines.cycle_strength[0] = self.calculate_cycle_strength()
        self.lines.cycle_phase[0] = self.calculate_cycle_phase()
        
        # Signal
        if len(self.cycle_history) >= 2:
            if (self.lines.cycle_phase[0] > 0 and
                self.lines.cycle_strength[0] > 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (self.lines.cycle_phase[0] < 0 and
                  self.lines.cycle_strength[0] > 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            max(self.p.ma_periods),
            self.p.cycle_period,
            self.p.smooth_period
        )
        for hist in [self.cycle_history,
                    self.ma_values]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'cycle': {
                'value': self.lines.cycle[0],
                'spread': self.lines.ma_spread[0],
                'strength': self.lines.cycle_strength[0],
                'phase': self.lines.cycle_phase[0]
            },
            'cycle_state': {
                'trend': (
                    'up' if self.lines.cycle_phase[0] > 0
                    else 'down' if self.lines.cycle_phase[0] < 0
                    else 'neutral'
                ),
                'strength': (
                    'strong'
                    if self.lines.cycle_strength[0] > 0.7
                    else 'weak'
                ),
                'reliability': (
                    'high'
                    if self.lines.cycle_strength[0] > 0.8
                    else 'medium'
                    if self.lines.cycle_strength[0] > 0.5
                    else 'low'
                )
            },
            'ma_analysis': {
                'spread_state': (
                    'expanding'
                    if len(self.ma_values) >= 2 and
                       self.ma_values[-1] > self.ma_values[-2]
                    else 'contracting'
                ),
                'alignment': (
                    'bullish'
                    if all(ma[0] > ma[-1]
                          for ma in self.mas)
                    else 'bearish'
                    if all(ma[0] < ma[-1]
                          for ma in self.mas)
                    else 'mixed'
                ),
                'convergence': (
                    'high'
                    if self.lines.ma_spread[0] <
                       0.01 * self.data.close[0]
                    else 'low'
                )
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'confidence': (
                    self.lines.cycle_strength[0] *
                    abs(self.lines.cycle_phase[0])
                )
            },
            'market_state': {
                'cycle_quality': (
                    'optimal'
                    if (self.lines.cycle_strength[0] > 0.7 and
                        abs(self.lines.cycle_phase[0]) == 1)
                    else 'suboptimal'
                ),
                'trend_structure': (
                    'clear'
                    if self.lines.ma_spread[0] >
                       0.02 * self.data.close[0]
                    else 'unclear'
                ),
                'trading_conditions': (
                    'favorable'
                    if (self.lines.cycle_strength[0] > 0.6 and
                        abs(self.lines.cycle_phase[0]) == 1 and
                        self.lines.ma_spread[0] >
                        0.015 * self.data.close[0])
                    else 'unfavorable'
                )
            }
        }
