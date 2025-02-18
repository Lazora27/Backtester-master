import backtrader as bt
import numpy as np

class DynamicMomentumIndex(bt.Indicator):
    """
    Dynamic Momentum Index (DMI)
    
    Ein adaptiver Momentum-Indikator, der die Periode basierend auf
    der Marktvolatilität dynamisch anpasst.
    
    Features:
    - Adaptive Periodenberechnung
    - Volatilitätsbasierte Anpassung
    - Momentum-Analyse
    - Überkauft/Überverkauft Zonen
    - Signal-Validierung
    
    Parameter:
    - base_period (14): Basis RSI Periode
    - vol_factor (1.0): Volatilitätsfaktor
    - smooth_period (5): Glättungsperiode
    - upper_threshold (70): Obere Schwelle
    - lower_threshold (30): Untere Schwelle
    """
    
    lines = ('dmi', 'dynamic_period', 'volatility',
             'upper', 'lower', 'signal',
             'buy_signal', 'sell_signal')
             
    params = (
        ('base_period', 14),
        ('vol_factor', 1.0),
        ('smooth_period', 5),
        ('upper_threshold', 70),
        ('lower_threshold', 30)
    )
    
    plotlines = dict(
        dmi=dict(color='blue', _name='DMI'),
        dynamic_period=dict(color='gray', _name='Dynamic Period'),
        volatility=dict(color='red', _name='Volatility'),
        upper=dict(color='green', _name='Upper'),
        lower=dict(color='red', _name='Lower'),
        signal=dict(color='orange', _name='Signal'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(DynamicMomentumIndex, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Glättung
        self.ema = bt.indicators.EMA(period=self.p.smooth_period)
        
        # Historie
        self.dmi_history = []
        self.period_history = []
        self.gains = []
        self.losses = []
        
    def calculate_dynamic_period(self):
        """
        Berechnet die dynamische Periode basierend auf Volatilität.
        """
        if len(self.data) < 20:
            return self.p.base_period
            
        # Volatilitätsberechnung
        vol = self.vol[0]
        if vol == 0:
            return self.p.base_period
            
        # Normalisierte Volatilität
        norm_vol = vol / self.data[0] if self.data[0] != 0 else 1
        
        # Dynamische Periode
        dynamic_period = int(
            self.p.base_period *
            (1 + self.p.vol_factor * norm_vol)
        )
        
        # Begrenzung
        return max(5, min(50, dynamic_period))
        
    def calculate_momentum(self, period):
        """
        Berechnet den Momentum-Wert für eine gegebene Periode.
        """
        if len(self.data) < period:
            return 50
            
        gains = []
        losses = []
        
        for i in range(period):
            change = self.data[-i] - self.data[-i-1]
            if change >= 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))
                
        avg_gain = sum(gains) / period
        avg_loss = sum(losses) / period
        
        if avg_loss == 0:
            return 100
            
        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))
        
    def next(self):
        # Dynamische Periode berechnen
        period = self.calculate_dynamic_period()
        self.lines.dynamic_period[0] = period
        
        # Volatilität
        self.lines.volatility[0] = self.vol[0] / self.data[0] if self.data[0] != 0 else 0
        
        # DMI berechnen
        self.lines.dmi[0] = self.calculate_momentum(period)
        
        # Geglätteter DMI
        smoothed_dmi = self.ema(self.lines.dmi)
        
        # Signal-Linie
        self.lines.signal[0] = smoothed_dmi[0]
        
        # Schwellen
        self.lines.upper[0] = self.p.upper_threshold
        self.lines.lower[0] = self.p.lower_threshold
        
        # Historie aktualisieren
        self.dmi_history.append(self.lines.dmi[0])
        self.period_history.append(period)
        
        if len(self.dmi_history) > self.p.base_period:
            self.dmi_history.pop(0)
            self.period_history.pop(0)
            
        # Signal-Generierung
        # Buy Signal
        if (self.lines.dmi[0] < self.p.lower_threshold and
            self.lines.dmi[0] > self.lines.signal[0] and
            self.lines.volatility[0] < 0.02):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.dmi[0] > self.p.upper_threshold and
            self.lines.dmi[0] < self.lines.signal[0] and
            self.lines.volatility[0] < 0.02):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'dmi': {
                'current': self.lines.dmi[0],
                'signal': self.lines.signal[0],
                'period': self.lines.dynamic_period[0],
                'volatility': self.lines.volatility[0]
            },
            'trend': {
                'direction': (
                    'up' if self.lines.dmi[0] > self.lines.signal[0]
                    else 'down'
                ),
                'strength': abs(
                    self.lines.dmi[0] - self.lines.signal[0]
                ),
                'momentum': (
                    self.lines.dmi[0] - self.dmi_history[-2]
                    if len(self.dmi_history) > 1
                    else 0
                )
            },
            'conditions': {
                'overbought': self.lines.dmi[0] > self.p.upper_threshold,
                'oversold': self.lines.dmi[0] < self.p.lower_threshold,
                'volatility': (
                    'high' if self.lines.volatility[0] > 0.02
                    else 'normal' if self.lines.volatility[0] > 0.01
                    else 'low'
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(
                    self.lines.dmi[0] - 50
                ) / 50,
                'reliability': (
                    (1 - self.lines.volatility[0]) *
                    abs(self.lines.dmi[0] - self.lines.signal[0]) / 100
                )
            },
            'statistics': {
                'avg_period': np.mean(self.period_history) if self.period_history else 0,
                'period_stability': np.std(self.period_history) if self.period_history else 0,
                'dmi_volatility': np.std(self.dmi_history) if self.dmi_history else 0
            }
        }
