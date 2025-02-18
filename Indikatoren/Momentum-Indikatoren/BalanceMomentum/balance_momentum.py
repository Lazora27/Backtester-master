import backtrader as bt
import numpy as np

class BalanceMomentum(bt.Indicator):
    """
    Balance Momentum Indicator
    
    Ein fortgeschrittener Momentum-Indikator, der Preis-Momentum mit
    Volumen-Flow und Marktbreite kombiniert.
    
    Features:
    - Preis-Momentum Analyse
    - Volumen-Flow Integration
    - Marktbreite-Berechnung
    - Adaptive Gewichtung
    - Multi-Timeframe Signale
    
    Parameter:
    - momentum_period (10): Momentum Basisperiode
    - volume_period (20): Volumen-Analyse Periode
    - smooth_period (5): Glättungsperiode
    - threshold (0.5): Signal-Schwelle
    """
    
    lines = ('momentum', 'volume_flow', 'balance',
             'signal_line', 'upper_band', 'lower_band',
             'buy_signal', 'sell_signal')
             
    params = (
        ('momentum_period', 10),
        ('volume_period', 20),
        ('smooth_period', 5),
        ('threshold', 0.5)
    )
    
    plotlines = dict(
        momentum=dict(color='blue', _name='Momentum'),
        volume_flow=dict(color='green', _name='Volume Flow'),
        balance=dict(color='red', _name='Balance'),
        signal_line=dict(color='orange', _name='Signal'),
        upper_band=dict(color='gray', _name='Upper Band'),
        lower_band=dict(color='gray', _name='Lower Band'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(BalanceMomentum, self).__init__()
        
        # Technische Indikatoren
        self.roc = bt.indicators.RateOfChange(
            period=self.p.momentum_period
        )
        self.volume_sma = bt.indicators.SMA(
            self.data.volume, period=self.p.volume_period
        )
        self.atr = bt.indicators.ATR(period=14)
        
        # Glättung
        self.smooth = bt.indicators.EMA(period=self.p.smooth_period)
        
        # Historie
        self.momentum_history = []
        self.volume_history = []
        self.balance_history = []
        
    def calculate_volume_flow(self):
        """
        Berechnet den Volumen-Flow-Indikator.
        """
        if len(self) < 2:
            return 0
            
        # Preis-Änderung
        price_change = self.data[0] - self.data[-1]
        
        # Volumen-Gewichtung
        current_volume = self.data.volume[0]
        avg_volume = self.volume_sma[0]
        
        if avg_volume == 0:
            return 0
            
        volume_ratio = current_volume / avg_volume
        
        # Volumen-Flow (-1 bis 1)
        flow = np.sign(price_change) * volume_ratio
        
        return np.tanh(flow)  # Normalisierung
        
    def calculate_balance(self):
        """
        Berechnet den Balance-Indikator.
        """
        if len(self.momentum_history) < self.p.momentum_period:
            return 0
            
        # Momentum-Komponente
        momentum = self.roc[0]
        
        # Volumen-Komponente
        volume_flow = self.calculate_volume_flow()
        
        # Marktbreite (simuliert durch Preisbewegung)
        if len(self) < self.p.momentum_period:
            market_breadth = 0
        else:
            up_days = sum(1 for i in range(self.p.momentum_period)
                         if self.data[-i] > self.data[-i-1])
            market_breadth = (up_days / self.p.momentum_period - 0.5) * 2
            
        # Gewichtete Kombination
        balance = (
            momentum * 0.4 +
            volume_flow * 0.4 +
            market_breadth * 0.2
        )
        
        return np.tanh(balance)  # Normalisierung
        
    def calculate_bands(self):
        """
        Berechnet adaptive Bänder für den Balance-Indikator.
        """
        if len(self.balance_history) < self.p.momentum_period:
            return self.p.threshold, -self.p.threshold
            
        # Volatilitätsbasierte Bandbreite
        volatility = np.std(self.balance_history)
        band_width = self.p.threshold * (1 + volatility)
        
        return band_width, -band_width
        
    def next(self):
        # Momentum
        self.lines.momentum[0] = self.roc[0]
        
        # Volumen-Flow
        self.lines.volume_flow[0] = self.calculate_volume_flow()
        
        # Balance
        self.lines.balance[0] = self.calculate_balance()
        
        # Signal-Linie
        self.lines.signal_line[0] = self.smooth(self.lines.balance)
        
        # Bänder
        upper, lower = self.calculate_bands()
        self.lines.upper_band[0] = upper
        self.lines.lower_band[0] = lower
        
        # Historie aktualisieren
        self.momentum_history.append(self.lines.momentum[0])
        self.volume_history.append(self.lines.volume_flow[0])
        self.balance_history.append(self.lines.balance[0])
        
        if len(self.momentum_history) > self.p.momentum_period:
            self.momentum_history.pop(0)
            self.volume_history.pop(0)
            self.balance_history.pop(0)
            
        # Signal-Generierung
        # Buy Signal
        if (self.lines.balance[0] > self.lines.signal_line[0] and
            self.lines.balance[0] > 0 and
            self.lines.volume_flow[0] > 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.balance[0] < self.lines.signal_line[0] and
            self.lines.balance[0] < 0 and
            self.lines.volume_flow[0] < 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'momentum': {
                'value': self.lines.momentum[0],
                'average': np.mean(self.momentum_history) if self.momentum_history else 0,
                'trend': ('up' if self.lines.momentum[0] > 0 else 'down')
            },
            'volume': {
                'flow': self.lines.volume_flow[0],
                'confirmation': (
                    self.lines.volume_flow[0] *
                    self.lines.momentum[0] > 0
                ),
                'strength': abs(self.lines.volume_flow[0])
            },
            'balance': {
                'current': self.lines.balance[0],
                'signal': self.lines.signal_line[0],
                'bands': {
                    'upper': self.lines.upper_band[0],
                    'lower': self.lines.lower_band[0]
                }
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(self.lines.balance[0]),
                'reliability': (
                    abs(self.lines.balance[0]) *
                    abs(self.lines.volume_flow[0])
                )
            },
            'risk': {
                'volatility': self.atr[0] / self.data[0] if self.data[0] != 0 else 0,
                'momentum_stability': np.std(self.momentum_history) if self.momentum_history else 0,
                'volume_stability': np.std(self.volume_history) if self.volume_history else 0
            }
        }
