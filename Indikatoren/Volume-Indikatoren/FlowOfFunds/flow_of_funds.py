import backtrader as bt
import numpy as np

class FlowOfFunds(bt.Indicator):
    """
    Flow of Funds Indicator
    
    Ein Indikator, der die Geldflussdynamik im Markt
    durch Preis- und Volumenbewegungen analysiert.
    
    Features:
    - Geldflussanalyse
    - Volumengewichtung
    - Marktliquiditätsanalyse
    - Trendstärkeberechnung
    - Signal-Validierung
    
    Parameter:
    - period (20): Basisperiode
    - volume_factor (1.0): Volumenfaktor
    - flow_threshold (0.6): Flussschwelle
    """
    
    lines = ('flow', 'smoothed_flow',
             'liquidity', 'trend_strength',
             'volume_impact', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 20),
        ('volume_factor', 1.0),
        ('flow_threshold', 0.6),
        ('min_trend_strength', 0.3)
    )
    
    plotlines = dict(
        flow=dict(color='blue', _name='Flow'),
        smoothed_flow=dict(color='red', _name='Smoothed Flow'),
        liquidity=dict(color='purple', _name='Liquidity'),
        trend_strength=dict(color='orange', _name='Trend Strength'),
        volume_impact=dict(color='green', _name='Volume Impact'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(FlowOfFunds, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.flow_history = []
        self.volume_history = []
        self.liquidity_history = []
        
    def calculate_flow(self):
        """
        Berechnet den Geldfluss.
        """
        if len(self.data) < 2:
            return 0
            
        # Preisbewegung
        price_change = self.data.close[0] - self.data.close[-1]
        
        # Volumengewichtung
        volume_weight = 1.0
        if len(self.volume_history) >= self.p.period:
            avg_volume = np.mean(self.volume_history[-self.p.period:])
            if avg_volume > 0:
                volume_weight = (
                    self.data.volume[0] / avg_volume
                ) ** self.p.volume_factor
                
        # Geldfluss berechnen
        flow = price_change * volume_weight * self.data.volume[0]
        
        # Normalisierung
        if self.data.close[0] != 0:
            flow = flow / self.data.close[0]
            
        return flow
        
    def calculate_liquidity(self):
        """
        Berechnet die Marktliquidität.
        """
        if len(self.volume_history) < self.p.period:
            return 0
            
        # Durchschnittliches Volumen
        avg_volume = np.mean(self.volume_history[-self.p.period:])
        
        # Liquiditätsmaß
        if avg_volume > 0:
            liquidity = self.data.volume[0] / avg_volume
        else:
            liquidity = 1.0
            
        return liquidity
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.flow_history) < 2:
            return 0
            
        # Flussmomentum
        momentum = self.flow_history[-1] - self.flow_history[-2]
        
        # Relative Stärke
        strength = abs(momentum)
        
        return min(1.0, strength)
        
    def next(self):
        # Geldfluss berechnen
        self.lines.flow[0] = self.calculate_flow()
        self.flow_history.append(self.lines.flow[0])
        
        # Geglätteter Fluss
        self.lines.smoothed_flow[0] = bt.indicators.EMA(
            self.lines.flow, period=self.p.period
        )[0]
        
        # Volumenanalyse
        self.volume_history.append(self.data.volume[0])
        
        # Liquidität
        self.lines.liquidity[0] = self.calculate_liquidity()
        self.liquidity_history.append(self.lines.liquidity[0])
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volumeneinfluss
        if len(self.volume_history) >= self.p.period:
            avg_volume = np.mean(self.volume_history[-self.p.period:])
            if avg_volume > 0:
                self.lines.volume_impact[0] = (
                    self.data.volume[0] / avg_volume
                )
        else:
            self.lines.volume_impact[0] = 1.0
            
        # Historie begrenzen
        max_period = self.p.period
        for hist in [self.flow_history, self.volume_history,
                    self.liquidity_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_flow[0] > self.p.flow_threshold and
            self.lines.liquidity[0] > 1.0 and
            self.lines.trend_strength[0] > self.p.min_trend_strength and
            self.lines.volume_impact[0] > 1.0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_flow[0] < -self.p.flow_threshold and
            self.lines.liquidity[0] > 1.0 and
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
            'flow': {
                'current': self.lines.flow[0],
                'smoothed': self.lines.smoothed_flow[0],
                'momentum': (
                    self.lines.flow[0] - self.flow_history[-2]
                    if len(self.flow_history) > 1
                    else 0
                )
            },
            'liquidity': {
                'level': self.lines.liquidity[0],
                'trend': (
                    'increasing' if self.lines.liquidity[0] > 1
                    else 'decreasing'
                ),
                'stability': (
                    np.std(self.liquidity_history)
                    if len(self.liquidity_history) > 1
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
                'strength': self.lines.trend_strength[0],
                'direction': np.sign(self.lines.smoothed_flow[0]),
                'persistence': (
                    np.mean([
                        1 if flow > 0
                        else -1 if flow < 0
                        else 0
                        for flow in self.flow_history[-5:]
                    ]) if len(self.flow_history) >= 5
                    else 0
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    self.lines.trend_strength[0] *
                    self.lines.liquidity[0] *
                    self.lines.volume_impact[0]
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'flow_stability': (
                    np.std(self.flow_history)
                    if len(self.flow_history) > 1
                    else 0
                ),
                'liquidity_risk': (
                    1 / self.lines.liquidity[0]
                    if self.lines.liquidity[0] > 0
                    else float('inf')
                )
            }
        }
