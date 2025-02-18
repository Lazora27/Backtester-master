import backtrader as bt
import numpy as np

class PolarizedTimePrice(bt.Indicator):
    """
    Polarized Time Price Oscillator
    
    Ein fortgeschrittener Indikator, der Preisbewegungen in
    polarisierte Komponenten zerlegt.
    
    Features:
    - Polarisierte Preisanalyse
    - Zeitliche Polarisation
    - Oszillatorberechnung
    - Signalgenerierung
    
    Parameter:
    - period (20): Analyseperiode
    - polar_shift (10): Polarisationsverschiebung
    - smooth_period (5): Glättungsperiode
    """
    
    lines = ('oscillator', 'polarity',
             'momentum', 'cycle_phase',
             'signal')
             
    params = (
        ('period', 20),
        ('polar_shift', 10),
        ('smooth_period', 5)
    )
    
    plotlines = dict(
        oscillator=dict(color='blue', _name='Oscillator'),
        polarity=dict(color='red', _name='Polarity'),
        momentum=dict(color='green', _name='Momentum'),
        cycle_phase=dict(color='purple', _name='Cycle Phase'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(PolarizedTimePrice, self).__init__()
        
        # Historie
        self.price_history = []
        self.oscillator_history = []
        self.polarity_history = []
        
    def calculate_polarity(self):
        """
        Berechnet die Polarität der Preisbewegung.
        """
        if len(self.price_history) < self.p.polar_shift:
            return 0
            
        current = np.array(
            self.price_history[-self.p.polar_shift:]
        )
        previous = np.array(
            self.price_history[
                -2*self.p.polar_shift:-self.p.polar_shift
            ]
        )
        
        if len(current) == len(previous):
            correlation = np.corrcoef(current, previous)[0,1]
            return correlation
        return 0
        
    def calculate_oscillator(self):
        """
        Berechnet den Oszillatorwert.
        """
        if len(self.price_history) < self.p.period:
            return 0
            
        prices = np.array(
            self.price_history[-self.p.period:]
        )
        mean = np.mean(prices)
        std = np.std(prices)
        
        if std != 0:
            return (prices[-1] - mean) / std
        return 0
        
    def calculate_momentum(self):
        """
        Berechnet den Momentum-Wert.
        """
        if len(self.oscillator_history) < 2:
            return 0
            
        return (
            self.oscillator_history[-1] -
            self.oscillator_history[-2]
        )
        
    def calculate_cycle_phase(self):
        """
        Berechnet die Zyklusphase.
        """
        if len(self.polarity_history) < 2:
            return 0
            
        current = self.polarity_history[-1]
        previous = self.polarity_history[-2]
        
        if current > previous:
            return 1  # Aufwärtsphase
        elif current < previous:
            return -1  # Abwärtsphase
        return 0  # Neutral
        
    def next(self):
        # Preis speichern
        self.price_history.append(self.data.close[0])
        
        # Oszillator berechnen
        oscillator = self.calculate_oscillator()
        self.oscillator_history.append(oscillator)
        
        # Polarität berechnen
        polarity = self.calculate_polarity()
        self.polarity_history.append(polarity)
        
        # Momentum und Zyklusphase
        momentum = self.calculate_momentum()
        cycle_phase = self.calculate_cycle_phase()
        
        # Linien aktualisieren
        self.lines.oscillator[0] = oscillator
        self.lines.polarity[0] = polarity
        self.lines.momentum[0] = momentum
        self.lines.cycle_phase[0] = cycle_phase
        
        # Signal
        if len(self.oscillator_history) >= 2:
            if (momentum > 0 and
                cycle_phase > 0 and
                polarity > 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (momentum < 0 and
                  cycle_phase < 0 and
                  polarity < 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.period,
            2 * self.p.polar_shift,
            self.p.smooth_period
        )
        for hist in [self.price_history,
                    self.oscillator_history,
                    self.polarity_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'oscillator': {
                'value': self.lines.oscillator[0],
                'polarity': self.lines.polarity[0],
                'momentum': self.lines.momentum[0],
                'phase': self.lines.cycle_phase[0]
            },
            'cycle_state': {
                'trend': (
                    'up'
                    if self.lines.cycle_phase[0] > 0
                    else 'down'
                    if self.lines.cycle_phase[0] < 0
                    else 'neutral'
                ),
                'strength': abs(self.lines.polarity[0]),
                'momentum': (
                    'increasing'
                    if self.lines.momentum[0] > 0
                    else 'decreasing'
                    if self.lines.momentum[0] < 0
                    else 'stable'
                )
            },
            'polarity_analysis': {
                'correlation': self.lines.polarity[0],
                'direction': (
                    'positive'
                    if self.lines.polarity[0] > 0
                    else 'negative'
                    if self.lines.polarity[0] < 0
                    else 'neutral'
                ),
                'strength': abs(self.lines.polarity[0])
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'confidence': (
                    abs(self.lines.polarity[0]) *
                    abs(self.lines.momentum[0])
                )
            },
            'market_conditions': {
                'cycle_quality': (
                    'optimal'
                    if (abs(self.lines.polarity[0]) > 0.7 and
                        abs(self.lines.momentum[0]) > 0.5)
                    else 'suboptimal'
                ),
                'trend_structure': (
                    'clear'
                    if abs(self.lines.oscillator[0]) > 1.5
                    else 'unclear'
                ),
                'trading_environment': (
                    'favorable'
                    if (abs(self.lines.polarity[0]) > 0.6 and
                        abs(self.lines.momentum[0]) > 0.4 and
                        abs(self.lines.oscillator[0]) > 1.0)
                    else 'unfavorable'
                )
            }
        }
