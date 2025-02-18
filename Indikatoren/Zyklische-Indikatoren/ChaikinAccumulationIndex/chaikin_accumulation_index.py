import backtrader as bt
import numpy as np

class ChaikinAccumulationIndex(bt.Indicator):
    """
    Chaikin Accumulation Index
    
    Ein Indikator, der Volumen und Preisbewegungen kombiniert,
    um Akkumulations- und Distributionsphasen zu identifizieren.
    
    Features:
    - Volumen-Preisanalyse
    - Akkumulationsberechnung
    - Trendstärkeanalyse
    - Signalgenerierung
    
    Parameter:
    - fast_period (3): Schnelle EMA-Periode
    - slow_period (10): Langsame EMA-Periode
    - smooth_period (10): Glättungsperiode
    """
    
    lines = ('cai', 'smoothed_cai',
             'trend_strength', 'volume_flow',
             'signal')
             
    params = (
        ('fast_period', 3),
        ('slow_period', 10),
        ('smooth_period', 10)
    )
    
    plotlines = dict(
        cai=dict(color='blue', _name='CAI'),
        smoothed_cai=dict(color='red', _name='Smoothed CAI'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        volume_flow=dict(color='purple', _name='Volume Flow'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(ChaikinAccumulationIndex, self).__init__()
        
        # Historie
        self.cai_history = []
        self.flow_history = []
        
    def calculate_money_flow_multiplier(self):
        """
        Berechnet den Money Flow Multiplier.
        """
        if (self.data.high[0] == self.data.low[0]):
            return 0
            
        return (
            ((self.data.close[0] - self.data.low[0]) -
             (self.data.high[0] - self.data.close[0])) /
            (self.data.high[0] - self.data.low[0])
        )
        
    def calculate_money_flow_volume(self):
        """
        Berechnet das Money Flow Volume.
        """
        return (
            self.calculate_money_flow_multiplier() *
            self.data.volume[0]
        )
        
    def calculate_cai(self):
        """
        Berechnet den Chaikin Accumulation Index.
        """
        if len(self.flow_history) < self.p.slow_period:
            return 0
            
        fast_ema = np.mean(
            self.flow_history[-self.p.fast_period:]
        )
        slow_ema = np.mean(
            self.flow_history[-self.p.slow_period:]
        )
        
        return fast_ema - slow_ema
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.cai_history) < 2:
            return 0
            
        return (
            self.cai_history[-1] -
            self.cai_history[-2]
        )
        
    def calculate_volume_flow(self):
        """
        Berechnet den Volumenfluss.
        """
        if len(self.flow_history) < self.p.slow_period:
            return 0
            
        return np.mean(
            self.flow_history[-self.p.slow_period:]
        )
        
    def next(self):
        # Money Flow Volume berechnen
        flow = self.calculate_money_flow_volume()
        self.flow_history.append(flow)
        
        # CAI berechnen
        cai = self.calculate_cai()
        self.cai_history.append(cai)
        self.lines.cai[0] = cai
        
        # Geglätteter CAI
        if len(self.cai_history) >= self.p.smooth_period:
            self.lines.smoothed_cai[0] = np.mean(
                self.cai_history[-self.p.smooth_period:]
            )
        else:
            self.lines.smoothed_cai[0] = cai
            
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volumenfluss
        self.lines.volume_flow[0] = self.calculate_volume_flow()
        
        # Signal
        if (self.lines.cai[0] > 0 and
            self.lines.trend_strength[0] > 0 and
            self.lines.volume_flow[0] > 0):
            self.lines.signal[0] = 1  # Kaufsignal
        elif (self.lines.cai[0] < 0 and
              self.lines.trend_strength[0] < 0 and
              self.lines.volume_flow[0] < 0):
            self.lines.signal[0] = -1  # Verkaufssignal
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.fast_period,
            self.p.slow_period,
            self.p.smooth_period
        )
        for hist in [self.cai_history,
                    self.flow_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'cai': {
                'value': self.lines.cai[0],
                'smoothed': self.lines.smoothed_cai[0],
                'trend': (
                    'accumulation'
                    if self.lines.cai[0] > 0
                    else 'distribution'
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': (
                    'up' if self.lines.trend_strength[0] > 0
                    else 'down'
                ),
                'quality': (
                    abs(self.lines.trend_strength[0])
                    if abs(self.lines.trend_strength[0]) <= 1
                    else 1
                )
            },
            'volume': {
                'flow': self.lines.volume_flow[0],
                'direction': (
                    'inflow' if self.lines.volume_flow[0] > 0
                    else 'outflow'
                ),
                'strength': abs(self.lines.volume_flow[0])
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'reliability': (
                    abs(self.lines.trend_strength[0]) *
                    abs(self.lines.volume_flow[0])
                    if abs(self.lines.volume_flow[0]) <= 1
                    else abs(self.lines.trend_strength[0])
                )
            },
            'market_state': {
                'accumulation': (
                    'strong'
                    if self.lines.cai[0] > 0.7
                    else 'weak'
                    if self.lines.cai[0] > 0
                    else 'none'
                ),
                'distribution': (
                    'strong'
                    if self.lines.cai[0] < -0.7
                    else 'weak'
                    if self.lines.cai[0] < 0
                    else 'none'
                ),
                'volume_quality': (
                    'high'
                    if abs(self.lines.volume_flow[0]) > 0.7
                    else 'low'
                )
            }
        }
