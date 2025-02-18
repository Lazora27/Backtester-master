import backtrader as bt
import numpy as np

class HistoricalATR(bt.Indicator):
    """
    Historical Average True Range (HATR)
    
    Ein erweiterter ATR-Indikator, der historische Volatilitätsmuster
    und deren Entwicklung analysiert.
    
    Features:
    - Historische ATR-Analyse
    - Volatilitätsregimeerkennung
    - Trendstärkeberechnung
    - Signalgenerierung
    
    Parameter:
    - period (14): ATR-Periode
    - hist_period (50): Historische Analyseperiode
    - regime_threshold (0.5): Regimewechselschwelle
    """
    
    lines = ('hatr', 'normalized_hatr',
             'volatility_regime', 'trend_strength',
             'signal')
             
    params = (
        ('period', 14),
        ('hist_period', 50),
        ('regime_threshold', 0.5)
    )
    
    plotlines = dict(
        hatr=dict(color='blue', _name='HATR'),
        normalized_hatr=dict(color='red', _name='Normalized HATR'),
        volatility_regime=dict(color='green', _name='Volatility Regime'),
        trend_strength=dict(color='purple', _name='Trend Strength'),
        signal=dict(color='orange', _name='Signal')
    )
    
    def __init__(self):
        super(HistoricalATR, self).__init__()
        
        # Basis-ATR
        self.atr = bt.indicators.ATR(period=self.p.period)
        
        # Historie
        self.atr_history = []
        self.regime_history = []
        
    def calculate_true_range(self):
        """
        Berechnet den True Range.
        """
        if len(self.data) < 2:
            return self.data.high[0] - self.data.low[0]
            
        tr1 = self.data.high[0] - self.data.low[0]
        tr2 = abs(self.data.high[0] - self.data.close[-1])
        tr3 = abs(self.data.low[0] - self.data.close[-1])
        
        return max(tr1, tr2, tr3)
        
    def calculate_regime(self):
        """
        Bestimmt das Volatilitätsregime.
        """
        if len(self.atr_history) < self.p.hist_period:
            return 0
            
        # Durchschnittliche Volatilität
        avg_vol = np.mean(self.atr_history)
        
        # Aktuelle Volatilität
        current_vol = self.lines.hatr[0]
        
        if current_vol > avg_vol * (1 + self.p.regime_threshold):
            regime = 1  # Hochvolatilitätsregime
        elif current_vol < avg_vol * (1 - self.p.regime_threshold):
            regime = -1  # Niedrigvolatilitätsregime
        else:
            regime = 0  # Neutrales Regime
            
        return regime
        
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
        
        # ATR-Änderung
        atr_change = (
            self.lines.hatr[0] - self.lines.hatr[-1]
        ) / self.lines.hatr[-1] if self.lines.hatr[-1] != 0 else 0
        
        return price_change * (1 + abs(atr_change))
        
    def next(self):
        # True Range berechnen
        tr = self.calculate_true_range()
        
        # HATR berechnen
        if len(self.atr_history) >= self.p.period:
            self.lines.hatr[0] = np.mean(
                self.atr_history[-self.p.period:]
            )
        else:
            self.lines.hatr[0] = tr
            
        self.atr_history.append(tr)
        
        # Normalisierte HATR
        if len(self.atr_history) >= self.p.hist_period:
            mean_atr = np.mean(self.atr_history[-self.p.hist_period:])
            std_atr = np.std(self.atr_history[-self.p.hist_period:])
            
            self.lines.normalized_hatr[0] = (
                (self.lines.hatr[0] - mean_atr) /
                std_atr if std_atr != 0 else 0
            )
        else:
            self.lines.normalized_hatr[0] = 0
            
        # Volatilitätsregime
        self.lines.volatility_regime[0] = self.calculate_regime()
        self.regime_history.append(self.lines.volatility_regime[0])
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Signal
        self.lines.signal[0] = (
            1 if (
                self.lines.volatility_regime[0] < 0 and
                self.lines.trend_strength[0] > 0
            )
            else -1 if (
                self.lines.volatility_regime[0] < 0 and
                self.lines.trend_strength[0] < 0
            )
            else 0
        )
        
        # Historie begrenzen
        max_period = max(self.p.period, self.p.hist_period)
        for hist in [self.atr_history, self.regime_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'volatility': {
                'current': self.lines.hatr[0],
                'normalized': self.lines.normalized_hatr[0],
                'regime': (
                    'high' if self.lines.volatility_regime[0] > 0
                    else 'low' if self.lines.volatility_regime[0] < 0
                    else 'normal'
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': (
                    'up' if self.lines.trend_strength[0] > 0
                    else 'down'
                ),
                'quality': (
                    1 - abs(self.lines.normalized_hatr[0])
                    if abs(self.lines.normalized_hatr[0]) <= 1
                    else 0
                )
            },
            'regime': {
                'current': self.lines.volatility_regime[0],
                'persistence': (
                    np.mean([
                        1 if r == self.lines.volatility_regime[0]
                        else 0
                        for r in self.regime_history[-10:]
                    ]) if len(self.regime_history) >= 10
                    else 0
                ),
                'stability': (
                    1 - np.std(self.regime_history[-10:])
                    if len(self.regime_history) >= 10
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
                    abs(self.lines.trend_strength[0]) *
                    (1 - abs(self.lines.normalized_hatr[0]))
                    if abs(self.lines.normalized_hatr[0]) <= 1
                    else 0
                )
            },
            'risk': {
                'volatility_risk': abs(self.lines.normalized_hatr[0]),
                'regime_risk': abs(self.lines.volatility_regime[0]),
                'trend_risk': (
                    1 - abs(self.lines.trend_strength[0])
                    if abs(self.lines.trend_strength[0]) <= 1
                    else 0
                )
            }
        }
