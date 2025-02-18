import backtrader as bt
import numpy as np

class BollingerBandWidth(bt.Indicator):
    """
    Bollinger Band Width (BBW)
    
    Ein Volatilitätsindikator, der die relative Breite der
    Bollinger Bänder analysiert.
    
    Features:
    - Bandbreitenberechnung
    - Volatilitätsnormalisierung
    - Trendstärkeanalyse
    - Signalgenerierung
    
    Parameter:
    - period (20): Analysezeitraum
    - devfactor (2.0): Standardabweichungsfaktor
    - squeeze_threshold (0.3): Squeeze-Schwelle
    """
    
    lines = ('bbw', 'normalized_bbw',
             'squeeze_indicator', 'trend_strength',
             'volatility_signal')
             
    params = (
        ('period', 20),
        ('devfactor', 2.0),
        ('squeeze_threshold', 0.3)
    )
    
    plotlines = dict(
        bbw=dict(color='blue', _name='BBW'),
        normalized_bbw=dict(color='red', _name='Normalized BBW'),
        squeeze_indicator=dict(color='green', _name='Squeeze'),
        trend_strength=dict(color='purple', _name='Trend Strength'),
        volatility_signal=dict(color='orange', _name='Volatility Signal')
    )
    
    def __init__(self):
        super(BollingerBandWidth, self).__init__()
        
        # Bollinger Bands
        self.boll = bt.indicators.BollingerBands(
            period=self.p.period,
            devfactor=self.p.devfactor
        )
        
        # Historie
        self.bbw_history = []
        
    def calculate_bbw(self):
        """
        Berechnet die Bollinger Band Breite.
        """
        if self.data[0] != 0:
            return (
                (self.boll.lines.top[0] - self.boll.lines.bot[0]) /
                self.boll.lines.mid[0]
            )
        return 0
        
    def calculate_squeeze(self):
        """
        Berechnet den Squeeze-Indikator.
        """
        if len(self.bbw_history) < self.p.period:
            return 0
            
        current_bbw = self.lines.bbw[0]
        min_bbw = min(self.bbw_history[-self.p.period:])
        max_bbw = max(self.bbw_history[-self.p.period:])
        
        if max_bbw - min_bbw > 0:
            return (current_bbw - min_bbw) / (max_bbw - min_bbw)
        return 0
        
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
        
        # BBW-Änderung
        bbw_change = (
            self.lines.bbw[0] - self.lines.bbw[-1]
        ) if len(self.bbw_history) > 1 else 0
        
        return price_change * bbw_change
        
    def next(self):
        # BBW berechnen
        self.lines.bbw[0] = self.calculate_bbw()
        self.bbw_history.append(self.lines.bbw[0])
        
        # Normalisierte BBW
        if len(self.bbw_history) >= self.p.period:
            mean_bbw = np.mean(self.bbw_history[-self.p.period:])
            std_bbw = np.std(self.bbw_history[-self.p.period:])
            
            self.lines.normalized_bbw[0] = (
                (self.lines.bbw[0] - mean_bbw) /
                std_bbw if std_bbw != 0 else 0
            )
        else:
            self.lines.normalized_bbw[0] = 0
            
        # Squeeze-Indikator
        self.lines.squeeze_indicator[0] = self.calculate_squeeze()
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volatilitätssignal
        self.lines.volatility_signal[0] = (
            1 if self.lines.squeeze_indicator[0] < self.p.squeeze_threshold
            else -1 if self.lines.squeeze_indicator[0] > (1 - self.p.squeeze_threshold)
            else 0
        )
        
        # Historie begrenzen
        if len(self.bbw_history) > self.p.period:
            self.bbw_history.pop(0)
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'bbw': {
                'current': self.lines.bbw[0],
                'normalized': self.lines.normalized_bbw[0],
                'squeeze': self.lines.squeeze_indicator[0],
                'trend': (
                    'expanding' if self.lines.bbw[0] > self.lines.bbw[-1]
                    else 'contracting'
                )
            },
            'volatility': {
                'signal': (
                    'squeeze' if self.lines.volatility_signal[0] > 0
                    else 'expansion' if self.lines.volatility_signal[0] < 0
                    else 'neutral'
                ),
                'strength': abs(self.lines.normalized_bbw[0]),
                'trend_impact': self.lines.trend_strength[0]
            },
            'trend': {
                'direction': (
                    'up' if self.lines.trend_strength[0] > 0
                    else 'down'
                ),
                'strength': abs(self.lines.trend_strength[0]),
                'quality': (
                    1 - abs(self.lines.squeeze_indicator[0] - 0.5)
                )
            },
            'squeeze': {
                'level': self.lines.squeeze_indicator[0],
                'probability': (
                    1 - self.lines.squeeze_indicator[0]
                    if self.lines.squeeze_indicator[0] < 0.5
                    else self.lines.squeeze_indicator[0]
                ),
                'duration': (
                    sum(1 for x in self.bbw_history[-5:]
                        if x < np.mean(self.bbw_history))
                    if len(self.bbw_history) >= 5
                    else 0
                )
            },
            'risk': {
                'current': abs(self.lines.normalized_bbw[0]),
                'squeeze_risk': (
                    1 - self.lines.squeeze_indicator[0]
                    if self.lines.squeeze_indicator[0] < 0.5
                    else self.lines.squeeze_indicator[0]
                ),
                'trend_risk': abs(self.lines.trend_strength[0])
            }
        }
