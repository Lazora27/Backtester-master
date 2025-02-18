import backtrader as bt
import numpy as np

class BollingerBandSqueeze(bt.Indicator):
    """
    Bollinger Band Squeeze Indicator
    
    Ein Volatilitätsindikator, der Bollinger Band Squeezes
    identifiziert und analysiert.
    
    Features:
    - Squeeze-Erkennung
    - Momentum-Berechnung
    - Ausbruchsvorhersage
    - Trendstärkeanalyse
    
    Parameter:
    - bb_period (20): Bollinger Band Periode
    - kc_period (20): Keltner Channel Periode
    - bb_devfactor (2.0): Bollinger Band Standardabweichungsfaktor
    - kc_devfactor (1.5): Keltner Channel Standardabweichungsfaktor
    """
    
    lines = ('squeeze', 'momentum',
             'squeeze_intensity', 'breakout_potential',
             'signal')
             
    params = (
        ('bb_period', 20),
        ('kc_period', 20),
        ('bb_devfactor', 2.0),
        ('kc_devfactor', 1.5)
    )
    
    plotlines = dict(
        squeeze=dict(color='blue', _name='Squeeze'),
        momentum=dict(color='red', _name='Momentum'),
        squeeze_intensity=dict(color='green', _name='Intensity'),
        breakout_potential=dict(color='purple', _name='Breakout'),
        signal=dict(color='orange', _name='Signal')
    )
    
    def __init__(self):
        super(BollingerBandSqueeze, self).__init__()
        
        # Bollinger Bands
        self.bb = bt.indicators.BollingerBands(
            period=self.p.bb_period,
            devfactor=self.p.bb_devfactor
        )
        
        # Keltner Channel
        self.kc = bt.indicators.KeltnerChannel(
            period=self.p.kc_period,
            devfactor=self.p.kc_devfactor
        )
        
        # Historie
        self.squeeze_history = []
        self.momentum_history = []
        
    def calculate_squeeze(self):
        """
        Berechnet den Squeeze-Zustand.
        """
        bb_width = self.bb.lines.top[0] - self.bb.lines.bot[0]
        kc_width = self.kc.lines.top[0] - self.kc.lines.bot[0]
        
        if kc_width != 0:
            return bb_width / kc_width
        return 1.0
        
    def calculate_momentum(self):
        """
        Berechnet das Momentum.
        """
        if len(self.data) < self.p.bb_period:
            return 0
            
        # Preisänderung
        returns = [
            (self.data.close[-i] - self.data.close[-i-1]) /
            self.data.close[-i-1] if self.data.close[-i-1] != 0 else 0
            for i in range(self.p.bb_period)
        ]
        
        return np.sum(returns)
        
    def calculate_breakout_potential(self):
        """
        Berechnet das Ausbruchspotential.
        """
        if len(self.squeeze_history) < self.p.bb_period:
            return 0
            
        # Squeeze-Dauer
        squeeze_duration = sum(
            1 for x in self.squeeze_history[-self.p.bb_period:]
            if x < 1
        )
        
        # Momentum-Stärke
        momentum_strength = abs(self.lines.momentum[0])
        
        return squeeze_duration * momentum_strength
        
    def next(self):
        # Squeeze berechnen
        self.lines.squeeze[0] = self.calculate_squeeze()
        self.squeeze_history.append(self.lines.squeeze[0])
        
        # Momentum
        self.lines.momentum[0] = self.calculate_momentum()
        self.momentum_history.append(self.lines.momentum[0])
        
        # Squeeze-Intensität
        if len(self.squeeze_history) >= self.p.bb_period:
            min_squeeze = min(self.squeeze_history[-self.p.bb_period:])
            max_squeeze = max(self.squeeze_history[-self.p.bb_period:])
            
            if max_squeeze - min_squeeze > 0:
                self.lines.squeeze_intensity[0] = (
                    (self.lines.squeeze[0] - min_squeeze) /
                    (max_squeeze - min_squeeze)
                )
            else:
                self.lines.squeeze_intensity[0] = 0
        else:
            self.lines.squeeze_intensity[0] = 0
            
        # Ausbruchspotential
        self.lines.breakout_potential[0] = self.calculate_breakout_potential()
        
        # Signal
        self.lines.signal[0] = (
            1 if (
                self.lines.squeeze[0] < 1 and
                self.lines.momentum[0] > 0 and
                self.lines.breakout_potential[0] > self.p.bb_period / 2
            )
            else -1 if (
                self.lines.squeeze[0] < 1 and
                self.lines.momentum[0] < 0 and
                self.lines.breakout_potential[0] > self.p.bb_period / 2
            )
            else 0
        )
        
        # Historie begrenzen
        max_period = max(self.p.bb_period, self.p.kc_period)
        for hist in [self.squeeze_history, self.momentum_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'squeeze': {
                'active': self.lines.squeeze[0] < 1,
                'intensity': self.lines.squeeze_intensity[0],
                'duration': (
                    sum(1 for x in self.squeeze_history[-10:]
                        if x < 1)
                    if len(self.squeeze_history) >= 10
                    else 0
                )
            },
            'momentum': {
                'value': self.lines.momentum[0],
                'direction': (
                    'up' if self.lines.momentum[0] > 0
                    else 'down'
                ),
                'strength': abs(self.lines.momentum[0])
            },
            'breakout': {
                'potential': self.lines.breakout_potential[0],
                'probability': (
                    self.lines.breakout_potential[0] /
                    self.p.bb_period if self.p.bb_period > 0
                    else 0
                ),
                'direction': (
                    'up' if self.lines.momentum[0] > 0
                    else 'down'
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
                    self.lines.breakout_potential[0] /
                    self.p.bb_period if self.p.bb_period > 0
                    else 0
                )
            },
            'risk': {
                'squeeze_risk': 1 - self.lines.squeeze[0],
                'momentum_risk': abs(self.lines.momentum[0]),
                'breakout_risk': (
                    1 - (self.lines.breakout_potential[0] /
                         self.p.bb_period)
                    if self.p.bb_period > 0
                    else 1
                )
            }
        }
