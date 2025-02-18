import backtrader as bt
import numpy as np

class AdaptiveATR(bt.Indicator):
    """
    Adaptive Average True Range (Adaptive ATR)
    
    Ein fortgeschrittener Volatilitätsindikator, der sich dynamisch
    an Marktbedingungen anpasst und die Volatilität präziser misst.
    
    Features:
    - Adaptive Periodenberechnung
    - Volatilitätsregimeerkennung
    - Dynamische Schwellenwertanpassung
    - Trendbasierte Volatilitätsanalyse
    - Signalgenerierung
    
    Parameter:
    - base_period (14): Basis-ATR-Periode
    - vol_lookback (50): Volatilitätsrückblickperiode
    - sensitivity (2.0): Empfindlichkeit der Adaption
    - regime_threshold (0.5): Regimewechselschwelle
    """
    
    lines = ('adaptive_atr', 'normalized_atr',
             'volatility_regime', 'trend_volatility',
             'regime_change', 'buy_signal',
             'sell_signal')
             
    params = (
        ('base_period', 14),
        ('vol_lookback', 50),
        ('sensitivity', 2.0),
        ('regime_threshold', 0.5),
        ('min_period', 5),
        ('max_period', 30)
    )
    
    plotlines = dict(
        adaptive_atr=dict(color='blue', _name='Adaptive ATR'),
        normalized_atr=dict(color='red', _name='Normalized ATR'),
        volatility_regime=dict(color='green', _name='Volatility Regime'),
        trend_volatility=dict(color='purple', _name='Trend Volatility'),
        regime_change=dict(color='orange', _name='Regime Change'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(AdaptiveATR, self).__init__()
        
        # Basis-ATR
        self.base_atr = bt.indicators.ATR(
            period=self.p.base_period
        )
        
        # Historie
        self.atr_history = []
        self.regime_history = []
        self.period_history = []
        
        # Aktuelle adaptive Periode
        self.current_period = self.p.base_period
        
    def calculate_true_range(self):
        """
        Berechnet den True Range für den aktuellen Zeitpunkt.
        """
        if len(self.data) < 2:
            return self.data.high[0] - self.data.low[0]
            
        tr1 = self.data.high[0] - self.data.low[0]
        tr2 = abs(self.data.high[0] - self.data.close[-1])
        tr3 = abs(self.data.low[0] - self.data.close[-1])
        
        return max(tr1, tr2, tr3)
        
    def adapt_period(self):
        """
        Passt die ATR-Periode basierend auf Marktbedingungen an.
        """
        if len(self.atr_history) < self.p.vol_lookback:
            return self.current_period
            
        # Volatilitätsanalyse
        recent_vol = np.std(self.atr_history[-20:])
        long_vol = np.std(self.atr_history)
        
        # Volatilitätsverhältnis
        vol_ratio = (
            recent_vol / long_vol
            if long_vol > 0 else 1.0
        )
        
        # Periodenberechnung
        if vol_ratio > self.p.sensitivity:
            # Höhere Volatilität -> kürzere Periode
            new_period = max(
                self.p.min_period,
                int(self.current_period / vol_ratio)
            )
        else:
            # Niedrigere Volatilität -> längere Periode
            new_period = min(
                self.p.max_period,
                int(self.current_period * (2 - vol_ratio))
            )
            
        return new_period
        
    def calculate_regime(self):
        """
        Bestimmt das aktuelle Volatilitätsregime.
        """
        if len(self.atr_history) < self.p.vol_lookback:
            return 0
            
        # Durchschnittliche Volatilität
        avg_vol = np.mean(self.atr_history)
        
        # Aktuelle Volatilität
        current_vol = self.lines.adaptive_atr[0]
        
        # Regime bestimmen
        if current_vol > avg_vol * (1 + self.p.regime_threshold):
            regime = 1  # Hochvolatilitätsregime
        elif current_vol < avg_vol * (1 - self.p.regime_threshold):
            regime = -1  # Niedrigvolatilitätsregime
        else:
            regime = 0  # Neutrales Regime
            
        return regime
        
    def calculate_trend_volatility(self):
        """
        Berechnet die trendbasierte Volatilität.
        """
        if len(self.data) < 2:
            return 0
            
        # Preisänderung
        price_change = (
            self.data.close[0] - self.data.close[-1]
        ) / self.data.close[-1] if self.data.close[-1] != 0 else 0
        
        # Volatilitätsänderung
        vol_change = (
            self.lines.adaptive_atr[0] - self.lines.adaptive_atr[-1]
        ) / self.lines.adaptive_atr[-1] if self.lines.adaptive_atr[-1] != 0 else 0
        
        # Trendvolatilität
        trend_vol = price_change * vol_change
        
        return trend_vol
        
    def next(self):
        # True Range berechnen
        tr = self.calculate_true_range()
        
        # Periode anpassen
        self.current_period = self.adapt_period()
        
        # Adaptive ATR berechnen
        if len(self.atr_history) >= self.current_period:
            self.lines.adaptive_atr[0] = np.mean(
                self.atr_history[-self.current_period:]
            )
        else:
            self.lines.adaptive_atr[0] = tr
            
        # Normalisierte ATR
        self.lines.normalized_atr[0] = (
            self.lines.adaptive_atr[0] / self.data.close[0]
            if self.data.close[0] != 0 else 0
        )
        
        # Volatilitätsregime
        self.lines.volatility_regime[0] = self.calculate_regime()
        
        # Trendvolatilität
        self.lines.trend_volatility[0] = self.calculate_trend_volatility()
        
        # Regimewechsel
        if len(self.regime_history) > 0:
            self.lines.regime_change[0] = (
                1 if self.lines.volatility_regime[0] != self.regime_history[-1]
                else 0
            )
        else:
            self.lines.regime_change[0] = 0
            
        # Historie aktualisieren
        self.atr_history.append(tr)
        self.regime_history.append(self.lines.volatility_regime[0])
        self.period_history.append(self.current_period)
        
        # Historie begrenzen
        max_period = self.p.vol_lookback
        for hist in [self.atr_history, self.regime_history,
                    self.period_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal (Volatilitätskontraktion)
        if (self.lines.volatility_regime[0] < 0 and
            self.lines.regime_change[0] == 1 and
            self.lines.trend_volatility[0] > 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal (Volatilitätsexpansion)
        if (self.lines.volatility_regime[0] > 0 and
            self.lines.regime_change[0] == 1 and
            self.lines.trend_volatility[0] < 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'atr': {
                'value': self.lines.adaptive_atr[0],
                'normalized': self.lines.normalized_atr[0],
                'period': self.current_period,
                'adaptation': (
                    'increasing' if self.current_period > self.p.base_period
                    else 'decreasing'
                )
            },
            'volatility': {
                'regime': (
                    'high' if self.lines.volatility_regime[0] > 0
                    else 'low' if self.lines.volatility_regime[0] < 0
                    else 'neutral'
                ),
                'trend': self.lines.trend_volatility[0],
                'stability': (
                    1 - abs(
                        np.std(self.atr_history) /
                        np.mean(self.atr_history)
                    ) if len(self.atr_history) > 0 and
                    np.mean(self.atr_history) > 0
                    else 0
                )
            },
            'regime': {
                'current': self.lines.volatility_regime[0],
                'change': self.lines.regime_change[0],
                'persistence': (
                    np.mean([
                        1 if r == self.lines.volatility_regime[0] else 0
                        for r in self.regime_history[-10:]
                    ]) if len(self.regime_history) >= 10
                    else 0
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(self.lines.volatility_regime[0]),
                'reliability': (
                    abs(self.lines.volatility_regime[0]) *
                    (1 - abs(self.lines.trend_volatility[0]))
                )
            },
            'risk': {
                'current': self.lines.normalized_atr[0],
                'regime_risk': abs(self.lines.volatility_regime[0]),
                'adaptation_risk': abs(
                    self.current_period - self.p.base_period
                ) / self.p.base_period
            }
        }
