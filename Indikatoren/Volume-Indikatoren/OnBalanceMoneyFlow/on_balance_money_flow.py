import backtrader as bt
import numpy as np

class OnBalanceMoneyFlow(bt.Indicator):
    """
    On-Balance Money Flow
    
    Ein Indikator, der den kumulativen Geldfluss basierend
    auf Preis und Volumen analysiert.
    
    Features:
    - Geldflussanalyse
    - Volumengewichtung
    - Trendbestätigung
    - Divergenzanalyse
    - Signal-Validierung
    
    Parameter:
    - period (20): Basisperiode
    - volume_factor (1.0): Volumenfaktor
    - price_weight (0.6): Preisgewichtung
    """
    
    lines = ('money_flow', 'smoothed_flow',
             'flow_force', 'trend_strength',
             'divergence', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 20),
        ('volume_factor', 1.0),
        ('price_weight', 0.6),
        ('min_strength', 0.3)
    )
    
    plotlines = dict(
        money_flow=dict(color='blue', _name='Money Flow'),
        smoothed_flow=dict(color='red', _name='Smoothed Flow'),
        flow_force=dict(color='green', _name='Flow Force'),
        trend_strength=dict(color='purple', _name='Trend Strength'),
        divergence=dict(color='orange', _name='Divergence'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(OnBalanceMoneyFlow, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.flow_history = []
        self.price_history = []
        self.volume_history = []
        
    def calculate_money_flow(self):
        """
        Berechnet den Geldfluss.
        """
        if len(self.data) < 2:
            return 0
            
        # Typischer Preis
        typical_price = (
            self.data.high[0] + self.data.low[0] +
            self.data.close[0]
        ) / 3
        
        # Preisänderung
        price_change = (
            self.data.close[0] - self.data.close[-1]
        ) / self.data.close[-1] if self.data.close[-1] != 0 else 0
        
        # Volumengewichtung
        volume_weight = (
            self.data.volume[0] ** self.p.volume_factor
        )
        
        # Geldfluss berechnen
        money_flow = (
            price_change * self.p.price_weight +
            (1 - self.p.price_weight)
        ) * volume_weight * typical_price
        
        return money_flow
        
    def calculate_flow_force(self):
        """
        Berechnet die Flussstärke.
        """
        if len(self.flow_history) < self.p.period:
            return 0
            
        # Durchschnittlicher Fluss
        avg_flow = np.mean(self.flow_history[-self.p.period:])
        
        # Flussstärke
        if avg_flow != 0:
            flow_force = (
                self.lines.money_flow[0] / avg_flow - 1
            )
        else:
            flow_force = 0
            
        return flow_force
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und Geldfluss.
        """
        if len(self.flow_history) < self.p.period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.period:])
        price_low = min(self.price_history[-self.p.period:])
        
        # Flusshochs/-tiefs
        flow_high = max(self.flow_history[-self.p.period:])
        flow_low = min(self.flow_history[-self.p.period:])
        
        # Bullische Divergenz
        if price_low < price_high and flow_low > flow_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and flow_low < flow_high:
            return -1
            
        return 0
        
    def next(self):
        # Geldfluss berechnen
        self.lines.money_flow[0] = self.calculate_money_flow()
        self.flow_history.append(self.lines.money_flow[0])
        
        # Geglätteter Fluss
        self.lines.smoothed_flow[0] = bt.indicators.EMA(
            self.lines.money_flow, period=self.p.period
        )[0]
        
        # Flussstärke
        self.lines.flow_force[0] = self.calculate_flow_force()
        
        # Trendstärke
        if len(self.flow_history) >= self.p.period:
            self.lines.trend_strength[0] = abs(
                np.mean(self.flow_history[-self.p.period:])
            )
        else:
            self.lines.trend_strength[0] = 0
            
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Historie aktualisieren
        self.price_history.append(self.data.close[0])
        self.volume_history.append(self.data.volume[0])
        
        # Historie begrenzen
        max_period = self.p.period
        for hist in [self.flow_history, self.price_history,
                    self.volume_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_flow[0] > 0 and
            self.lines.flow_force[0] > 0 and
            self.lines.trend_strength[0] > self.p.min_strength and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_flow[0] < 0 and
            self.lines.flow_force[0] < 0 and
            self.lines.trend_strength[0] > self.p.min_strength and
            self.lines.divergence[0] <= 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'money_flow': {
                'current': self.lines.money_flow[0],
                'smoothed': self.lines.smoothed_flow[0],
                'force': self.lines.flow_force[0],
                'trend': (
                    'bullish' if self.lines.money_flow[0] > 0
                    else 'bearish'
                )
            },
            'volume': {
                'weight': (
                    self.data.volume[0] ** self.p.volume_factor
                ),
                'trend': (
                    'increasing' if self.data.volume[0] > np.mean(self.volume_history)
                    else 'decreasing'
                    if len(self.volume_history) > 0
                    else 'neutral'
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'persistence': (
                    np.mean([
                        1 if f > 0 else -1
                        for f in self.flow_history[-5:]
                    ]) if len(self.flow_history) >= 5
                    else 0
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
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    self.lines.trend_strength[0] *
                    abs(self.lines.flow_force[0])
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'flow_volatility': (
                    np.std(self.flow_history)
                    if len(self.flow_history) > 1
                    else 0
                ),
                'divergence_risk': abs(self.lines.divergence[0])
            }
        }
