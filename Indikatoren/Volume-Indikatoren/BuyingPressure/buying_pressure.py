import backtrader as bt
import numpy as np

class BuyingPressure(bt.Indicator):
    """
    Buying Pressure Indicator
    
    Ein Indikator, der den Kaufdruck im Markt durch
    Analyse von Preis und Volumen misst.
    
    Features:
    - Kaufdruckanalyse
    - Volumengewichtung
    - Trendstärkeberechnung
    - Marktungleichgewicht-Erkennung
    - Signal-Validierung
    
    Parameter:
    - period (20): Basisperiode
    - volume_factor (1.0): Volumenfaktor
    - pressure_threshold (0.6): Druckschwelle
    """
    
    lines = ('pressure', 'smoothed_pressure',
             'volume_ratio', 'market_balance',
             'trend_strength', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 20),
        ('volume_factor', 1.0),
        ('pressure_threshold', 0.6),
        ('min_trend_strength', 0.3)
    )
    
    plotlines = dict(
        pressure=dict(color='blue', _name='Pressure'),
        smoothed_pressure=dict(color='red', _name='Smoothed Pressure'),
        volume_ratio=dict(color='green', _name='Volume Ratio'),
        market_balance=dict(color='purple', _name='Market Balance'),
        trend_strength=dict(color='orange', _name='Trend Strength'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(BuyingPressure, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.pressure_history = []
        self.volume_history = []
        self.balance_history = []
        
    def calculate_pressure(self):
        """
        Berechnet den Kaufdruck.
        """
        if len(self.data) < 1:
            return 0
            
        # Preiskomponente
        close = self.data.close[0]
        high = self.data.high[0]
        low = self.data.low[0]
        
        if high == low:
            price_position = 0.5
        else:
            price_position = (close - low) / (high - low)
            
        # Volumenkomponente
        volume_weight = 1.0
        if len(self.volume_history) >= self.p.period:
            avg_volume = np.mean(self.volume_history[-self.p.period:])
            if avg_volume > 0:
                volume_weight = (
                    self.data.volume[0] / avg_volume
                ) ** self.p.volume_factor
                
        # Kaufdruck berechnen
        pressure = price_position * volume_weight
        
        return pressure
        
    def calculate_market_balance(self):
        """
        Berechnet das Marktgleichgewicht.
        """
        if len(self.pressure_history) < self.p.period:
            return 0
            
        # Durchschnittlicher Druck
        avg_pressure = np.mean(self.pressure_history[-self.p.period:])
        
        # Abweichung vom Gleichgewicht (0.5)
        balance = avg_pressure - 0.5
        
        return balance
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.pressure_history) < 2:
            return 0
            
        # Druckmomentum
        momentum = self.pressure_history[-1] - self.pressure_history[-2]
        
        # Relative Stärke
        strength = abs(momentum)
        
        return min(1.0, strength)
        
    def next(self):
        # Kaufdruck berechnen
        self.lines.pressure[0] = self.calculate_pressure()
        self.pressure_history.append(self.lines.pressure[0])
        
        # Geglätteter Druck
        self.lines.smoothed_pressure[0] = bt.indicators.EMA(
            self.lines.pressure, period=self.p.period
        )[0]
        
        # Volumenanalyse
        self.volume_history.append(self.data.volume[0])
        if len(self.volume_history) >= self.p.period:
            avg_volume = np.mean(self.volume_history[-self.p.period:])
            if avg_volume > 0:
                self.lines.volume_ratio[0] = (
                    self.data.volume[0] / avg_volume
                )
        else:
            self.lines.volume_ratio[0] = 1.0
            
        # Marktgleichgewicht
        self.lines.market_balance[0] = self.calculate_market_balance()
        self.balance_history.append(self.lines.market_balance[0])
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Historie begrenzen
        max_period = self.p.period
        for hist in [self.pressure_history, self.volume_history,
                    self.balance_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_pressure[0] > self.p.pressure_threshold and
            self.lines.volume_ratio[0] > 1.0 and
            self.lines.trend_strength[0] > self.p.min_trend_strength and
            self.lines.market_balance[0] > 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_pressure[0] < (1 - self.p.pressure_threshold) and
            self.lines.volume_ratio[0] > 1.0 and
            self.lines.trend_strength[0] > self.p.min_trend_strength and
            self.lines.market_balance[0] < 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'pressure': {
                'current': self.lines.pressure[0],
                'smoothed': self.lines.smoothed_pressure[0],
                'momentum': (
                    self.lines.pressure[0] - self.pressure_history[-2]
                    if len(self.pressure_history) > 1
                    else 0
                )
            },
            'volume': {
                'ratio': self.lines.volume_ratio[0],
                'trend': (
                    'increasing' if self.lines.volume_ratio[0] > 1
                    else 'decreasing'
                ),
                'significance': abs(self.lines.volume_ratio[0] - 1)
            },
            'market': {
                'balance': self.lines.market_balance[0],
                'state': (
                    'buying_pressure' if self.lines.market_balance[0] > 0
                    else 'selling_pressure'
                ),
                'intensity': abs(self.lines.market_balance[0])
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'persistence': (
                    np.mean([
                        1 if balance > 0
                        else -1 if balance < 0
                        else 0
                        for balance in self.balance_history[-5:]
                    ]) if len(self.balance_history) >= 5
                    else 0
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    self.lines.trend_strength[0] *
                    abs(self.lines.market_balance[0]) *
                    self.lines.volume_ratio[0]
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'pressure_stability': (
                    np.std(self.pressure_history)
                    if len(self.pressure_history) > 1
                    else 0
                ),
                'balance_stability': (
                    np.std(self.balance_history)
                    if len(self.balance_history) > 1
                    else 0
                )
            }
        }
