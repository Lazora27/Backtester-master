import backtrader as bt
import numpy as np

class AccumulativeSwingIndex(bt.Indicator):
    """
    Accumulative Swing Index (ASI)
    
    Ein Indikator, der die kumulative Preisstärke und
    -bewegung unter Berücksichtigung von Volumen misst.
    
    Features:
    - Preisbewegungsanalyse
    - Volumengewichtung
    - Trendstärkeberechnung
    - Swing-Identifikation
    - Signal-Validierung
    
    Parameter:
    - period (20): Basisperiode
    - limit_move (3.0): Limitbewegung
    - volume_factor (1.0): Volumenfaktor
    """
    
    lines = ('asi', 'smoothed_asi',
             'swing_strength', 'volume_impact',
             'trend_direction', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 20),
        ('limit_move', 3.0),
        ('volume_factor', 1.0),
        ('min_swing_strength', 0.3)
    )
    
    plotlines = dict(
        asi=dict(color='blue', _name='ASI'),
        smoothed_asi=dict(color='red', _name='Smoothed ASI'),
        swing_strength=dict(color='purple', _name='Swing Strength'),
        volume_impact=dict(color='green', _name='Volume Impact'),
        trend_direction=dict(color='orange', _name='Trend Direction'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(AccumulativeSwingIndex, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.asi_history = []
        self.volume_history = []
        self.swing_history = []
        
    def calculate_asi(self):
        """
        Berechnet den ASI-Wert.
        """
        if len(self.data) < 2:
            return 0
            
        # Aktuelle Werte
        close = self.data.close[0]
        prev_close = self.data.close[-1]
        high = self.data.high[0]
        low = self.data.low[0]
        prev_high = self.data.high[-1]
        prev_low = self.data.low[-1]
        
        # Limit Move
        limit = self.p.limit_move * self.atr[0]
        
        # Preisbewegungen
        k = max(abs(high - prev_close), abs(low - prev_close))
        
        # Richtungsbestimmung
        if abs(high - prev_close) > abs(low - prev_close):
            r = high - prev_close - (low - prev_close) / 2
        else:
            r = low - prev_close - (high - prev_close) / 2
            
        # ASI-Berechnung
        if k > 0 and limit > 0:
            asi = 50 * (
                (close - prev_close +
                 (close - open) / 2 +
                 (prev_close - prev_open) / 2) *
                (k / limit) * r / k
            )
        else:
            asi = 0
            
        # Volumengewichtung
        if len(self.volume_history) >= self.p.period:
            avg_volume = np.mean(self.volume_history[-self.p.period:])
            if avg_volume > 0:
                volume_weight = (
                    self.data.volume[0] / avg_volume
                ) ** self.p.volume_factor
                asi *= volume_weight
                
        return asi
        
    def calculate_swing_strength(self):
        """
        Berechnet die Swing-Stärke.
        """
        if len(self.asi_history) < 2:
            return 0
            
        # ASI-Momentum
        momentum = self.asi_history[-1] - self.asi_history[-2]
        
        # Relative Stärke
        strength = abs(momentum)
        if self.data[0] != 0:
            strength = strength / self.data[0]
            
        return min(1.0, strength)
        
    def next(self):
        # ASI berechnen
        self.lines.asi[0] = self.calculate_asi()
        self.asi_history.append(self.lines.asi[0])
        
        # Geglätteter ASI
        self.lines.smoothed_asi[0] = bt.indicators.EMA(
            self.lines.asi, period=self.p.period
        )[0]
        
        # Swing-Stärke
        self.lines.swing_strength[0] = self.calculate_swing_strength()
        self.swing_history.append(self.lines.swing_strength[0])
        
        # Volumeneinfluss
        self.volume_history.append(self.data.volume[0])
        if len(self.volume_history) >= self.p.period:
            avg_volume = np.mean(self.volume_history[-self.p.period:])
            if avg_volume > 0:
                self.lines.volume_impact[0] = (
                    self.data.volume[0] / avg_volume
                )
        else:
            self.lines.volume_impact[0] = 1.0
            
        # Trendrichtung
        self.lines.trend_direction[0] = np.sign(
            self.lines.smoothed_asi[0] -
            self.lines.smoothed_asi[-1]
        )
        
        # Historie begrenzen
        max_period = self.p.period
        for hist in [self.asi_history, self.volume_history,
                    self.swing_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_asi[0] > self.lines.smoothed_asi[-1] and
            self.lines.swing_strength[0] > self.p.min_swing_strength and
            self.lines.volume_impact[0] > 1.0 and
            self.lines.trend_direction[0] > 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_asi[0] < self.lines.smoothed_asi[-1] and
            self.lines.swing_strength[0] > self.p.min_swing_strength and
            self.lines.volume_impact[0] > 1.0 and
            self.lines.trend_direction[0] < 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'asi': {
                'current': self.lines.asi[0],
                'smoothed': self.lines.smoothed_asi[0],
                'momentum': (
                    self.lines.asi[0] - self.asi_history[-2]
                    if len(self.asi_history) > 1
                    else 0
                )
            },
            'swing': {
                'strength': self.lines.swing_strength[0],
                'direction': self.lines.trend_direction[0],
                'consistency': (
                    np.mean([
                        1 if swing > self.p.min_swing_strength
                        else 0
                        for swing in self.swing_history[-5:]
                    ]) if len(self.swing_history) >= 5
                    else 0
                )
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
                'direction': self.lines.trend_direction[0],
                'strength': abs(
                    self.lines.smoothed_asi[0] -
                    self.lines.smoothed_asi[-1]
                ),
                'persistence': (
                    np.mean([
                        1 if (
                            self.lines.trend_direction[0] > 0 and
                            self.lines.smoothed_asi[0] > self.lines.smoothed_asi[-1]
                        ) or (
                            self.lines.trend_direction[0] < 0 and
                            self.lines.smoothed_asi[0] < self.lines.smoothed_asi[-1]
                        ) else 0
                        for _ in range(min(5, len(self.asi_history)))
                    ])
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.swing_strength[0],
                'reliability': (
                    self.lines.swing_strength[0] *
                    abs(self.lines.trend_direction[0]) *
                    self.lines.volume_impact[0]
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'asi_stability': (
                    np.std(self.asi_history)
                    if len(self.asi_history) > 1
                    else 0
                ),
                'swing_stability': (
                    np.std(self.swing_history)
                    if len(self.swing_history) > 1
                    else 0
                )
            }
        }
