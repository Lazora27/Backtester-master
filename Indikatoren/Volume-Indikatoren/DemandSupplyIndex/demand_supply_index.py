import backtrader as bt
import numpy as np

class DemandSupplyIndex(bt.Indicator):
    """
    Demand Supply Index
    
    Ein Indikator, der das Verhältnis von Angebot und
    Nachfrage durch Preis- und Volumenbewegungen misst.
    
    Features:
    - Angebot-Nachfrage-Analyse
    - Volumengewichtung
    - Marktungleichgewicht-Erkennung
    - Trendstärkeberechnung
    - Signal-Validierung
    
    Parameter:
    - period (20): Basisperiode
    - volume_factor (1.0): Volumenfaktor
    - threshold (0.6): Ungleichgewichtsschwelle
    """
    
    lines = ('demand', 'supply',
             'ds_ratio', 'smoothed_ratio',
             'market_force', 'trend_strength',
             'buy_signal', 'sell_signal')
             
    params = (
        ('period', 20),
        ('volume_factor', 1.0),
        ('threshold', 0.6),
        ('min_trend_strength', 0.3)
    )
    
    plotlines = dict(
        demand=dict(color='green', _name='Demand'),
        supply=dict(color='red', _name='Supply'),
        ds_ratio=dict(color='blue', _name='D/S Ratio'),
        smoothed_ratio=dict(color='purple', _name='Smoothed Ratio'),
        market_force=dict(color='orange', _name='Market Force'),
        trend_strength=dict(color='gray', _name='Trend Strength'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(DemandSupplyIndex, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.ratio_history = []
        self.volume_history = []
        self.force_history = []
        
    def calculate_demand_supply(self):
        """
        Berechnet Angebot und Nachfrage.
        """
        if len(self.data) < 2:
            return 0, 0
            
        # Preisbewegung
        close = self.data.close[0]
        prev_close = self.data.close[-1]
        high = self.data.high[0]
        low = self.data.low[0]
        
        # Volumengewichtung
        volume_weight = 1.0
        if len(self.volume_history) >= self.p.period:
            avg_volume = np.mean(self.volume_history[-self.p.period:])
            if avg_volume > 0:
                volume_weight = (
                    self.data.volume[0] / avg_volume
                ) ** self.p.volume_factor
                
        # Nachfrage berechnen
        if close > prev_close:
            demand = (close - low) * volume_weight
        else:
            demand = 0
            
        # Angebot berechnen
        if close < prev_close:
            supply = (high - close) * volume_weight
        else:
            supply = 0
            
        return demand, supply
        
    def calculate_market_force(self):
        """
        Berechnet die Marktkraft.
        """
        if len(self.ratio_history) < self.p.period:
            return 0
            
        # Durchschnittliches Verhältnis
        avg_ratio = np.mean(self.ratio_history[-self.p.period:])
        
        # Abweichung vom Gleichgewicht (1.0)
        force = avg_ratio - 1.0
        
        return force
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.ratio_history) < 2:
            return 0
            
        # Verhältnismomentum
        momentum = self.ratio_history[-1] - self.ratio_history[-2]
        
        # Relative Stärke
        strength = abs(momentum)
        
        return min(1.0, strength)
        
    def next(self):
        # Angebot und Nachfrage berechnen
        demand, supply = self.calculate_demand_supply()
        self.lines.demand[0] = demand
        self.lines.supply[0] = supply
        
        # Verhältnis berechnen
        if supply > 0:
            ratio = demand / supply
        elif demand > 0:
            ratio = float('inf')
        else:
            ratio = 1.0
            
        self.lines.ds_ratio[0] = ratio
        self.ratio_history.append(ratio)
        
        # Geglättetes Verhältnis
        self.lines.smoothed_ratio[0] = bt.indicators.EMA(
            self.lines.ds_ratio, period=self.p.period
        )[0]
        
        # Volumenanalyse
        self.volume_history.append(self.data.volume[0])
        
        # Marktkraft
        self.lines.market_force[0] = self.calculate_market_force()
        self.force_history.append(self.lines.market_force[0])
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Historie begrenzen
        max_period = self.p.period
        for hist in [self.ratio_history, self.volume_history,
                    self.force_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_ratio[0] > self.p.threshold and
            self.lines.market_force[0] > 0 and
            self.lines.trend_strength[0] > self.p.min_trend_strength and
            self.lines.demand[0] > self.lines.supply[0]):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_ratio[0] < (1 / self.p.threshold) and
            self.lines.market_force[0] < 0 and
            self.lines.trend_strength[0] > self.p.min_trend_strength and
            self.lines.supply[0] > self.lines.demand[0]):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'demand_supply': {
                'demand': self.lines.demand[0],
                'supply': self.lines.supply[0],
                'ratio': self.lines.ds_ratio[0],
                'smoothed_ratio': self.lines.smoothed_ratio[0]
            },
            'market': {
                'force': self.lines.market_force[0],
                'state': (
                    'demand_driven' if self.lines.market_force[0] > 0
                    else 'supply_driven'
                ),
                'intensity': abs(self.lines.market_force[0])
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'persistence': (
                    np.mean([
                        1 if force > 0
                        else -1 if force < 0
                        else 0
                        for force in self.force_history[-5:]
                    ]) if len(self.force_history) >= 5
                    else 0
                )
            },
            'volume': {
                'current': self.data.volume[0],
                'average': (
                    np.mean(self.volume_history)
                    if self.volume_history
                    else 0
                ),
                'trend': (
                    'increasing'
                    if len(self.volume_history) >= 2 and
                    self.volume_history[-1] > self.volume_history[-2]
                    else 'decreasing'
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    self.lines.trend_strength[0] *
                    abs(self.lines.market_force[0]) *
                    (self.lines.demand[0] / self.lines.supply[0]
                     if self.lines.supply[0] > 0
                     else float('inf'))
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'ratio_stability': (
                    np.std(self.ratio_history)
                    if len(self.ratio_history) > 1
                    else 0
                ),
                'force_stability': (
                    np.std(self.force_history)
                    if len(self.force_history) > 1
                    else 0
                )
            }
        }
