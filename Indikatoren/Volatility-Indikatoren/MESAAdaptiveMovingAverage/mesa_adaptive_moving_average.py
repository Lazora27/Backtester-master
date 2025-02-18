import backtrader as bt
import numpy as np

class MESAAdaptiveMovingAverage(bt.Indicator):
    """
    MESA Adaptive Moving Average (MAMA)
    
    Ein adaptiver Volatilitätsindikator, der die Glättungsperiode
    basierend auf der Marktphase anpasst.
    
    Features:
    - Adaptive Glättung
    - Phasenanalyse
    - Volatilitätsnormalisierung
    - Signalgenerierung
    
    Parameter:
    - fast_limit (0.5): Maximale Anpassungsrate
    - slow_limit (0.05): Minimale Anpassungsrate
    - phase_period (10): Phasenanalyseperiode
    """
    
    lines = ('mama', 'fama',
             'phase', 'volatility_ratio',
             'signal')
             
    params = (
        ('fast_limit', 0.5),
        ('slow_limit', 0.05),
        ('phase_period', 10)
    )
    
    plotlines = dict(
        mama=dict(color='blue', _name='MAMA'),
        fama=dict(color='red', _name='FAMA'),
        phase=dict(color='green', _name='Phase'),
        volatility_ratio=dict(color='purple', _name='Volatility Ratio'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(MESAAdaptiveMovingAverage, self).__init__()
        
        # Historie
        self.smooth_history = []
        self.phase_history = []
        self.mama_history = []
        self.fama_history = []
        
        # Initialisierung
        self.smooth_price = 0
        self.detrender = 0
        self.q1 = 0
        self.i1 = 0
        self.jI = 0
        self.jQ = 0
        
    def smooth(self, price):
        """
        Glättet den Preis.
        """
        return (4 * price + 3 * self.data.close[-1] +
                2 * self.data.close[-2] + self.data.close[-3]) / 10
                
    def calculate_phase(self):
        """
        Berechnet die Phase.
        """
        if len(self.data) < self.p.phase_period:
            return 0
            
        # Hilbert Transform
        self.detrender = (
            0.0962 * self.smooth_price +
            0.5769 * self.smooth_history[-2] -
            0.5769 * self.smooth_history[-4] -
            0.0962 * self.smooth_history[-6]
        )
        
        # Quadratur und In-Phase Komponenten
        self.q1 = (
            0.0962 * self.detrender +
            0.5769 * self.smooth_history[-2] -
            0.5769 * self.smooth_history[-4] -
            0.0962 * self.smooth_history[-6]
        )
        
        self.i1 = self.smooth_history[-3]
        
        # Jitter Reduzierung
        self.jI = (
            0.0962 * self.i1 +
            0.5769 * self.jI -
            0.5769 * self.jI -
            0.0962 * self.jI
        )
        
        self.jQ = (
            0.0962 * self.q1 +
            0.5769 * self.jQ -
            0.5769 * self.jQ -
            0.0962 * self.jQ
        )
        
        # Phase berechnen
        if self.jI != 0:
            phase = np.arctan(self.jQ / self.jI)
        else:
            phase = 0
            
        return phase
        
    def calculate_alpha(self, phase):
        """
        Berechnet die Anpassungsrate.
        """
        if len(self.phase_history) < 2:
            return self.p.slow_limit
            
        delta_phase = abs(phase - self.phase_history[-1])
        
        alpha = (
            self.p.fast_limit /
            (1 + delta_phase)
        )
        
        return min(
            max(alpha, self.p.slow_limit),
            self.p.fast_limit
        )
        
    def calculate_volatility_ratio(self):
        """
        Berechnet das Volatilitätsverhältnis.
        """
        if len(self.data) < self.p.phase_period:
            return 1.0
            
        current_vol = np.std([
            self.data.close[-i] for i in range(5)
        ])
        historical_vol = np.std([
            self.data.close[-i]
            for i in range(self.p.phase_period)
        ])
        
        return (
            current_vol / historical_vol
            if historical_vol != 0 else 1.0
        )
        
    def next(self):
        # Preis glätten
        self.smooth_price = self.smooth(self.data.close[0])
        self.smooth_history.append(self.smooth_price)
        
        # Phase berechnen
        phase = self.calculate_phase()
        self.phase_history.append(phase)
        self.lines.phase[0] = phase
        
        # Alpha berechnen
        alpha = self.calculate_alpha(phase)
        
        # MAMA und FAMA berechnen
        if len(self.mama_history) > 0:
            self.lines.mama[0] = (
                alpha * self.smooth_price +
                (1 - alpha) * self.mama_history[-1]
            )
        else:
            self.lines.mama[0] = self.smooth_price
            
        self.mama_history.append(self.lines.mama[0])
        
        if len(self.fama_history) > 0:
            self.lines.fama[0] = (
                0.5 * alpha * self.lines.mama[0] +
                (1 - 0.5 * alpha) * self.fama_history[-1]
            )
        else:
            self.lines.fama[0] = self.lines.mama[0]
            
        self.fama_history.append(self.lines.fama[0])
        
        # Volatilitätsverhältnis
        self.lines.volatility_ratio[0] = self.calculate_volatility_ratio()
        
        # Signal
        if (self.lines.mama[0] > self.lines.fama[0] and
            phase > 0):
            self.lines.signal[0] = 1  # Kaufsignal
        elif (self.lines.mama[0] < self.lines.fama[0] and
              phase < 0):
            self.lines.signal[0] = -1  # Verkaufssignal
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = self.p.phase_period
        for hist in [self.smooth_history, self.phase_history,
                    self.mama_history, self.fama_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'mama': {
                'value': self.lines.mama[0],
                'fama': self.lines.fama[0],
                'spread': (
                    self.lines.mama[0] -
                    self.lines.fama[0]
                ),
                'trend': (
                    'up' if self.lines.mama[0] > self.lines.fama[0]
                    else 'down'
                )
            },
            'phase': {
                'value': self.lines.phase[0],
                'state': (
                    'leading' if self.lines.phase[0] > 0
                    else 'lagging'
                ),
                'strength': abs(self.lines.phase[0])
            },
            'volatility': {
                'ratio': self.lines.volatility_ratio[0],
                'state': (
                    'increasing'
                    if self.lines.volatility_ratio[0] > 1
                    else 'decreasing'
                ),
                'relative_level': (
                    'high'
                    if self.lines.volatility_ratio[0] > 1.5
                    else 'low'
                    if self.lines.volatility_ratio[0] < 0.5
                    else 'normal'
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
                    abs(self.lines.phase[0]) *
                    abs(self.lines.mama[0] -
                        self.lines.fama[0]) /
                    self.lines.mama[0]
                    if self.lines.mama[0] != 0
                    else 0
                )
            },
            'risk': {
                'phase_risk': (
                    1 - abs(self.lines.phase[0])
                    if abs(self.lines.phase[0]) <= 1
                    else 0
                ),
                'spread_risk': (
                    abs(self.lines.mama[0] -
                        self.lines.fama[0]) /
                    self.lines.mama[0]
                    if self.lines.mama[0] != 0
                    else 1
                ),
                'volatility_risk': (
                    self.lines.volatility_ratio[0]
                    if self.lines.volatility_ratio[0] > 1
                    else 1 / self.lines.volatility_ratio[0]
                    if self.lines.volatility_ratio[0] > 0
                    else 1
                )
            }
        }
