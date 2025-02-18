import backtrader as bt
import numpy as np

class MassIndex(bt.Indicator):
    """
    Mass Index
    
    Ein Indikator, der Trendwenden durch die Analyse
    der Preisreichweite identifiziert.
    
    Features:
    - Trendwendenerkennung
    - Volatilitätsanalyse
    - Preisbereichsanalyse
    - Trendstärkeberechnung
    - Signal-Validierung
    
    Parameter:
    - ema_period (9): EMA-Periode für Preisbereich
    - mass_period (25): Periode für Mass Index
    - reversal_bulge (27): Schwellenwert für Trendwende
    """
    
    lines = ('mass_index', 'smoothed_mass',
             'range_ratio', 'volatility',
             'trend_strength', 'buy_signal',
             'sell_signal')
             
    params = (
        ('ema_period', 9),
        ('mass_period', 25),
        ('reversal_bulge', 27),
        ('min_strength', 0.3)
    )
    
    plotlines = dict(
        mass_index=dict(color='blue', _name='Mass Index'),
        smoothed_mass=dict(color='red', _name='Smoothed Mass'),
        range_ratio=dict(color='green', _name='Range Ratio'),
        volatility=dict(color='purple', _name='Volatility'),
        trend_strength=dict(color='orange', _name='Trend Strength'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(MassIndex, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.ema_period)
        self.vol = bt.indicators.StdDev(period=self.p.ema_period)
        
        # Historie
        self.mass_history = []
        self.range_history = []
        self.ratio_history = []
        
    def calculate_mass_index(self):
        """
        Berechnet den Mass Index.
        """
        if len(self.data) < self.p.ema_period:
            return 0
            
        # Preisbereich
        high_low_range = self.data.high[0] - self.data.low[0]
        
        # Erster EMA
        ema1 = bt.indicators.EMA(
            high_low_range, period=self.p.ema_period
        )[0]
        
        # Zweiter EMA
        ema2 = bt.indicators.EMA(
            ema1, period=self.p.ema_period
        )[0]
        
        # Range Ratio
        if ema2 != 0:
            range_ratio = ema1 / ema2
        else:
            range_ratio = 1.0
            
        self.ratio_history.append(range_ratio)
        
        # Mass Index
        if len(self.ratio_history) >= self.p.mass_period:
            mass_index = sum(self.ratio_history[-self.p.mass_period:])
        else:
            mass_index = 0
            
        return mass_index
        
    def calculate_volatility(self):
        """
        Berechnet die Volatilität.
        """
        if len(self.range_history) < self.p.ema_period:
            return 0
            
        # Volatilität des Preisbereichs
        volatility = np.std(self.range_history[-self.p.ema_period:])
        
        # Normalisierung
        if self.data.close[0] != 0:
            volatility = volatility / self.data.close[0]
            
        return volatility
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.mass_history) < self.p.mass_period:
            return 0
            
        # Trendstärke basierend auf Mass Index
        trend_strength = abs(
            self.mass_history[-1] - np.mean(self.mass_history)
        ) / np.std(self.mass_history) if len(self.mass_history) > 1 else 0
        
        return trend_strength
        
    def next(self):
        # Mass Index berechnen
        self.lines.mass_index[0] = self.calculate_mass_index()
        self.mass_history.append(self.lines.mass_index[0])
        
        # Geglätteter Mass Index
        self.lines.smoothed_mass[0] = bt.indicators.EMA(
            self.lines.mass_index, period=self.p.ema_period
        )[0]
        
        # Range Ratio
        if len(self.ratio_history) > 0:
            self.lines.range_ratio[0] = self.ratio_history[-1]
        else:
            self.lines.range_ratio[0] = 1.0
            
        # Volatilität
        self.lines.volatility[0] = self.calculate_volatility()
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Historie aktualisieren
        self.range_history.append(
            self.data.high[0] - self.data.low[0]
        )
        
        # Historie begrenzen
        max_period = max(
            self.p.ema_period,
            self.p.mass_period
        )
        for hist in [self.mass_history, self.range_history,
                    self.ratio_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.mass_index[0] > self.p.reversal_bulge and
            self.lines.mass_index[-1] <= self.p.reversal_bulge and
            self.lines.trend_strength[0] > self.p.min_strength):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.mass_index[0] < self.p.reversal_bulge and
            self.lines.mass_index[-1] >= self.p.reversal_bulge and
            self.lines.trend_strength[0] > self.p.min_strength):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'mass_index': {
                'current': self.lines.mass_index[0],
                'smoothed': self.lines.smoothed_mass[0],
                'trend': (
                    'reversal likely' if self.lines.mass_index[0] > self.p.reversal_bulge
                    else 'trend continuing'
                )
            },
            'range': {
                'ratio': self.lines.range_ratio[0],
                'volatility': self.lines.volatility[0],
                'stability': (
                    np.std(self.range_history)
                    if len(self.range_history) > 1
                    else 0
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'persistence': (
                    np.mean([
                        1 if m > self.p.reversal_bulge
                        else -1
                        for m in self.mass_history[-5:]
                    ]) if len(self.mass_history) >= 5
                    else 0
                ),
                'phase': (
                    'expansion' if self.lines.mass_index[0] > self.lines.mass_index[-1]
                    else 'contraction'
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    abs(self.lines.mass_index[0] - self.p.reversal_bulge) *
                    self.lines.trend_strength[0]
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'range_risk': self.lines.volatility[0],
                'reversal_risk': (
                    abs(self.lines.mass_index[0] - self.p.reversal_bulge) /
                    self.p.reversal_bulge
                )
            }
        }
