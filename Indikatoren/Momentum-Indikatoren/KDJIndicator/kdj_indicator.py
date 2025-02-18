import backtrader as bt
import numpy as np

class KDJIndicator(bt.Indicator):
    """
    KDJ Indicator (Stochastic Variant)
    
    Eine erweiterte Version des Stochastic Oscillators, die
    zusätzliche Signallinien und Momentum-Analyse bietet.
    
    Features:
    - Erweiterte Stochastic-Berechnung
    - Dreifache Signallinien (K, D, J)
    - Momentum-Bestätigung
    - Divergenz-Erkennung
    - Signal-Validierung
    
    Parameter:
    - k_period (9): K-Linie Periode
    - d_period (3): D-Linie Periode
    - j_period (3): J-Linie Periode
    - upper_threshold (80): Obere Schwelle
    - lower_threshold (20): Untere Schwelle
    """
    
    lines = ('K', 'D', 'J',
             'upper', 'lower', 'mid',
             'momentum', 'divergence',
             'buy_signal', 'sell_signal')
             
    params = (
        ('k_period', 9),
        ('d_period', 3),
        ('j_period', 3),
        ('upper_threshold', 80),
        ('lower_threshold', 20)
    )
    
    plotlines = dict(
        K=dict(color='blue', _name='%K'),
        D=dict(color='red', _name='%D'),
        J=dict(color='green', _name='%J'),
        upper=dict(color='gray', _name='Upper'),
        lower=dict(color='gray', _name='Lower'),
        mid=dict(color='gray', _name='Mid'),
        momentum=dict(color='purple', _name='Momentum'),
        divergence=dict(color='orange', _name='Divergence'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(KDJIndicator, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.rsi = bt.indicators.RSI(period=14)
        
        # Historie
        self.k_history = []
        self.d_history = []
        self.j_history = []
        self.price_history = []
        
    def calculate_stochastic(self, high, low, close, period):
        """
        Berechnet den Stochastic-Wert.
        """
        if len(high) < period:
            return 50
            
        highest_high = max(high[-period:])
        lowest_low = min(low[-period:])
        
        if highest_high == lowest_low:
            return 50
            
        return 100 * (close - lowest_low) / (highest_high - lowest_low)
        
    def calculate_momentum(self):
        """
        Berechnet den Momentum-Wert.
        """
        if len(self.k_history) < 2:
            return 0
            
        return self.k_history[-1] - self.k_history[-2]
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und Indikator.
        """
        if len(self.price_history) < self.p.k_period or len(self.k_history) < self.p.k_period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.k_period:])
        price_low = min(self.price_history[-self.p.k_period:])
        
        # Indikator-Hochs/-Tiefs
        k_high = max(self.k_history[-self.p.k_period:])
        k_low = min(self.k_history[-self.p.k_period:])
        
        # Bullische Divergenz
        if price_low < price_high and k_low > k_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and k_low < k_high:
            return -1
            
        return 0
        
    def next(self):
        # Preisdaten aktualisieren
        self.price_history.append(self.data[0])
        
        # K-Linie berechnen
        k_value = self.calculate_stochastic(
            self.data.high.get(size=self.p.k_period),
            self.data.low.get(size=self.p.k_period),
            self.data[0],
            self.p.k_period
        )
        self.k_history.append(k_value)
        self.lines.K[0] = k_value
        
        # D-Linie berechnen (Glättung von K)
        if len(self.k_history) >= self.p.d_period:
            d_value = np.mean(self.k_history[-self.p.d_period:])
            self.d_history.append(d_value)
            self.lines.D[0] = d_value
        else:
            self.lines.D[0] = k_value
            
        # J-Linie berechnen
        if len(self.k_history) >= self.p.j_period and len(self.d_history) >= self.p.j_period:
            j_value = 3 * self.k_history[-1] - 2 * self.d_history[-1]
            self.j_history.append(j_value)
            self.lines.J[0] = j_value
        else:
            self.lines.J[0] = k_value
            
        # Schwellen
        self.lines.upper[0] = self.p.upper_threshold
        self.lines.lower[0] = self.p.lower_threshold
        self.lines.mid[0] = 50
        
        # Momentum
        self.lines.momentum[0] = self.calculate_momentum()
        
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Historie begrenzen
        max_period = max(self.p.k_period, self.p.d_period, self.p.j_period)
        for hist in [self.k_history, self.d_history, self.j_history, self.price_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.K[0] < self.p.lower_threshold and
            self.lines.K[0] > self.lines.D[0] and
            self.lines.momentum[0] > 0 and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.K[0] > self.p.upper_threshold and
            self.lines.K[0] < self.lines.D[0] and
            self.lines.momentum[0] < 0 and
            self.lines.divergence[0] <= 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'values': {
                'K': self.lines.K[0],
                'D': self.lines.D[0],
                'J': self.lines.J[0],
                'momentum': self.lines.momentum[0],
                'divergence': self.lines.divergence[0]
            },
            'conditions': {
                'overbought': self.lines.K[0] > self.p.upper_threshold,
                'oversold': self.lines.K[0] < self.p.lower_threshold,
                'bullish_cross': (
                    self.lines.K[0] > self.lines.D[0] and
                    self.k_history[-2] < self.d_history[-2]
                    if len(self.k_history) > 1 and len(self.d_history) > 1
                    else False
                ),
                'bearish_cross': (
                    self.lines.K[0] < self.lines.D[0] and
                    self.k_history[-2] > self.d_history[-2]
                    if len(self.k_history) > 1 and len(self.d_history) > 1
                    else False
                )
            },
            'trend': {
                'direction': np.sign(self.lines.momentum[0]),
                'strength': abs(self.lines.momentum[0]),
                'j_confirmation': (
                    self.lines.J[0] > self.lines.K[0] and
                    self.lines.J[0] > self.lines.D[0]
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(self.lines.K[0] - self.lines.D[0]),
                'reliability': (
                    abs(self.lines.momentum[0]) *
                    (1 + abs(self.lines.divergence[0]))
                )
            },
            'risk': {
                'volatility': self.atr[0] / self.data[0] if self.data[0] != 0 else 0,
                'momentum_stability': (
                    np.std(self.k_history) if len(self.k_history) > 1 else 0
                ),
                'divergence_risk': abs(self.lines.divergence[0])
            }
        }
