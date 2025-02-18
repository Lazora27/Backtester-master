import backtrader as bt
import numpy as np

class DecyclerOscillator(bt.Indicator):
    """
    Decycler Oscillator
    
    Ein Indikator, der Preisbewegungen von zyklischen Komponenten
    trennt und den verbleibenden Trend analysiert.
    
    Features:
    - Zyklische Komponenten-Entfernung
    - Trendextraktion
    - Oszillator-Berechnung
    - Signalgenerierung
    
    Parameter:
    - hp_period (40): Hochpass-Filterperiode
    - lp_period (10): Tiefpass-Filterperiode
    - smooth_period (10): Glättungsperiode
    """
    
    lines = ('decycler', 'oscillator',
             'trend_strength', 'cycle_removed',
             'signal')
             
    params = (
        ('hp_period', 40),
        ('lp_period', 10),
        ('smooth_period', 10)
    )
    
    plotlines = dict(
        decycler=dict(color='blue', _name='Decycler'),
        oscillator=dict(color='red', _name='Oscillator'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        cycle_removed=dict(color='purple', _name='Cycle Removed'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(DecyclerOscillator, self).__init__()
        
        # Historie
        self.price_history = []
        self.decycler_history = []
        
        # Alpha-Werte für Filter
        self.hp_alpha = 2 * np.pi / self.p.hp_period
        self.lp_alpha = 2 * np.pi / self.p.lp_period
        
    def high_pass_filter(self, data):
        """
        Wendet einen Hochpass-Filter an.
        """
        if len(data) < 2:
            return data[0] if len(data) > 0 else 0
            
        filtered = []
        a1 = (1 - self.hp_alpha/2) / (1 + self.hp_alpha/2)
        b0 = (1 + self.hp_alpha/2)
        b1 = -(1 + self.hp_alpha/2)
        
        prev_input = data[0]
        prev_output = 0
        
        for x in data:
            y = (b0 * x + b1 * prev_input - a1 * prev_output) / 2
            filtered.append(y)
            prev_input = x
            prev_output = y
            
        return filtered[-1]
        
    def low_pass_filter(self, data):
        """
        Wendet einen Tiefpass-Filter an.
        """
        if len(data) < 2:
            return data[0] if len(data) > 0 else 0
            
        filtered = []
        alpha = self.lp_alpha
        
        prev_output = data[0]
        
        for x in data:
            y = prev_output + alpha * (x - prev_output)
            filtered.append(y)
            prev_output = y
            
        return filtered[-1]
        
    def calculate_oscillator(self):
        """
        Berechnet den Oszillator-Wert.
        """
        if len(self.decycler_history) < 2:
            return 0
            
        return (
            self.decycler_history[-1] -
            self.decycler_history[-2]
        )
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.decycler_history) < self.p.smooth_period:
            return 0
            
        trend = np.array(
            self.decycler_history[-self.p.smooth_period:]
        )
        return np.std(trend)
        
    def next(self):
        # Preis speichern
        self.price_history.append(self.data.close[0])
        
        # Hochpass-Filter anwenden
        hp_filtered = self.high_pass_filter(self.price_history)
        
        # Tiefpass-Filter anwenden
        decycler = self.low_pass_filter([hp_filtered])
        self.decycler_history.append(decycler)
        
        # Linien aktualisieren
        self.lines.decycler[0] = decycler
        self.lines.oscillator[0] = self.calculate_oscillator()
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        self.lines.cycle_removed[0] = (
            self.data.close[0] - decycler
        )
        
        # Signal
        if len(self.decycler_history) >= 2:
            if (self.lines.oscillator[0] > 0 and
                self.lines.trend_strength[0] > 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (self.lines.oscillator[0] < 0 and
                  self.lines.trend_strength[0] > 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.hp_period,
            self.p.lp_period,
            self.p.smooth_period
        )
        for hist in [self.price_history,
                    self.decycler_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'decycler': {
                'value': self.lines.decycler[0],
                'oscillator': self.lines.oscillator[0],
                'trend': (
                    'up' if self.lines.oscillator[0] > 0
                    else 'down'
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'quality': (
                    'strong'
                    if self.lines.trend_strength[0] > 0.7
                    else 'weak'
                ),
                'reliability': (
                    abs(self.lines.oscillator[0])
                    if abs(self.lines.oscillator[0]) <= 1
                    else 1
                )
            },
            'cycles': {
                'removed': self.lines.cycle_removed[0],
                'significance': (
                    abs(self.lines.cycle_removed[0]) /
                    self.data.close[0]
                    if self.data.close[0] != 0
                    else 0
                ),
                'impact': (
                    'high'
                    if abs(self.lines.cycle_removed[0]) >
                       0.1 * self.data.close[0]
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
                    self.lines.trend_strength[0] *
                    abs(self.lines.oscillator[0])
                    if abs(self.lines.oscillator[0]) <= 1
                    else self.lines.trend_strength[0]
                )
            },
            'market_state': {
                'trend_quality': (
                    'clean'
                    if abs(self.lines.cycle_removed[0]) <
                       0.05 * self.data.close[0]
                    else 'noisy'
                ),
                'cycle_influence': (
                    'minimal'
                    if abs(self.lines.cycle_removed[0]) <
                       0.03 * self.data.close[0]
                    else 'significant'
                ),
                'trading_condition': (
                    'favorable'
                    if self.lines.trend_strength[0] > 0.5 and
                       abs(self.lines.cycle_removed[0]) <
                       0.07 * self.data.close[0]
                    else 'unfavorable'
                )
            }
        }
