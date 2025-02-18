import backtrader as bt
import numpy as np

class KeltnerBandWidth(bt.Indicator):
    """
    Keltner Band Width Indicator
    
    Ein Volatilitätsindikator, der die Breite der Keltner
    Channels analysiert.
    
    Features:
    - Keltner Channel Breitenanalyse
    - Volatilitätsnormalisierung
    - Trendstärkeberechnung
    - Signalgenerierung
    
    Parameter:
    - period (20): Analysezeitraum
    - atr_period (10): ATR-Periode
    - devfactor (2.0): Standardabweichungsfaktor
    """
    
    lines = ('kbw', 'normalized_kbw',
             'trend_strength', 'volatility_regime',
             'signal')
             
    params = (
        ('period', 20),
        ('atr_period', 10),
        ('devfactor', 2.0)
    )
    
    plotlines = dict(
        kbw=dict(color='blue', _name='KBW'),
        normalized_kbw=dict(color='red', _name='Normalized KBW'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volatility_regime=dict(color='purple', _name='Volatility Regime'),
        signal=dict(color='orange', _name='Signal')
    )
    
    def __init__(self):
        super(KeltnerBandWidth, self).__init__()
        
        # Keltner Channel
        self.kc = bt.indicators.KeltnerChannel(
            period=self.p.period,
            devfactor=self.p.devfactor
        )
        
        # ATR
        self.atr = bt.indicators.ATR(period=self.p.atr_period)
        
        # Historie
        self.kbw_history = []
        self.atr_history = []
        
    def calculate_kbw(self):
        """
        Berechnet die Keltner Band Breite.
        """
        if self.kc.lines.mid[0] != 0:
            return (
                (self.kc.lines.top[0] - self.kc.lines.bot[0]) /
                self.kc.lines.mid[0]
            )
        return 0
        
    def calculate_regime(self):
        """
        Bestimmt das Volatilitätsregime.
        """
        if len(self.kbw_history) < self.p.period:
            return 0
            
        mean_kbw = np.mean(self.kbw_history)
        std_kbw = np.std(self.kbw_history)
        
        if std_kbw == 0:
            return 0
            
        z_score = (self.lines.kbw[0] - mean_kbw) / std_kbw
        
        if z_score > 1:
            regime = 1  # Expansion
        elif z_score < -1:
            regime = -1  # Kontraktion
        else:
            regime = 0  # Normal
            
        return regime
        
    def next(self):
        # KBW berechnen
        self.lines.kbw[0] = self.calculate_kbw()
        self.kbw_history.append(self.lines.kbw[0])
        
        # Normalisierte KBW
        if len(self.kbw_history) >= self.p.period:
            mean_kbw = np.mean(self.kbw_history[-self.p.period:])
            std_kbw = np.std(self.kbw_history[-self.p.period:])
            
            self.lines.normalized_kbw[0] = (
                (self.lines.kbw[0] - mean_kbw) /
                std_kbw if std_kbw != 0 else 0
            )
        else:
            self.lines.normalized_kbw[0] = 0
            
        # Volatilitätsregime
        self.lines.volatility_regime[0] = self.calculate_regime()
        
        # Trendstärke
        if len(self.kbw_history) >= 2:
            self.lines.trend_strength[0] = abs(
                self.lines.kbw[0] -
                self.lines.kbw[-1]
            )
        else:
            self.lines.trend_strength[0] = 0
            
        # Signal
        self.lines.signal[0] = (
            1 if (
                self.lines.volatility_regime[0] < 0 and
                self.lines.trend_strength[0] > 0
            )
            else -1 if (
                self.lines.volatility_regime[0] > 0 and
                self.lines.trend_strength[0] < 0
            )
            else 0
        )
        
        # ATR Historie
        self.atr_history.append(self.atr[0])
        
        # Historie begrenzen
        max_period = max(self.p.period, self.p.atr_period)
        for hist in [self.kbw_history, self.atr_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'width': {
                'current': self.lines.kbw[0],
                'normalized': self.lines.normalized_kbw[0],
                'trend': (
                    'expanding' if self.lines.kbw[0] > self.lines.kbw[-1]
                    else 'contracting'
                )
            },
            'volatility': {
                'regime': (
                    'expansion' if self.lines.volatility_regime[0] > 0
                    else 'contraction' if self.lines.volatility_regime[0] < 0
                    else 'normal'
                ),
                'strength': abs(self.lines.volatility_regime[0]),
                'persistence': (
                    np.mean([
                        1 if v == self.lines.volatility_regime[0] else 0
                        for v in self.kbw_history[-5:]
                    ]) if len(self.kbw_history) >= 5
                    else 0
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': (
                    'up' if self.lines.kbw[0] > self.lines.kbw[-1]
                    else 'down'
                ),
                'quality': (
                    1 - abs(self.lines.normalized_kbw[0])
                    if abs(self.lines.normalized_kbw[0]) <= 1
                    else 0
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
                    self.lines.trend_strength[0] *
                    abs(self.lines.volatility_regime[0])
                )
            },
            'risk': {
                'width_risk': abs(self.lines.normalized_kbw[0]),
                'volatility_risk': (
                    self.atr[0] / np.mean(self.atr_history)
                    if len(self.atr_history) > 0 and
                    np.mean(self.atr_history) > 0
                    else 1.0
                ),
                'trend_risk': (
                    1 - self.lines.trend_strength[0]
                    if self.lines.trend_strength[0] <= 1
                    else 0
                )
            }
        }
