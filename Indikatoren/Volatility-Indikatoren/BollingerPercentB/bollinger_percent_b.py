import backtrader as bt
import numpy as np

class BollingerPercentB(bt.Indicator):
    """
    Bollinger %B Indicator
    
    Ein Volatilitätsindikator, der die relative Position des Preises
    innerhalb der Bollinger Bänder misst.
    
    Features:
    - Relative Preispositionierung
    - Trendstärkeanalyse
    - Überverkauft/Überkauft-Erkennung
    - Divergenzanalyse
    
    Parameter:
    - period (20): Analysezeitraum
    - devfactor (2.0): Standardabweichungsfaktor
    - oversold (0.2): Überverkauft-Schwelle
    - overbought (0.8): Überkauft-Schwelle
    """
    
    lines = ('percent_b', 'trend_strength',
             'momentum', 'signal_line',
             'divergence')
             
    params = (
        ('period', 20),
        ('devfactor', 2.0),
        ('oversold', 0.2),
        ('overbought', 0.8)
    )
    
    plotlines = dict(
        percent_b=dict(color='blue', _name='%B'),
        trend_strength=dict(color='red', _name='Trend Strength'),
        momentum=dict(color='green', _name='Momentum'),
        signal_line=dict(color='purple', _name='Signal'),
        divergence=dict(color='orange', _name='Divergence')
    )
    
    def __init__(self):
        super(BollingerPercentB, self).__init__()
        
        # Bollinger Bands
        self.boll = bt.indicators.BollingerBands(
            period=self.p.period,
            devfactor=self.p.devfactor
        )
        
        # Historie
        self.percent_b_history = []
        self.price_history = []
        
    def calculate_percent_b(self):
        """
        Berechnet den %B-Wert.
        """
        if (self.boll.lines.top[0] - self.boll.lines.bot[0]) != 0:
            return (
                (self.data.close[0] - self.boll.lines.bot[0]) /
                (self.boll.lines.top[0] - self.boll.lines.bot[0])
            )
        return 0.5
        
    def calculate_momentum(self):
        """
        Berechnet den Momentum-Indikator.
        """
        if len(self.percent_b_history) < 2:
            return 0
            
        return (
            self.lines.percent_b[0] -
            self.lines.percent_b[-1]
        )
        
    def calculate_divergence(self):
        """
        Berechnet die Preisdivergenz.
        """
        if len(self.price_history) < self.p.period:
            return 0
            
        # Preisänderung
        price_change = (
            self.data.close[0] - self.price_history[-self.p.period]
        ) / self.price_history[-self.p.period] if self.price_history[-self.p.period] != 0 else 0
        
        # %B Änderung
        percent_b_change = (
            self.lines.percent_b[0] -
            self.percent_b_history[-self.p.period]
            if len(self.percent_b_history) >= self.p.period
            else 0
        )
        
        return np.sign(price_change) * np.sign(percent_b_change)
        
    def next(self):
        # %B berechnen
        self.lines.percent_b[0] = self.calculate_percent_b()
        self.percent_b_history.append(self.lines.percent_b[0])
        
        # Momentum
        self.lines.momentum[0] = self.calculate_momentum()
        
        # Signal-Linie (EMA von %B)
        if len(self.percent_b_history) >= self.p.period:
            self.lines.signal_line[0] = np.mean(
                self.percent_b_history[-self.p.period:]
            )
        else:
            self.lines.signal_line[0] = self.lines.percent_b[0]
            
        # Trendstärke
        if len(self.percent_b_history) >= self.p.period:
            self.lines.trend_strength[0] = abs(
                self.lines.percent_b[0] -
                self.lines.signal_line[0]
            )
        else:
            self.lines.trend_strength[0] = 0
            
        # Divergenz
        self.lines.divergence[0] = self.calculate_divergence()
        
        # Historie aktualisieren
        self.price_history.append(self.data.close[0])
        
        # Historie begrenzen
        max_period = self.p.period
        for hist in [self.percent_b_history, self.price_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'position': {
                'percent_b': self.lines.percent_b[0],
                'signal': self.lines.signal_line[0],
                'momentum': self.lines.momentum[0],
                'state': (
                    'overbought' if self.lines.percent_b[0] > self.p.overbought
                    else 'oversold' if self.lines.percent_b[0] < self.p.oversold
                    else 'neutral'
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': (
                    'up' if self.lines.momentum[0] > 0
                    else 'down'
                ),
                'persistence': (
                    np.mean([
                        1 if m > 0 else -1
                        for m in self.percent_b_history[-5:]
                    ]) if len(self.percent_b_history) >= 5
                    else 0
                )
            },
            'divergence': {
                'value': self.lines.divergence[0],
                'type': (
                    'positive' if self.lines.divergence[0] > 0
                    else 'negative' if self.lines.divergence[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.divergence[0])
            },
            'signals': {
                'overbought': self.lines.percent_b[0] > self.p.overbought,
                'oversold': self.lines.percent_b[0] < self.p.oversold,
                'crossover': (
                    'bullish' if (
                        self.lines.percent_b[0] > self.lines.signal_line[0] and
                        self.lines.percent_b[-1] <= self.lines.signal_line[-1]
                    )
                    else 'bearish' if (
                        self.lines.percent_b[0] < self.lines.signal_line[0] and
                        self.lines.percent_b[-1] >= self.lines.signal_line[-1]
                    )
                    else 'none'
                )
            },
            'risk': {
                'current': abs(self.lines.percent_b[0] - 0.5),
                'momentum_risk': abs(self.lines.momentum[0]),
                'divergence_risk': (
                    1 - abs(self.lines.divergence[0])
                    if abs(self.lines.divergence[0]) <= 1
                    else 0
                )
            }
        }
