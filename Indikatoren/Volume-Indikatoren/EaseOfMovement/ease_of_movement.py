import backtrader as bt
import numpy as np

class EaseOfMovement(bt.Indicator):
    """
    Ease of Movement (EMV)
    
    Ein Indikator, der die "Leichtigkeit" der Preisbewegung
    in Relation zum Volumen misst.
    
    Features:
    - Bewegungsleichtigkeit-Analyse
    - Volumengewichtung
    - Trendstärkeberechnung
    - Momentum-Analyse
    - Signal-Validierung
    
    Parameter:
    - period (14): Basisperiode
    - volume_factor (10000): Volumenfaktor
    - smooth_period (3): Glättungsperiode
    """
    
    lines = ('emv', 'smoothed_emv',
             'momentum', 'trend_strength',
             'volume_impact', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 14),
        ('volume_factor', 10000),
        ('smooth_period', 3),
        ('min_trend_strength', 0.3)
    )
    
    plotlines = dict(
        emv=dict(color='blue', _name='EMV'),
        smoothed_emv=dict(color='red', _name='Smoothed EMV'),
        momentum=dict(color='purple', _name='Momentum'),
        trend_strength=dict(color='orange', _name='Trend Strength'),
        volume_impact=dict(color='green', _name='Volume Impact'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(EaseOfMovement, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.emv_history = []
        self.volume_history = []
        self.momentum_history = []
        
    def calculate_emv(self):
        """
        Berechnet den EMV-Wert.
        """
        if len(self.data) < 2:
            return 0
            
        # Mittelpunktbewegung
        curr_midpoint = (self.data.high[0] + self.data.low[0]) / 2
        prev_midpoint = (self.data.high[-1] + self.data.low[-1]) / 2
        midpoint_move = curr_midpoint - prev_midpoint
        
        # Box Ratio
        box_ratio = self.data.volume[0] / self.p.volume_factor
        
        # High-Low Range
        high_low_range = self.data.high[0] - self.data.low[0]
        
        if box_ratio == 0 or high_low_range == 0:
            return 0
            
        # EMV berechnen
        emv = midpoint_move / box_ratio
        
        return emv
        
    def calculate_momentum(self):
        """
        Berechnet das EMV-Momentum.
        """
        if len(self.emv_history) < 2:
            return 0
            
        # EMV-Momentum
        momentum = self.emv_history[-1] - self.emv_history[-2]
        
        return momentum
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.momentum_history) < self.p.period:
            return 0
            
        # Momentum-Konsistenz
        momentum_consistency = np.sum(
            1 if mom > 0
            else -1 if mom < 0
            else 0
            for mom in self.momentum_history[-self.p.period:]
        ) / self.p.period
        
        return abs(momentum_consistency)
        
    def next(self):
        # EMV berechnen
        self.lines.emv[0] = self.calculate_emv()
        self.emv_history.append(self.lines.emv[0])
        
        # Geglätteter EMV
        self.lines.smoothed_emv[0] = bt.indicators.EMA(
            self.lines.emv, period=self.p.smooth_period
        )[0]
        
        # Momentum
        self.lines.momentum[0] = self.calculate_momentum()
        self.momentum_history.append(self.lines.momentum[0])
        
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
        max_period = max(self.p.period, self.p.smooth_period)
        for hist in [self.emv_history, self.volume_history,
                    self.momentum_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_emv[0] > 0 and
            self.lines.momentum[0] > 0 and
            self.lines.trend_strength[0] > self.p.min_trend_strength and
            self.lines.volume_impact[0] > 1.0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_emv[0] < 0 and
            self.lines.momentum[0] < 0 and
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
            'movement': {
                'emv': self.lines.emv[0],
                'smoothed': self.lines.smoothed_emv[0],
                'momentum': self.lines.momentum[0],
                'ease': (
                    'high' if abs(self.lines.emv[0]) > 0.01
                    else 'low'
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': np.sign(self.lines.smoothed_emv[0]),
                'momentum_consistency': (
                    np.mean([
                        1 if mom > 0
                        else -1 if mom < 0
                        else 0
                        for mom in self.momentum_history[-5:]
                    ]) if len(self.momentum_history) >= 5
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
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    self.lines.trend_strength[0] *
                    abs(self.lines.momentum[0]) *
                    self.lines.volume_impact[0]
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'emv_stability': (
                    np.std(self.emv_history)
                    if len(self.emv_history) > 1
                    else 0
                ),
                'momentum_stability': (
                    np.std(self.momentum_history)
                    if len(self.momentum_history) > 1
                    else 0
                )
            }
        }
