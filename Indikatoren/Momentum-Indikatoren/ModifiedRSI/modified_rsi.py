import backtrader as bt
import numpy as np

class ModifiedRSI(bt.Indicator):
    """
    Modified RSI Indicator
    
    Eine erweiterte Version des RSI mit adaptiver Berechnung
    und zusätzlichen Analysefunktionen.
    
    Features:
    - Adaptive RSI-Berechnung
    - Volatilitätsanpassung
    - Momentum-Bestätigung
    - Divergenz-Erkennung
    - Signal-Validierung
    
    Parameter:
    - period (14): Basisperiode
    - mod_period (5): Modifikationsperiode
    - vol_period (10): Volatilitätsperiode
    - upper_band (70): Obere Schwelle
    - lower_band (30): Untere Schwelle
    """
    
    lines = ('mod_rsi', 'vol_adjusted_rsi',
             'momentum', 'divergence', 'signal',
             'upper', 'lower', 'mid',
             'buy_signal', 'sell_signal')
             
    params = (
        ('period', 14),
        ('mod_period', 5),
        ('vol_period', 10),
        ('upper_band', 70),
        ('lower_band', 30)
    )
    
    plotlines = dict(
        mod_rsi=dict(color='blue', _name='Mod RSI'),
        vol_adjusted_rsi=dict(color='red', _name='Vol Adj RSI'),
        momentum=dict(color='green', _name='Momentum'),
        divergence=dict(color='purple', _name='Divergence'),
        signal=dict(color='orange', _name='Signal'),
        upper=dict(color='gray', _name='Upper'),
        lower=dict(color='gray', _name='Lower'),
        mid=dict(color='gray', _name='Mid'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(ModifiedRSI, self).__init__()
        
        # Basis RSI
        self.rsi = bt.indicators.RSI(period=self.p.period)
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=self.p.vol_period)
        
        # Historie
        self.rsi_history = []
        self.price_history = []
        self.momentum_history = []
        
    def calculate_modified_rsi(self):
        """
        Berechnet den modifizierten RSI-Wert.
        """
        if len(self.rsi_history) < self.p.mod_period:
            return self.rsi[0]
            
        # Gewichtete Summe
        weights = np.linspace(1, 2, self.p.mod_period)
        weighted_sum = sum(
            w * r for w, r in zip(
                weights,
                self.rsi_history[-self.p.mod_period:]
            )
        )
        
        return weighted_sum / sum(weights)
        
    def calculate_volatility_adjustment(self):
        """
        Berechnet die Volatilitätsanpassung.
        """
        if len(self.data) < self.p.vol_period:
            return 1.0
            
        # Relative Volatilität
        current_vol = self.vol[0]
        if current_vol == 0:
            return 1.0
            
        avg_vol = np.mean([
            self.vol[-i] for i in range(self.p.vol_period)
            if not np.isnan(self.vol[-i])
        ])
        
        if avg_vol == 0:
            return 1.0
            
        return current_vol / avg_vol
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und RSI.
        """
        if len(self.price_history) < self.p.period or len(self.rsi_history) < self.p.period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.period:])
        price_low = min(self.price_history[-self.p.period:])
        
        # RSI-Hochs/-Tiefs
        rsi_high = max(self.rsi_history[-self.p.period:])
        rsi_low = min(self.rsi_history[-self.p.period:])
        
        # Bullische Divergenz
        if price_low < price_high and rsi_low > rsi_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and rsi_low < rsi_high:
            return -1
            
        return 0
        
    def calculate_momentum(self):
        """
        Berechnet den Momentum-Wert.
        """
        if len(self.rsi_history) < 2:
            return 0
            
        return self.rsi_history[-1] - self.rsi_history[-2]
        
    def next(self):
        # Historie aktualisieren
        self.rsi_history.append(self.rsi[0])
        self.price_history.append(self.data[0])
        
        # Modifizierter RSI
        self.lines.mod_rsi[0] = self.calculate_modified_rsi()
        
        # Volatilitätsanpassung
        vol_adj = self.calculate_volatility_adjustment()
        self.lines.vol_adjusted_rsi[0] = (
            self.lines.mod_rsi[0] * vol_adj
        )
        
        # Momentum
        momentum = self.calculate_momentum()
        self.lines.momentum[0] = momentum
        self.momentum_history.append(momentum)
        
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Signal-Linie
        self.lines.signal[0] = bt.indicators.SMA(
            self.lines.mod_rsi, period=self.p.mod_period
        )[0]
        
        # Bänder
        self.lines.upper[0] = self.p.upper_band
        self.lines.lower[0] = self.p.lower_band
        self.lines.mid[0] = 50
        
        # Historie begrenzen
        max_period = max(self.p.period, self.p.mod_period)
        for hist in [self.rsi_history, self.price_history, self.momentum_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.vol_adjusted_rsi[0] < self.p.lower_band and
            self.lines.momentum[0] > 0 and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.vol_adjusted_rsi[0] > self.p.upper_band and
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
            'rsi': {
                'standard': self.rsi[0],
                'modified': self.lines.mod_rsi[0],
                'vol_adjusted': self.lines.vol_adjusted_rsi[0],
                'momentum': self.lines.momentum[0]
            },
            'conditions': {
                'overbought': (
                    self.lines.vol_adjusted_rsi[0] >
                    self.p.upper_band
                ),
                'oversold': (
                    self.lines.vol_adjusted_rsi[0] <
                    self.p.lower_band
                ),
                'momentum': (
                    'increasing' if self.lines.momentum[0] > 0
                    else 'decreasing'
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
                'strength': abs(
                    self.lines.vol_adjusted_rsi[0] - 50
                ) / 50,
                'reliability': (
                    (1 - abs(self.lines.vol_adjusted_rsi[0] - 50) / 50) *
                    abs(self.lines.momentum[0]) *
                    (1 + abs(self.lines.divergence[0]))
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'rsi_stability': (
                    np.std(self.rsi_history)
                    if len(self.rsi_history) > 1
                    else 0
                ),
                'momentum_stability': (
                    np.std(self.momentum_history)
                    if len(self.momentum_history) > 1
                    else 0
                )
            }
        }
