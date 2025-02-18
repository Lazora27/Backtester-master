import backtrader as bt
import numpy as np

class IntradayIntensity(bt.Indicator):
    """
    Intraday Intensity Index
    
    Ein Indikator, der die Intensität der Intraday-Bewegungen
    durch Preis- und Volumenanalyse misst.
    
    Features:
    - Intraday-Intensitätsanalyse
    - Volumengewichtung
    - Preispositionsanalyse
    - Trendstärkeberechnung
    - Signal-Validierung
    
    Parameter:
    - period (20): Basisperiode
    - volume_factor (1.0): Volumenfaktor
    - intensity_threshold (0.6): Intensitätsschwelle
    """
    
    lines = ('iii', 'smoothed_iii',
             'price_position', 'trend_strength',
             'volume_impact', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 20),
        ('volume_factor', 1.0),
        ('intensity_threshold', 0.6),
        ('min_trend_strength', 0.3)
    )
    
    plotlines = dict(
        iii=dict(color='blue', _name='III'),
        smoothed_iii=dict(color='red', _name='Smoothed III'),
        price_position=dict(color='purple', _name='Price Position'),
        trend_strength=dict(color='orange', _name='Trend Strength'),
        volume_impact=dict(color='green', _name='Volume Impact'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(IntradayIntensity, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.iii_history = []
        self.volume_history = []
        self.position_history = []
        
    def calculate_iii(self):
        """
        Berechnet den Intraday Intensity Index.
        """
        if len(self.data) < 1:
            return 0
            
        # Preiskomponenten
        close = self.data.close[0]
        high = self.data.high[0]
        low = self.data.low[0]
        
        # Range berechnen
        if high == low:
            return 0
            
        # Preisposition
        price_position = (2 * close - high - low) / (high - low)
        
        # Volumengewichtung
        volume_weight = 1.0
        if len(self.volume_history) >= self.p.period:
            avg_volume = np.mean(self.volume_history[-self.p.period:])
            if avg_volume > 0:
                volume_weight = (
                    self.data.volume[0] / avg_volume
                ) ** self.p.volume_factor
                
        # III berechnen
        iii = price_position * volume_weight
        
        return iii
        
    def calculate_price_position(self):
        """
        Berechnet die relative Preisposition.
        """
        if len(self.data) < self.p.period:
            return 0
            
        # Preisextreme
        highest = max(
            self.data.high.get(ago=-i, size=1)[0]
            for i in range(self.p.period)
        )
        lowest = min(
            self.data.low.get(ago=-i, size=1)[0]
            for i in range(self.p.period)
        )
        
        if highest == lowest:
            return 0.5
            
        # Relative Position
        position = (
            self.data.close[0] - lowest
        ) / (highest - lowest)
        
        return position
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.iii_history) < 2:
            return 0
            
        # III-Momentum
        momentum = self.iii_history[-1] - self.iii_history[-2]
        
        # Relative Stärke
        strength = abs(momentum)
        
        return min(1.0, strength)
        
    def next(self):
        # III berechnen
        self.lines.iii[0] = self.calculate_iii()
        self.iii_history.append(self.lines.iii[0])
        
        # Geglätteter III
        self.lines.smoothed_iii[0] = bt.indicators.EMA(
            self.lines.iii, period=self.p.period
        )[0]
        
        # Preisposition
        self.lines.price_position[0] = self.calculate_price_position()
        self.position_history.append(self.lines.price_position[0])
        
        # Volumenanalyse
        self.volume_history.append(self.data.volume[0])
        if len(self.volume_history) >= self.p.period:
            avg_volume = np.mean(self.volume_history[-self.p.period:])
            if avg_volume > 0:
                self.lines.volume_impact[0] = (
                    self.data.volume[0] / avg_volume
                )
        else:
            self.lines.volume_impact[0] = 1.0
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Historie begrenzen
        max_period = self.p.period
        for hist in [self.iii_history, self.volume_history,
                    self.position_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_iii[0] > self.p.intensity_threshold and
            self.lines.price_position[0] < 0.3 and
            self.lines.trend_strength[0] > self.p.min_trend_strength and
            self.lines.volume_impact[0] > 1.0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_iii[0] < -self.p.intensity_threshold and
            self.lines.price_position[0] > 0.7 and
            self.lines.trend_strength[0] > self.p.min_trend_strength and
            self.lines.volume_impact[0] > 1.0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'intensity': {
                'iii': self.lines.iii[0],
                'smoothed': self.lines.smoothed_iii[0],
                'momentum': (
                    self.lines.iii[0] - self.iii_history[-2]
                    if len(self.iii_history) > 1
                    else 0
                )
            },
            'price': {
                'position': self.lines.price_position[0],
                'zone': (
                    'overbought' if self.lines.price_position[0] > 0.7
                    else 'oversold' if self.lines.price_position[0] < 0.3
                    else 'neutral'
                ),
                'extremity': abs(self.lines.price_position[0] - 0.5)
            },
            'volume': {
                'impact': self.lines.volume_impact[0],
                'trend': (
                    'increasing' if self.lines.volume_impact[0] > 1
                    else 'decreasing'
                ),
                'significance': abs(self.lines.volume_impact[0] - 1)
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': np.sign(self.lines.smoothed_iii[0]),
                'persistence': (
                    np.mean([
                        1 if iii > 0
                        else -1 if iii < 0
                        else 0
                        for iii in self.iii_history[-5:]
                    ]) if len(self.iii_history) >= 5
                    else 0
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    self.lines.trend_strength[0] *
                    abs(self.lines.price_position[0] - 0.5) *
                    self.lines.volume_impact[0]
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'iii_stability': (
                    np.std(self.iii_history)
                    if len(self.iii_history) > 1
                    else 0
                ),
                'position_stability': (
                    np.std(self.position_history)
                    if len(self.position_history) > 1
                    else 0
                )
            }
        }
