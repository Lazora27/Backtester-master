import backtrader as bt
import numpy as np

class CumulativeTick(bt.Indicator):
    """
    Cumulative Tick Indicator
    
    Ein fortgeschrittener Indikator zur Analyse der
    kumulativen Tick-Bewegungen.
    
    Features:
    - Tick-Analyse
    - Kumulativer Delta
    - Impulsberechnung
    - Signalgenerierung
    
    Parameter:
    - tick_period (20): Berechnungsperiode
    - delta_threshold (100): Delta-Schwelle
    - smooth_period (5): Glättungsperiode
    """
    
    lines = ('tick_delta', 'cumulative_delta',
             'tick_impulse', 'tick_momentum',
             'signal')
             
    params = (
        ('tick_period', 20),
        ('delta_threshold', 100),
        ('smooth_period', 5)
    )
    
    plotlines = dict(
        tick_delta=dict(color='blue', _name='Tick Delta'),
        cumulative_delta=dict(color='red', _name='Cumulative Delta'),
        tick_impulse=dict(color='green', _name='Tick Impulse'),
        tick_momentum=dict(color='purple', _name='Tick Momentum'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(CumulativeTick, self).__init__()
        
        # Historie
        self.tick_history = []
        self.delta_history = []
        self.price_history = []
        
    def calculate_tick_delta(self):
        """
        Berechnet den Tick-Delta.
        """
        if len(self.price_history) < 2:
            return 0
            
        # Preisänderung bestimmen
        price_change = (
            self.price_history[-1] -
            self.price_history[-2]
        )
        
        # Tick-Delta basierend auf Preisänderung
        if price_change > 0:
            return 1
        elif price_change < 0:
            return -1
        return 0
        
    def calculate_cumulative_delta(self):
        """
        Berechnet den kumulativen Delta.
        """
        if len(self.delta_history) < self.p.tick_period:
            return sum(self.delta_history)
            
        return sum(
            self.delta_history[-self.p.tick_period:]
        )
        
    def calculate_tick_impulse(self):
        """
        Berechnet den Tick-Impuls.
        """
        if len(self.delta_history) < self.p.smooth_period:
            return 0
            
        recent_deltas = self.delta_history[
            -self.p.smooth_period:
        ]
        
        # Impuls basierend auf Delta-Änderung
        return sum(recent_deltas) / self.p.smooth_period
        
    def calculate_tick_momentum(self):
        """
        Berechnet das Tick-Momentum.
        """
        if len(self.delta_history) < self.p.tick_period:
            return 0
            
        period_deltas = self.delta_history[
            -self.p.tick_period:
        ]
        
        # Momentum als gewichtete Summe
        weights = np.linspace(1, 2, len(period_deltas))
        return np.average(period_deltas, weights=weights)
        
    def next(self):
        # Preis speichern
        self.price_history.append(self.data.close[0])
        
        # Tick-Delta berechnen
        tick_delta = self.calculate_tick_delta()
        self.delta_history.append(tick_delta)
        
        # Weitere Metriken
        cumulative_delta = self.calculate_cumulative_delta()
        tick_impulse = self.calculate_tick_impulse()
        tick_momentum = self.calculate_tick_momentum()
        
        # Linien aktualisieren
        self.lines.tick_delta[0] = tick_delta
        self.lines.cumulative_delta[0] = cumulative_delta
        self.lines.tick_impulse[0] = tick_impulse
        self.lines.tick_momentum[0] = tick_momentum
        
        # Signal
        if abs(cumulative_delta) > self.p.delta_threshold:
            if (cumulative_delta > 0 and
                tick_momentum > 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (cumulative_delta < 0 and
                  tick_momentum < 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.tick_period,
            self.p.smooth_period
        )
        for hist in [self.tick_history,
                    self.delta_history,
                    self.price_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'ticks': {
                'delta': self.lines.tick_delta[0],
                'cumulative': self.lines.cumulative_delta[0],
                'impulse': self.lines.tick_impulse[0],
                'momentum': self.lines.tick_momentum[0]
            },
            'flow_analysis': {
                'direction': (
                    'buying'
                    if self.lines.cumulative_delta[0] > 0
                    else 'selling'
                ),
                'strength': (
                    abs(self.lines.cumulative_delta[0]) /
                    self.p.delta_threshold
                ),
                'persistence': (
                    'persistent'
                    if abs(self.lines.tick_momentum[0]) > 0.5
                    else 'temporary'
                )
            },
            'momentum_analysis': {
                'value': self.lines.tick_momentum[0],
                'bias': (
                    'bullish'
                    if self.lines.tick_momentum[0] > 0.2
                    else 'bearish'
                    if self.lines.tick_momentum[0] < -0.2
                    else 'neutral'
                ),
                'strength': abs(self.lines.tick_momentum[0])
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'reliability': (
                    abs(self.lines.cumulative_delta[0]) /
                    self.p.delta_threshold *
                    abs(self.lines.tick_momentum[0])
                )
            },
            'market_conditions': {
                'tick_quality': (
                    'high'
                    if abs(self.lines.tick_delta[0]) > 0
                    else 'low'
                ),
                'flow_balance': (
                    'balanced'
                    if abs(
                        self.lines.cumulative_delta[0]
                    ) < self.p.delta_threshold * 0.5
                    else 'imbalanced'
                ),
                'trading_environment': (
                    'favorable'
                    if (abs(self.lines.cumulative_delta[0]) >
                        self.p.delta_threshold * 0.8 and
                        abs(self.lines.tick_momentum[0]) > 0.4)
                    else 'unfavorable'
                )
            }
        }
