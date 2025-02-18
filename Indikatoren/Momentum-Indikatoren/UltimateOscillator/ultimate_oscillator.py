import backtrader as bt
import numpy as np

class UltimateOscillator(bt.Indicator):
    """
    Ultimate Oscillator
    
    Ein Momentum-Indikator, der drei verschiedene Zeiträume
    kombiniert, um Überkauf- und Überverkaufbedingungen
    zu identifizieren.
    
    Features:
    - Dreifache Zeitraumanalyse
    - Gewichtete Berechnung
    - Trendstärke-Analyse
    - Divergenz-Erkennung
    - Signal-Validierung
    
    Parameter:
    - fast_period (7): Schnelle Periode
    - mid_period (14): Mittlere Periode
    - slow_period (28): Langsame Periode
    - fast_weight (4.0): Gewichtung schnelle Periode
    - mid_weight (2.0): Gewichtung mittlere Periode
    - slow_weight (1.0): Gewichtung langsame Periode
    """
    
    lines = ('uo', 'signal',
             'trend_strength', 'divergence',
             'upper', 'lower', 'mid',
             'buy_signal', 'sell_signal')
             
    params = (
        ('fast_period', 7),
        ('mid_period', 14),
        ('slow_period', 28),
        ('fast_weight', 4.0),
        ('mid_weight', 2.0),
        ('slow_weight', 1.0),
        ('signal_period', 9),
        ('upper_threshold', 70),
        ('lower_threshold', 30)
    )
    
    plotlines = dict(
        uo=dict(color='blue', _name='UO'),
        signal=dict(color='red', _name='Signal'),
        trend_strength=dict(color='purple', _name='Trend Strength'),
        divergence=dict(color='orange', _name='Divergence'),
        upper=dict(color='gray', _name='Upper'),
        lower=dict(color='gray', _name='Lower'),
        mid=dict(color='gray', _name='Mid'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(UltimateOscillator, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Historie
        self.uo_history = []
        self.price_history = []
        self.bp_history = []  # Buying Pressure
        self.tr_history = []  # True Range
        
    def calculate_buying_pressure(self):
        """
        Berechnet den Buying Pressure.
        """
        close = self.data.close[0]
        true_low = min(self.data.low[0], self.data.close[-1])
        return close - true_low
        
    def calculate_true_range(self):
        """
        Berechnet die True Range.
        """
        high = self.data.high[0]
        low = self.data.low[0]
        prev_close = self.data.close[-1]
        
        return max(
            high - low,
            abs(high - prev_close),
            abs(low - prev_close)
        )
        
    def calculate_average(self, period):
        """
        Berechnet den Average für eine bestimmte Periode.
        """
        if len(self.bp_history) < period or len(self.tr_history) < period:
            return 0
            
        bp_sum = sum(self.bp_history[-period:])
        tr_sum = sum(self.tr_history[-period:])
        
        if tr_sum == 0:
            return 0
            
        return bp_sum / tr_sum
        
    def calculate_uo(self):
        """
        Berechnet den Ultimate Oscillator Wert.
        """
        # Averages berechnen
        fast_avg = self.calculate_average(self.p.fast_period)
        mid_avg = self.calculate_average(self.p.mid_period)
        slow_avg = self.calculate_average(self.p.slow_period)
        
        # Gewichtete Summe
        weighted_sum = (
            self.p.fast_weight * fast_avg +
            self.p.mid_weight * mid_avg +
            self.p.slow_weight * slow_avg
        )
        
        # Gesamtgewichtung
        total_weight = (
            self.p.fast_weight +
            self.p.mid_weight +
            self.p.slow_weight
        )
        
        if total_weight == 0:
            return 50
            
        return 100 * weighted_sum / total_weight
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.uo_history) < 2:
            return 0
            
        # UO-Momentum
        momentum = self.uo_history[-1] - self.uo_history[-2]
        
        # Relative Stärke
        strength = abs(momentum)
        if self.data[0] != 0:
            strength = strength / self.data[0]
            
        return min(1.0, strength)
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und UO.
        """
        if len(self.price_history) < self.p.slow_period or len(self.uo_history) < self.p.slow_period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.slow_period:])
        price_low = min(self.price_history[-self.p.slow_period:])
        
        # UO-Hochs/-Tiefs
        uo_high = max(self.uo_history[-self.p.slow_period:])
        uo_low = min(self.uo_history[-self.p.slow_period:])
        
        # Bullische Divergenz
        if price_low < price_high and uo_low > uo_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and uo_low < uo_high:
            return -1
            
        return 0
        
    def next(self):
        # Buying Pressure und True Range berechnen
        bp = self.calculate_buying_pressure()
        tr = self.calculate_true_range()
        
        # Historie aktualisieren
        self.bp_history.append(bp)
        self.tr_history.append(tr)
        self.price_history.append(self.data[0])
        
        # UO berechnen
        self.lines.uo[0] = self.calculate_uo()
        self.uo_history.append(self.lines.uo[0])
        
        # Signal-Linie
        self.lines.signal[0] = bt.indicators.EMA(
            self.lines.uo, period=self.p.signal_period
        )[0]
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Bänder
        self.lines.upper[0] = self.p.upper_threshold
        self.lines.lower[0] = self.p.lower_threshold
        self.lines.mid[0] = 50
        
        # Historie begrenzen
        max_period = max(
            self.p.fast_period,
            self.p.mid_period,
            self.p.slow_period
        )
        for hist in [
            self.uo_history,
            self.price_history,
            self.bp_history,
            self.tr_history
        ]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.uo[0] < self.p.lower_threshold and
            self.lines.uo[0] > self.lines.uo[-1] and
            self.lines.trend_strength[0] > 0.3 and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.uo[0] > self.p.upper_threshold and
            self.lines.uo[0] < self.lines.uo[-1] and
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
            'oscillator': {
                'uo': self.lines.uo[0],
                'signal': self.lines.signal[0],
                'trend_strength': self.lines.trend_strength[0]
            },
            'trend': {
                'direction': np.sign(
                    self.lines.uo[0] - self.lines.uo[-1]
                ),
                'strength': self.lines.trend_strength[0],
                'momentum': (
                    self.lines.uo[0] - self.lines.uo[-1]
                    if len(self.uo_history) > 1
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
                    abs(self.lines.uo[0] - 50) / 50
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'uo_stability': (
                    np.std(self.uo_history)
                    if len(self.uo_history) > 1
                    else 0
                ),
                'buying_pressure': (
                    np.mean(self.bp_history) /
                    np.mean(self.tr_history)
                    if len(self.bp_history) > 0 and
                    np.mean(self.tr_history) != 0
                    else 0
                )
            }
        }
