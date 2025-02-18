import backtrader as bt
import numpy as np

class SineWaveAdaptive(bt.Indicator):
    """
    Sine Wave Adaptive Indicator
    
    Ein adaptiver Indikator, der Sinuswellen verwendet, um
    Marktzyklen zu identifizieren und zu analysieren.
    
    Features:
    - Adaptive Sinuswellenanalyse
    - Dynamische Periodizitätsanpassung
    - Phasenwinkelberechnung
    - Signalgenerierung
    
    Parameter:
    - period (20): Basisperiode
    - adapt_factor (0.1): Adaptionsfaktor
    - smooth_period (10): Glättungsperiode
    """
    
    lines = ('sine', 'lead_sine',
             'period', 'phase',
             'signal')
             
    params = (
        ('period', 20),
        ('adapt_factor', 0.1),
        ('smooth_period', 10)
    )
    
    plotlines = dict(
        sine=dict(color='blue', _name='Sine'),
        lead_sine=dict(color='red', _name='Lead Sine'),
        period=dict(color='green', _name='Period'),
        phase=dict(color='purple', _name='Phase'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(SineWaveAdaptive, self).__init__()
        
        # Historie
        self.price_history = []
        self.sine_history = []
        self.phase_history = []
        self.current_period = self.p.period
        
    def adaptive_period(self):
        """
        Berechnet die adaptive Periode.
        """
        if len(self.price_history) < self.p.period:
            return self.p.period
            
        # Autokorrelation berechnen
        prices = np.array(
            self.price_history[-self.p.period:]
        )
        norm_prices = (
            prices - np.mean(prices)
        ) / np.std(prices)
        
        corr = np.correlate(
            norm_prices,
            norm_prices,
            mode='full'
        )
        corr = corr[len(corr)//2:]
        
        # Peaks finden
        peaks = signal.find_peaks(corr)[0]
        if len(peaks) > 0:
            dominant_period = peaks[0]
            # Periode anpassen
            self.current_period = (
                (1 - self.p.adapt_factor) *
                self.current_period +
                self.p.adapt_factor * dominant_period
            )
            
        return max(
            min(self.current_period, self.p.period * 2),
            self.p.period / 2
        )
        
    def calculate_phase(self):
        """
        Berechnet den Phasenwinkel.
        """
        if len(self.sine_history) < 2:
            return 0
            
        current = self.sine_history[-1]
        previous = self.sine_history[-2]
        
        phase = np.arctan2(
            current - previous,
            self.p.smooth_period
        )
        return (phase + np.pi) % (2 * np.pi)
        
    def next(self):
        # Preis speichern
        self.price_history.append(self.data.close[0])
        
        # Adaptive Periode berechnen
        period = self.adaptive_period()
        
        # Phase berechnen
        if len(self.price_history) >= period:
            t = len(self.price_history) % period
            phase = 2 * np.pi * t / period
            
            # Sinus und Lead-Sinus
            sine = np.sin(phase)
            lead_sine = np.sin(phase + np.pi/4)
            
            self.sine_history.append(sine)
            self.phase_history.append(phase)
        else:
            sine = 0
            lead_sine = 0
            phase = 0
            
        # Linien aktualisieren
        self.lines.sine[0] = sine
        self.lines.lead_sine[0] = lead_sine
        self.lines.period[0] = period
        self.lines.phase[0] = phase
        
        # Signal
        if len(self.sine_history) >= 2:
            if (sine > 0 and
                self.sine_history[-2] <= 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (sine < 0 and
                  self.sine_history[-2] >= 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            int(self.p.period * 2),
            self.p.smooth_period
        )
        for hist in [self.price_history,
                    self.sine_history,
                    self.phase_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'wave': {
                'sine': self.lines.sine[0],
                'lead': self.lines.lead_sine[0],
                'period': self.lines.period[0],
                'phase': self.lines.phase[0]
            },
            'cycle_state': {
                'position': (
                    'peak'
                    if abs(self.lines.sine[0] - 1) < 0.1
                    else 'trough'
                    if abs(self.lines.sine[0] + 1) < 0.1
                    else 'transition'
                ),
                'direction': (
                    'up'
                    if self.lines.lead_sine[0] > 0
                    else 'down'
                ),
                'strength': abs(self.lines.sine[0])
            },
            'adaptation': {
                'current_period': self.current_period,
                'adaptation_rate': (
                    'high'
                    if abs(
                        self.current_period -
                        self.p.period
                    ) > self.p.period / 4
                    else 'low'
                ),
                'stability': (
                    'stable'
                    if len(self.sine_history) >= 2 and
                       abs(
                           self.sine_history[-1] -
                           self.sine_history[-2]
                       ) < 0.2
                    else 'unstable'
                )
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'reliability': (
                    abs(self.lines.sine[0]) *
                    (1 - abs(
                        self.lines.sine[0] -
                        self.lines.lead_sine[0]
                    ) / 2)
                )
            },
            'market_conditions': {
                'cycle_quality': (
                    'optimal'
                    if abs(self.lines.sine[0]) > 0.7
                    else 'suboptimal'
                ),
                'trend_structure': (
                    'clear'
                    if self.lines.period[0] >
                       self.p.period * 0.8
                    else 'unclear'
                ),
                'trading_environment': (
                    'favorable'
                    if (abs(self.lines.sine[0]) > 0.6 and
                        self.lines.period[0] >
                        self.p.period * 0.9)
                    else 'unfavorable'
                )
            }
        }
