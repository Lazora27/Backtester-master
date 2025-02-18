import backtrader as bt
import numpy as np

class UlcerIndexVolume(bt.Indicator):
    """
    Ulcer Index Volume Variant
    
    Eine volumengewichtete Variante des Ulcer Index, die
    Drawdowns unter Berücksichtigung des Handelsvolumens misst.
    
    Features:
    - Drawdown-Analyse
    - Volumengewichtung
    - Risikomessung
    - Trendstärkeberechnung
    - Signalgenerierung
    
    Parameter:
    - period (14): Analysezeitraum
    - volume_factor (1.0): Volumenfaktor
    - smoothing_period (3): Glättungsperiode
    """
    
    lines = ('uiv', 'smoothed_uiv',
             'volume_impact', 'risk_level',
             'trend_quality', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 14),
        ('volume_factor', 1.0),
        ('smoothing_period', 3),
        ('risk_threshold', 0.3)
    )
    
    plotlines = dict(
        uiv=dict(color='blue', _name='UIV'),
        smoothed_uiv=dict(color='red', _name='Smoothed UIV'),
        volume_impact=dict(color='green', _name='Volume Impact'),
        risk_level=dict(color='purple', _name='Risk Level'),
        trend_quality=dict(color='orange', _name='Trend Quality'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(UlcerIndexVolume, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.uiv_history = []
        self.price_history = []
        self.volume_history = []
        
    def calculate_uiv(self):
        """
        Berechnet den Ulcer Index Volume.
        """
        if len(self.price_history) < self.p.period:
            return 0
            
        # Maximaler Preis im Zeitraum
        max_price = max(self.price_history[-self.p.period:])
        
        # Volumengewichtung
        volume_weight = (
            self.data.volume[0] ** self.p.volume_factor
        )
        
        # Drawdown berechnen
        if max_price > 0:
            drawdown = (
                (max_price - self.data.close[0]) /
                max_price * 100
            )
        else:
            drawdown = 0
            
        # Volumengewichteter Drawdown
        weighted_drawdown = drawdown * volume_weight
        
        # Quadrierter Drawdown
        squared_drawdown = weighted_drawdown ** 2
        
        # Ulcer Index berechnen
        if len(self.uiv_history) >= self.p.period:
            uiv = np.sqrt(
                np.mean([
                    d ** 2 for d in self.uiv_history[-self.p.period:]
                ] + [squared_drawdown])
            )
        else:
            uiv = np.sqrt(squared_drawdown)
            
        return uiv
        
    def calculate_volume_impact(self):
        """
        Berechnet den Volumeneinfluss.
        """
        if len(self.volume_history) < self.p.period:
            return 0
            
        # Durchschnittliches Volumen
        avg_volume = np.mean(self.volume_history[-self.p.period:])
        
        # Volumeneinfluss
        if avg_volume > 0:
            impact = (
                self.data.volume[0] / avg_volume - 1
            )
        else:
            impact = 0
            
        return impact
        
    def calculate_risk_level(self):
        """
        Berechnet das Risikolevel.
        """
        if len(self.uiv_history) < self.p.period:
            return 0
            
        # Durchschnittlicher UIV
        avg_uiv = np.mean(self.uiv_history[-self.p.period:])
        
        # Risikolevel
        if avg_uiv > 0:
            risk = self.lines.uiv[0] / avg_uiv
        else:
            risk = 1.0
            
        return risk
        
    def calculate_trend_quality(self):
        """
        Berechnet die Trendqualität.
        """
        if len(self.price_history) < self.p.period:
            return 0
            
        # Preisänderung
        price_change = (
            self.data.close[0] - self.price_history[-self.p.period]
        ) / self.price_history[-self.p.period]
        
        # Trendqualität
        quality = price_change * (1 - self.lines.risk_level[0])
        
        return quality
        
    def next(self):
        # UIV berechnen
        self.lines.uiv[0] = self.calculate_uiv()
        self.uiv_history.append(self.lines.uiv[0])
        
        # Geglätteter UIV
        self.lines.smoothed_uiv[0] = bt.indicators.EMA(
            self.lines.uiv, period=self.p.smoothing_period
        )[0]
        
        # Volumeneinfluss
        self.lines.volume_impact[0] = self.calculate_volume_impact()
        
        # Risikolevel
        self.lines.risk_level[0] = self.calculate_risk_level()
        
        # Trendqualität
        self.lines.trend_quality[0] = self.calculate_trend_quality()
        
        # Historie aktualisieren
        self.price_history.append(self.data.close[0])
        self.volume_history.append(self.data.volume[0])
        
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.smoothing_period
        )
        for hist in [self.uiv_history, self.price_history,
                    self.volume_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_uiv[0] < self.p.risk_threshold and
            self.lines.volume_impact[0] > 0 and
            self.lines.trend_quality[0] > 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_uiv[0] > self.p.risk_threshold and
            self.lines.volume_impact[0] < 0 and
            self.lines.trend_quality[0] < 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'ulcer_index': {
                'current': self.lines.uiv[0],
                'smoothed': self.lines.smoothed_uiv[0],
                'trend': (
                    'improving' if self.lines.uiv[0] < self.lines.uiv[-1]
                    else 'deteriorating'
                )
            },
            'volume': {
                'impact': self.lines.volume_impact[0],
                'significance': (
                    'high' if abs(self.lines.volume_impact[0]) > 0.5
                    else 'low'
                ),
                'trend': (
                    'supportive' if self.lines.volume_impact[0] > 0
                    else 'restrictive'
                )
            },
            'risk': {
                'level': self.lines.risk_level[0],
                'state': (
                    'high' if self.lines.risk_level[0] > 1.0
                    else 'moderate' if self.lines.risk_level[0] > 0.5
                    else 'low'
                ),
                'trend': (
                    'increasing' if self.lines.risk_level[0] > self.lines.risk_level[-1]
                    else 'decreasing'
                )
            },
            'trend': {
                'quality': self.lines.trend_quality[0],
                'strength': abs(self.lines.trend_quality[0]),
                'reliability': (
                    'high' if self.lines.risk_level[0] < 0.5
                    else 'moderate' if self.lines.risk_level[0] < 1.0
                    else 'low'
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': 1 - self.lines.risk_level[0],
                'reliability': (
                    (1 - self.lines.risk_level[0]) *
                    abs(self.lines.volume_impact[0])
                )
            },
            'metrics': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'drawdown': self.lines.uiv[0],
                'risk_adjusted_return': (
                    self.lines.trend_quality[0] /
                    (1 + self.lines.risk_level[0])
                    if self.lines.risk_level[0] > 0
                    else 0
                )
            }
        }
