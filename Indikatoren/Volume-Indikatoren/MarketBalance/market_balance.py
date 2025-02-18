import backtrader as bt
import numpy as np

class MarketBalance(bt.Indicator):
    """
    Market Balance Indicator
    
    Ein Indikator, der das Gleichgewicht zwischen Käufern
    und Verkäufern durch Volumen- und Preisanalyse misst.
    
    Features:
    - Marktgleichgewichtsanalyse
    - Volumengewichtung
    - Preisdynamik
    - Trendstärkeberechnung
    - Signal-Validierung
    
    Parameter:
    - period (20): Basisperiode
    - volume_weight (0.6): Volumengewichtung
    - price_weight (0.4): Preisgewichtung
    """
    
    lines = ('balance', 'smoothed_balance',
             'buying_pressure', 'selling_pressure',
             'market_strength', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 20),
        ('volume_weight', 0.6),
        ('price_weight', 0.4),
        ('min_strength', 0.3)
    )
    
    plotlines = dict(
        balance=dict(color='blue', _name='Balance'),
        smoothed_balance=dict(color='red', _name='Smoothed Balance'),
        buying_pressure=dict(color='green', _name='Buying Pressure'),
        selling_pressure=dict(color='red', _name='Selling Pressure'),
        market_strength=dict(color='purple', _name='Market Strength'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(MarketBalance, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.balance_history = []
        self.volume_history = []
        self.price_history = []
        
    def calculate_balance(self):
        """
        Berechnet den Marktgleichgewichtsindex.
        """
        if len(self.data) < 2:
            return 0
            
        # Preisdynamik
        price_change = (
            self.data.close[0] - self.data.close[-1]
        ) / self.data.close[-1] if self.data.close[-1] != 0 else 0
        
        # Volumengewichtung
        volume_ratio = 1.0
        if len(self.volume_history) >= self.p.period:
            avg_volume = np.mean(self.volume_history[-self.p.period:])
            if avg_volume > 0:
                volume_ratio = self.data.volume[0] / avg_volume
                
        # Balance berechnen
        balance = (
            volume_ratio * self.p.volume_weight +
            price_change * self.p.price_weight
        )
        
        return balance
        
    def calculate_pressure(self):
        """
        Berechnet Kauf- und Verkaufsdruck.
        """
        if len(self.data) < self.p.period:
            return 0, 0
            
        # Preisbereich
        price_range = self.data.high[0] - self.data.low[0]
        if price_range == 0:
            return 0, 0
            
        # Kauf- und Verkaufsdruck
        buying_pressure = (
            self.data.close[0] - self.data.low[0]
        ) / price_range
        
        selling_pressure = (
            self.data.high[0] - self.data.close[0]
        ) / price_range
        
        return buying_pressure, selling_pressure
        
    def calculate_strength(self):
        """
        Berechnet die Marktstärke.
        """
        if len(self.balance_history) < self.p.period:
            return 0
            
        # Trendstärke
        trend_strength = np.abs(
            np.mean(self.balance_history[-self.p.period:])
        )
        
        # Volumenbestätigung
        if len(self.volume_history) >= self.p.period:
            volume_confirmation = (
                self.data.volume[0] /
                np.mean(self.volume_history[-self.p.period:])
            )
        else:
            volume_confirmation = 1.0
            
        return trend_strength * volume_confirmation
        
    def next(self):
        # Marktgleichgewicht berechnen
        self.lines.balance[0] = self.calculate_balance()
        self.balance_history.append(self.lines.balance[0])
        
        # Geglättetes Gleichgewicht
        self.lines.smoothed_balance[0] = bt.indicators.EMA(
            self.lines.balance, period=self.p.period
        )[0]
        
        # Kauf- und Verkaufsdruck
        buying, selling = self.calculate_pressure()
        self.lines.buying_pressure[0] = buying
        self.lines.selling_pressure[0] = selling
        
        # Marktstärke
        self.lines.market_strength[0] = self.calculate_strength()
        
        # Historie aktualisieren
        self.volume_history.append(self.data.volume[0])
        self.price_history.append(self.data.close[0])
        
        # Historie begrenzen
        max_period = self.p.period
        for hist in [self.balance_history, self.volume_history,
                    self.price_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_balance[0] > 0 and
            self.lines.buying_pressure[0] > self.lines.selling_pressure[0] and
            self.lines.market_strength[0] > self.p.min_strength):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_balance[0] < 0 and
            self.lines.selling_pressure[0] > self.lines.buying_pressure[0] and
            self.lines.market_strength[0] > self.p.min_strength):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'balance': {
                'current': self.lines.balance[0],
                'smoothed': self.lines.smoothed_balance[0],
                'trend': (
                    'bullish' if self.lines.balance[0] > 0
                    else 'bearish'
                )
            },
            'pressure': {
                'buying': self.lines.buying_pressure[0],
                'selling': self.lines.selling_pressure[0],
                'net': (
                    self.lines.buying_pressure[0] -
                    self.lines.selling_pressure[0]
                )
            },
            'strength': {
                'market': self.lines.market_strength[0],
                'trend': (
                    np.mean([
                        1 if b > 0 else -1
                        for b in self.balance_history[-5:]
                    ]) if len(self.balance_history) >= 5
                    else 0
                ),
                'volume': (
                    self.data.volume[0] /
                    np.mean(self.volume_history)
                    if len(self.volume_history) > 0
                    else 1.0
                )
            },
            'momentum': {
                'price': (
                    (self.data.close[0] - self.price_history[0]) /
                    self.price_history[0]
                    if len(self.price_history) > 0 and
                    self.price_history[0] != 0
                    else 0
                ),
                'volume': (
                    (self.data.volume[0] - self.volume_history[0]) /
                    self.volume_history[0]
                    if len(self.volume_history) > 0 and
                    self.volume_history[0] != 0
                    else 0
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.market_strength[0],
                'reliability': (
                    self.lines.market_strength[0] *
                    abs(self.lines.balance[0])
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'imbalance': abs(self.lines.balance[0]),
                'pressure_risk': abs(
                    self.lines.buying_pressure[0] -
                    self.lines.selling_pressure[0]
                )
            }
        }
