import backtrader as bt
import numpy as np

class StochasticMomentumIndex(bt.Indicator):
    """
    Stochastic Momentum Index (SMI)
    
    Ein fortgeschrittener Momentum-Indikator, der die Position des
    Schlusskurses relativ zur Mitte des Hochs/Tiefs-Bereichs misst.
    
    Features:
    - Doppelte Glättung
    - Signallinie
    - Trendstärke-Analyse
    - Divergenz-Erkennung
    - Signal-Validierung
    
    Parameter:
    - period (14): Basisperiode
    - smooth_period1 (25): Erste Glättungsperiode
    - smooth_period2 (13): Zweite Glättungsperiode
    - signal_period (9): Signallinien-Periode
    """
    
    lines = ('smi', 'signal', 'histogram',
             'trend_strength', 'divergence',
             'upper', 'lower', 'mid',
             'buy_signal', 'sell_signal')
             
    params = (
        ('period', 14),
        ('smooth_period1', 25),
        ('smooth_period2', 13),
        ('signal_period', 9),
        ('upper_threshold', 40),
        ('lower_threshold', -40)
    )
    
    plotlines = dict(
        smi=dict(color='blue', _name='SMI'),
        signal=dict(color='red', _name='Signal'),
        histogram=dict(color='green', _name='Histogram'),
        trend_strength=dict(color='purple', _name='Trend Strength'),
        divergence=dict(color='orange', _name='Divergence'),
        upper=dict(color='gray', _name='Upper'),
        lower=dict(color='gray', _name='Lower'),
        mid=dict(color='gray', _name='Mid'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(StochasticMomentumIndex, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Historie
        self.smi_history = []
        self.price_history = []
        self.histogram_history = []
        
    def calculate_smi(self):
        """
        Berechnet den SMI-Wert.
        """
        if len(self.price_history) < self.p.period:
            return 0
            
        # Hochs und Tiefs
        highs = [max(self.data.high.get(ago=i, size=self.p.period))
                for i in range(self.p.period)]
        lows = [min(self.data.low.get(ago=i, size=self.p.period))
               for i in range(self.p.period)]
               
        # Median und Differenz
        median = [(h + l) / 2 for h, l in zip(highs, lows)]
        diff = self.data.close[0] - sum(median) / len(median)
        
        # Range
        range_sum = sum(h - l for h, l in zip(highs, lows))
        if range_sum == 0:
            return 0
            
        # Erste Glättung
        smoothed1 = bt.indicators.EMA(
            bt.indicators.EMA(
                diff, period=self.p.smooth_period1
            ),
            period=self.p.smooth_period2
        )[0]
        
        # Zweite Glättung
        smoothed2 = bt.indicators.EMA(
            bt.indicators.EMA(
                range_sum, period=self.p.smooth_period1
            ),
            period=self.p.smooth_period2
        )[0]
        
        if smoothed2 == 0:
            return 0
            
        return 100 * smoothed1 / (smoothed2 / 2)
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.smi_history) < 2:
            return 0
            
        # SMI-Momentum
        momentum = self.smi_history[-1] - self.smi_history[-2]
        
        # Relative Stärke
        strength = abs(momentum)
        if self.data[0] != 0:
            strength = strength / self.data[0]
            
        return min(1.0, strength)
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und SMI.
        """
        if len(self.price_history) < self.p.period or len(self.smi_history) < self.p.period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.period:])
        price_low = min(self.price_history[-self.p.period:])
        
        # SMI-Hochs/-Tiefs
        smi_high = max(self.smi_history[-self.p.period:])
        smi_low = min(self.smi_history[-self.p.period:])
        
        # Bullische Divergenz
        if price_low < price_high and smi_low > smi_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and smi_low < smi_high:
            return -1
            
        return 0
        
    def next(self):
        # SMI berechnen
        self.lines.smi[0] = self.calculate_smi()
        
        # Historie aktualisieren
        self.smi_history.append(self.lines.smi[0])
        self.price_history.append(self.data[0])
        
        # Signal-Linie
        self.lines.signal[0] = bt.indicators.EMA(
            self.lines.smi, period=self.p.signal_period
        )[0]
        
        # Histogramm
        self.lines.histogram[0] = (
            self.lines.smi[0] - self.lines.signal[0]
        )
        self.histogram_history.append(self.lines.histogram[0])
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Bänder
        self.lines.upper[0] = self.p.upper_threshold
        self.lines.lower[0] = self.p.lower_threshold
        self.lines.mid[0] = 0
        
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.smooth_period1,
            self.p.smooth_period2
        )
        for hist in [self.smi_history, self.price_history, self.histogram_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smi[0] < self.p.lower_threshold and
            self.lines.histogram[0] > 0 and
            self.lines.trend_strength[0] > 0.3 and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smi[0] > self.p.upper_threshold and
            self.lines.histogram[0] < 0 and
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
                'smi': self.lines.smi[0],
                'signal': self.lines.signal[0],
                'histogram': self.lines.histogram[0],
                'trend_strength': self.lines.trend_strength[0]
            },
            'trend': {
                'direction': np.sign(self.lines.histogram[0]),
                'strength': abs(self.lines.histogram[0]),
                'momentum': (
                    self.lines.histogram[0] -
                    self.histogram_history[-2]
                    if len(self.histogram_history) > 1
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
                    abs(self.lines.histogram[0])
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'smi_stability': (
                    np.std(self.smi_history)
                    if len(self.smi_history) > 1
                    else 0
                ),
                'histogram_stability': (
                    np.std(self.histogram_history)
                    if len(self.histogram_history) > 1
                    else 0
                )
            }
        }
