import backtrader as bt
import numpy as np

class TrueStrengthIndex(bt.Indicator):
    """
    True Strength Index (TSI)
    
    Ein Momentum-Indikator, der Preisänderungen und deren
    absolute Werte doppelt glättet, um die wahre Marktstärke
    zu messen.
    
    Features:
    - Doppelte Glättung
    - Signallinie
    - Trendstärke-Analyse
    - Divergenz-Erkennung
    - Signal-Validierung
    
    Parameter:
    - r_period (25): Erste Glättungsperiode
    - s_period (13): Zweite Glättungsperiode
    - signal_period (9): Signallinien-Periode
    """
    
    lines = ('tsi', 'signal', 'histogram',
             'trend_strength', 'divergence',
             'upper', 'lower', 'mid',
             'buy_signal', 'sell_signal')
             
    params = (
        ('r_period', 25),
        ('s_period', 13),
        ('signal_period', 9),
        ('upper_threshold', 25),
        ('lower_threshold', -25)
    )
    
    plotlines = dict(
        tsi=dict(color='blue', _name='TSI'),
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
        super(TrueStrengthIndex, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Historie
        self.tsi_history = []
        self.price_history = []
        self.histogram_history = []
        
        # Momentum und absolute Momentum Historie
        self.momentum = []
        self.abs_momentum = []
        
    def calculate_tsi(self):
        """
        Berechnet den TSI-Wert.
        """
        if len(self.price_history) < 2:
            return 0
            
        # Momentum
        momentum = self.price_history[-1] - self.price_history[-2]
        abs_momentum = abs(momentum)
        
        self.momentum.append(momentum)
        self.abs_momentum.append(abs_momentum)
        
        # Erste Glättung
        if len(self.momentum) < self.p.r_period:
            return 0
            
        smooth1_mom = bt.indicators.EMA(
            self.momentum[-self.p.r_period:],
            period=self.p.r_period
        )[-1]
        
        smooth1_abs = bt.indicators.EMA(
            self.abs_momentum[-self.p.r_period:],
            period=self.p.r_period
        )[-1]
        
        # Zweite Glättung
        if len(self.momentum) < self.p.r_period + self.p.s_period:
            return 0
            
        smooth2_mom = bt.indicators.EMA(
            [smooth1_mom],
            period=self.p.s_period
        )[-1]
        
        smooth2_abs = bt.indicators.EMA(
            [smooth1_abs],
            period=self.p.s_period
        )[-1]
        
        # TSI berechnen
        if smooth2_abs == 0:
            return 0
            
        return 100 * smooth2_mom / smooth2_abs
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.histogram_history) < 2:
            return 0
            
        # Histogramm-Momentum
        momentum = self.histogram_history[-1] - self.histogram_history[-2]
        
        # Relative Stärke
        strength = abs(momentum)
        if self.data[0] != 0:
            strength = strength / self.data[0]
            
        return min(1.0, strength)
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und TSI.
        """
        if len(self.price_history) < self.p.r_period or len(self.tsi_history) < self.p.r_period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.r_period:])
        price_low = min(self.price_history[-self.p.r_period:])
        
        # TSI-Hochs/-Tiefs
        tsi_high = max(self.tsi_history[-self.p.r_period:])
        tsi_low = min(self.tsi_history[-self.p.r_period:])
        
        # Bullische Divergenz
        if price_low < price_high and tsi_low > tsi_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and tsi_low < tsi_high:
            return -1
            
        return 0
        
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.data[0])
        
        # TSI berechnen
        self.lines.tsi[0] = self.calculate_tsi()
        self.tsi_history.append(self.lines.tsi[0])
        
        # Signal-Linie
        self.lines.signal[0] = bt.indicators.EMA(
            self.lines.tsi, period=self.p.signal_period
        )[0]
        
        # Histogramm
        self.lines.histogram[0] = (
            self.lines.tsi[0] - self.lines.signal[0]
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
            self.p.r_period,
            self.p.s_period,
            self.p.signal_period
        )
        for hist in [
            self.tsi_history,
            self.price_history,
            self.histogram_history,
            self.momentum,
            self.abs_momentum
        ]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.tsi[0] < self.p.lower_threshold and
            self.lines.histogram[0] > 0 and
            self.lines.trend_strength[0] > 0.3 and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.tsi[0] > self.p.upper_threshold and
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
                'tsi': self.lines.tsi[0],
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
                'tsi_stability': (
                    np.std(self.tsi_history)
                    if len(self.tsi_history) > 1
                    else 0
                ),
                'histogram_stability': (
                    np.std(self.histogram_history)
                    if len(self.histogram_history) > 1
                    else 0
                )
            }
        }
