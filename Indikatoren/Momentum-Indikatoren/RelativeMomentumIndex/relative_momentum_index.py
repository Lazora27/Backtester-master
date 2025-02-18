import backtrader as bt
import numpy as np

class RelativeMomentumIndex(bt.Indicator):
    """
    Relative Momentum Index (RMI)
    
    Eine Variante des RSI, die Momentum-basierte Preisänderungen
    über einen bestimmten Zeitraum berücksichtigt.
    
    Features:
    - Momentum-basierte RSI-Berechnung
    - Adaptive Glättung
    - Trendstärke-Analyse
    - Divergenz-Erkennung
    - Signal-Validierung
    
    Parameter:
    - period (14): Basisperiode
    - momentum_period (3): Momentum-Periode
    - smooth_period (10): Glättungsperiode
    - upper_band (70): Obere Schwelle
    - lower_band (30): Untere Schwelle
    """
    
    lines = ('rmi', 'smoothed_rmi',
             'momentum', 'trend_strength',
             'divergence', 'upper', 'lower',
             'buy_signal', 'sell_signal')
             
    params = (
        ('period', 14),
        ('momentum_period', 3),
        ('smooth_period', 10),
        ('upper_band', 70),
        ('lower_band', 30)
    )
    
    plotlines = dict(
        rmi=dict(color='blue', _name='RMI'),
        smoothed_rmi=dict(color='red', _name='Smoothed RMI'),
        momentum=dict(color='green', _name='Momentum'),
        trend_strength=dict(color='purple', _name='Trend Strength'),
        divergence=dict(color='orange', _name='Divergence'),
        upper=dict(color='gray', _name='Upper'),
        lower=dict(color='gray', _name='Lower'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(RelativeMomentumIndex, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Historie
        self.rmi_history = []
        self.momentum_history = []
        self.price_history = []
        
    def calculate_momentum(self):
        """
        Berechnet den Momentum-Wert.
        """
        if len(self.price_history) <= self.p.momentum_period:
            return 0
            
        return self.price_history[-1] - self.price_history[-self.p.momentum_period-1]
        
    def calculate_rmi(self):
        """
        Berechnet den RMI-Wert.
        """
        if len(self.momentum_history) < self.p.period:
            return 50
            
        gains = sum(
            m for m in self.momentum_history[-self.p.period:]
            if m > 0
        )
        losses = abs(sum(
            m for m in self.momentum_history[-self.p.period:]
            if m < 0
        ))
        
        if losses == 0:
            return 100 if gains > 0 else 50
            
        rs = gains / losses
        return 100 - (100 / (1 + rs))
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.rmi_history) < 2:
            return 0
            
        # RMI-Momentum
        momentum = self.rmi_history[-1] - self.rmi_history[-2]
        
        # Relative Stärke
        strength = abs(momentum)
        if self.data[0] != 0:
            strength = strength / self.data[0]
            
        return min(1.0, strength)
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und RMI.
        """
        if len(self.price_history) < self.p.period or len(self.rmi_history) < self.p.period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.period:])
        price_low = min(self.price_history[-self.p.period:])
        
        # RMI-Hochs/-Tiefs
        rmi_high = max(self.rmi_history[-self.p.period:])
        rmi_low = min(self.rmi_history[-self.p.period:])
        
        # Bullische Divergenz
        if price_low < price_high and rmi_low > rmi_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and rmi_low < rmi_high:
            return -1
            
        return 0
        
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.data[0])
        
        # Momentum berechnen
        momentum = self.calculate_momentum()
        self.momentum_history.append(momentum)
        self.lines.momentum[0] = momentum
        
        # RMI berechnen
        self.lines.rmi[0] = self.calculate_rmi()
        self.rmi_history.append(self.lines.rmi[0])
        
        # Geglätteter RMI
        self.lines.smoothed_rmi[0] = bt.indicators.EMA(
            self.lines.rmi, period=self.p.smooth_period
        )[0]
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Bänder
        self.lines.upper[0] = self.p.upper_band
        self.lines.lower[0] = self.p.lower_band
        
        # Historie begrenzen
        max_period = max(self.p.period, self.p.momentum_period)
        for hist in [self.rmi_history, self.momentum_history, self.price_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_rmi[0] < self.p.lower_band and
            self.lines.momentum[0] > 0 and
            self.lines.trend_strength[0] > 0.3 and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_rmi[0] > self.p.upper_band and
            self.lines.momentum[0] < 0 and
            self.lines.trend_strength[0] > 0.3 and
            self.lines.divergence[0] <= 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'momentum': {
                'rmi': self.lines.rmi[0],
                'smoothed': self.lines.smoothed_rmi[0],
                'raw': self.lines.momentum[0],
                'trend_strength': self.lines.trend_strength[0]
            },
            'trend': {
                'direction': np.sign(self.lines.momentum[0]),
                'strength': abs(self.lines.momentum[0]),
                'consistency': (
                    np.mean([
                        1 if np.sign(m) == np.sign(self.lines.momentum[0])
                        else 0
                        for m in self.momentum_history[-5:]
                    ]) if len(self.momentum_history) >= 5
                    else 0
                )
            },
            'divergence': {
                'type': (
                    'bullish' if self.lines.divergence[0] > 0
                    else 'bearish' if self.lines.divergence[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.divergence[0])
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    self.lines.trend_strength[0] *
                    (1 + abs(self.lines.divergence[0])) *
                    abs(self.lines.momentum[0])
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'momentum_stability': (
                    np.std(self.momentum_history)
                    if len(self.momentum_history) > 1
                    else 0
                ),
                'rmi_stability': (
                    np.std(self.rmi_history)
                    if len(self.rmi_history) > 1
                    else 0
                )
            }
        }
