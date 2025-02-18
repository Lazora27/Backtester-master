import backtrader as bt
import numpy as np

class ChoppinessIndex(bt.Indicator):
    """
    Choppiness Index
    
    Ein Volatilitätsindikator, der den Grad der Marktbewegung
    zwischen Trending und Choppy misst.
    
    Features:
    - Trendstärkemessung
    - Marktphasenidentifikation
    - Volatilitätsnormalisierung
    - Signalgenerierung
    
    Parameter:
    - period (14): Analysezeitraum
    - atr_period (14): ATR-Periode
    - trend_threshold (61.8): Trendschwelle
    """
    
    lines = ('ci', 'normalized_ci',
             'market_phase', 'trend_strength',
             'signal')
             
    params = (
        ('period', 14),
        ('atr_period', 14),
        ('trend_threshold', 61.8)
    )
    
    plotlines = dict(
        ci=dict(color='blue', _name='CI'),
        normalized_ci=dict(color='red', _name='Normalized CI'),
        market_phase=dict(color='green', _name='Market Phase'),
        trend_strength=dict(color='purple', _name='Trend Strength'),
        signal=dict(color='orange', _name='Signal')
    )
    
    def __init__(self):
        super(ChoppinessIndex, self).__init__()
        
        # ATR
        self.atr = bt.indicators.ATR(period=self.p.atr_period)
        
        # Historie
        self.high_history = []
        self.low_history = []
        self.ci_history = []
        
    def calculate_ci(self):
        """
        Berechnet den Choppiness Index.
        """
        if len(self.high_history) < self.p.period:
            return 50
            
        # Summe der ATR-Werte
        atr_sum = sum(
            self.atr.get(ago=-i, size=1)[0]
            for i in range(self.p.period)
        )
        
        # Höchst- und Tiefstkurse
        highest_high = max(self.high_history[-self.p.period:])
        lowest_low = min(self.low_history[-self.p.period:])
        
        if highest_high - lowest_low == 0:
            return 50
            
        # Choppiness Index
        ci = 100 * np.log10(atr_sum / (highest_high - lowest_low)) / np.log10(self.p.period)
        
        return min(100, max(0, ci))
        
    def calculate_market_phase(self):
        """
        Bestimmt die Marktphase.
        """
        if len(self.ci_history) < self.p.period:
            return 0
            
        # Durchschnittlicher CI
        avg_ci = np.mean(self.ci_history[-self.p.period:])
        
        if avg_ci > self.p.trend_threshold:
            return 1  # Choppy
        elif avg_ci < (100 - self.p.trend_threshold):
            return -1  # Trending
        return 0  # Neutral
        
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
        
        # CI-Änderung
        ci_change = (
            self.lines.ci[0] - self.lines.ci[-1]
        ) if len(self.ci_history) > 1 else 0
        
        return price_change * (1 - abs(ci_change) / 100)
        
    def next(self):
        # Historie aktualisieren
        self.high_history.append(self.data.high[0])
        self.low_history.append(self.data.low[0])
        
        # CI berechnen
        self.lines.ci[0] = self.calculate_ci()
        self.ci_history.append(self.lines.ci[0])
        
        # Normalisierter CI
        if len(self.ci_history) >= self.p.period:
            mean_ci = np.mean(self.ci_history[-self.p.period:])
            std_ci = np.std(self.ci_history[-self.p.period:])
            
            self.lines.normalized_ci[0] = (
                (self.lines.ci[0] - mean_ci) /
                std_ci if std_ci != 0 else 0
            )
        else:
            self.lines.normalized_ci[0] = 0
            
        # Marktphase
        self.lines.market_phase[0] = self.calculate_market_phase()
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Signal
        self.lines.signal[0] = (
            1 if (
                self.lines.ci[0] < (100 - self.p.trend_threshold) and
                self.lines.trend_strength[0] > 0
            )
            else -1 if (
                self.lines.ci[0] < (100 - self.p.trend_threshold) and
                self.lines.trend_strength[0] < 0
            )
            else 0
        )
        
        # Historie begrenzen
        max_period = max(self.p.period, self.p.atr_period)
        for hist in [self.high_history, self.low_history,
                    self.ci_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'choppiness': {
                'value': self.lines.ci[0],
                'normalized': self.lines.normalized_ci[0],
                'state': (
                    'choppy' if self.lines.ci[0] > self.p.trend_threshold
                    else 'trending'
                )
            },
            'market': {
                'phase': (
                    'choppy' if self.lines.market_phase[0] > 0
                    else 'trending' if self.lines.market_phase[0] < 0
                    else 'neutral'
                ),
                'strength': abs(self.lines.market_phase[0]),
                'persistence': (
                    np.mean([
                        1 if p == self.lines.market_phase[0] else 0
                        for p in self.ci_history[-5:]
                    ]) if len(self.ci_history) >= 5
                    else 0
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'quality': (
                    1 - (self.lines.ci[0] / 100)
                    if self.lines.ci[0] <= 50
                    else 0
                ),
                'reliability': (
                    1 - abs(self.lines.normalized_ci[0])
                    if abs(self.lines.normalized_ci[0]) <= 1
                    else 0
                )
            },
            'signals': {
                'current': (
                    'trend_following' if self.lines.signal[0] != 0
                    else 'range_trading'
                ),
                'strength': abs(self.lines.signal[0]),
                'confidence': (
                    1 - (self.lines.ci[0] / 100)
                    if self.lines.ci[0] <= 50
                    else 0
                )
            },
            'risk': {
                'choppiness_risk': self.lines.ci[0] / 100,
                'trend_risk': abs(self.lines.trend_strength[0]),
                'phase_risk': (
                    1 - abs(self.lines.market_phase[0])
                    if abs(self.lines.market_phase[0]) <= 1
                    else 0
                )
            }
        }
