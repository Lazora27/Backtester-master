import backtrader as bt
import numpy as np

class CoppockCurve(bt.Indicator):
    """
    Coppock Curve Indicator
    
    Ein langfristiger Momentum-Indikator, der hauptsächlich für die Identifizierung
    von wichtigen Marktböden verwendet wird. Entwickelt von Edwin Coppock.
    
    Features:
    - Klassische Coppock Berechnung
    - Adaptive Periodenlängen
    - Trend-Stärke Analyse
    - Signal-Generierung
    - Multi-Timeframe Integration
    
    Parameter:
    - wma_period (10): Periode für Weighted Moving Average
    - roc1_period (14): Erste Rate of Change Periode
    - roc2_period (11): Zweite Rate of Change Periode
    - signal_period (5): Signalgenerierungs-Periode
    - threshold (0.0): Signal-Schwelle
    """
    
    lines = ('coppock', 'signal', 'trend_strength',
             'buy_signal', 'sell_signal', 'divergence')
             
    params = (
        ('wma_period', 10),
        ('roc1_period', 14),
        ('roc2_period', 11),
        ('signal_period', 5),
        ('threshold', 0.0)
    )
    
    plotlines = dict(
        coppock=dict(color='blue', _name='Coppock'),
        signal=dict(color='red', _name='Signal'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v'),
        divergence=dict(_name='Divergence', color='purple', marker='o')
    )
    
    def __init__(self):
        super(CoppockCurve, self).__init__()
        
        # ROC Berechnung
        self.roc1 = bt.indicators.RateOfChange(
            period=self.p.roc1_period
        )
        self.roc2 = bt.indicators.RateOfChange(
            period=self.p.roc2_period
        )
        
        # Gleitende Durchschnitte
        self.wma = bt.indicators.WMA(period=self.p.wma_period)
        self.signal_ma = bt.indicators.SMA(
            period=self.p.signal_period
        )
        
        # Historie für Divergenz-Analyse
        self.coppock_history = []
        self.price_history = []
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke basierend auf Coppock-Werten.
        """
        if len(self.coppock_history) < 2:
            return 0
            
        # Momentum der Coppock Curve
        momentum = (self.lines.coppock[0] -
                   self.lines.coppock[-1])
                   
        # Relative Stärke
        max_cop = max(self.coppock_history[-10:])
        min_cop = min(self.coppock_history[-10:])
        range_cop = max_cop - min_cop
        
        if range_cop != 0:
            relative_pos = ((self.lines.coppock[0] - min_cop) /
                          range_cop)
        else:
            relative_pos = 0.5
            
        # Kombinierte Stärke
        strength = (0.7 * relative_pos +
                   0.3 * (1 if momentum > 0 else 0))
                   
        return max(min(strength, 1), 0)
        
    def check_divergence(self):
        """
        Überprüft auf Divergenzen zwischen Preis und Coppock Curve.
        """
        if len(self.coppock_history) < 20:
            return False
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-20:-1])
        price_low = min(self.price_history[-20:-1])
        current_price = self.price_history[-1]
        
        # Coppock Hochs/Tiefs
        cop_high = max(self.coppock_history[-20:-1])
        cop_low = min(self.coppock_history[-20:-1])
        current_cop = self.coppock_history[-1]
        
        # Bearish Divergenz
        if (current_price > price_high and
            current_cop < cop_high):
            return -1
            
        # Bullish Divergenz
        if (current_price < price_low and
            current_cop > cop_low):
            return 1
            
        return 0
        
    def next(self):
        # Coppock Curve berechnen
        roc_sum = self.roc1[0] + self.roc2[0]
        self.lines.coppock[0] = self.wma(roc_sum)[0]
        
        # Signal Line
        self.lines.signal[0] = self.signal_ma(self.lines.coppock)[0]
        
        # Historie aktualisieren
        self.coppock_history.append(self.lines.coppock[0])
        self.price_history.append(self.data.close[0])
        
        if len(self.coppock_history) > 50:  # Limit history
            self.coppock_history.pop(0)
            self.price_history.pop(0)
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Signal-Generierung
        # Buy Signal
        if (self.lines.coppock[0] > self.lines.signal[0] and
            self.lines.coppock[0] > self.p.threshold and
            self.lines.trend_strength[0] > 0.6):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.coppock[0] < self.lines.signal[0] and
            self.lines.coppock[0] < -self.p.threshold and
            self.lines.trend_strength[0] > 0.6):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
        # Divergenz Check
        div = self.check_divergence()
        if div != 0:
            self.lines.divergence[0] = (
                self.data.low[0] if div > 0
                else self.data.high[0]
            )
        else:
            self.lines.divergence[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'coppock': {
                'value': self.lines.coppock[0],
                'signal': self.lines.signal[0],
                'trend_strength': self.lines.trend_strength[0]
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'divergence': self.lines.divergence[0] != float('nan')
            },
            'trend_analysis': {
                'direction': ('up' if self.lines.coppock[0] > 0
                            else 'down'),
                'momentum': (self.lines.coppock[0] -
                           self.lines.coppock[-1]),
                'strength': self.lines.trend_strength[0]
            },
            'market_state': {
                'overbought': self.lines.coppock[0] > 10,
                'oversold': self.lines.coppock[0] < -10,
                'trend_confirmed': (self.lines.coppock[0] *
                                  self.lines.trend_strength[0] > 0)
            }
        }
