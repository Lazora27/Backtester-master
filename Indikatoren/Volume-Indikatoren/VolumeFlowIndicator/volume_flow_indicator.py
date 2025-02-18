import backtrader as bt
import numpy as np

class VolumeFlowIndicator(bt.Indicator):
    """
    Volume Flow Indicator (VFI)
    
    Ein fortgeschrittener Indikator, der den Volumenfluss
    in Relation zur Preisdynamik analysiert.
    
    Features:
    - Volumenflussanalyse
    - Preisdynamik
    - Trendbestätigung
    - Marktphasenanalyse
    - Signalgenerierung
    
    Parameter:
    - period (20): Analysezeitraum
    - vf_threshold (0.2): Volumenflussschwelle
    - price_factor (0.7): Preisgewichtung
    """
    
    lines = ('vfi', 'smoothed_vfi',
             'flow_strength', 'price_momentum',
             'market_phase', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 20),
        ('vf_threshold', 0.2),
        ('price_factor', 0.7),
        ('min_strength', 0.3)
    )
    
    plotlines = dict(
        vfi=dict(color='blue', _name='VFI'),
        smoothed_vfi=dict(color='red', _name='Smoothed VFI'),
        flow_strength=dict(color='green', _name='Flow Strength'),
        price_momentum=dict(color='purple', _name='Price Momentum'),
        market_phase=dict(color='orange', _name='Market Phase'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(VolumeFlowIndicator, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.vfi_history = []
        self.price_history = []
        self.volume_history = []
        
    def calculate_vfi(self):
        """
        Berechnet den Volume Flow Indicator.
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
            typical_price - typical_price
        ) if typical_price != 0 else 0
        
        # Volumenfluss
        if abs(price_change) > self.p.vf_threshold:
            volume_flow = (
                self.data.volume[0] *
                np.sign(price_change)
            )
        else:
            volume_flow = 0
            
        # VFI berechnen
        vfi = (
            volume_flow * self.p.price_factor +
            price_change * (1 - self.p.price_factor)
        )
        
        return vfi
        
    def calculate_flow_strength(self):
        """
        Berechnet die Flussstärke.
        """
        if len(self.vfi_history) < self.p.period:
            return 0
            
        # Durchschnittlicher VFI
        avg_vfi = np.mean(self.vfi_history[-self.p.period:])
        
        # Flussstärke
        if avg_vfi != 0:
            strength = (
                self.lines.vfi[0] / avg_vfi - 1
            )
        else:
            strength = 0
            
        return strength
        
    def calculate_price_momentum(self):
        """
        Berechnet das Preismomentum.
        """
        if len(self.price_history) < self.p.period:
            return 0
            
        # Preisänderung
        price_change = (
            self.data.close[0] - self.price_history[-self.p.period]
        ) / self.price_history[-self.p.period]
        
        return price_change
        
    def calculate_market_phase(self):
        """
        Berechnet die Marktphase.
        """
        if len(self.vfi_history) < self.p.period:
            return 0
            
        # Trendrichtung
        trend_direction = np.mean([
            1 if vfi > self.vfi_history[i-1]
            else -1
            for i, vfi in enumerate(self.vfi_history[-5:])
            if i > 0
        ]) if len(self.vfi_history) >= 5 else 0
        
        # Trendstärke
        trend_strength = abs(
            np.mean(self.vfi_history[-self.p.period:])
        )
        
        return trend_direction * trend_strength
        
    def next(self):
        # VFI berechnen
        self.lines.vfi[0] = self.calculate_vfi()
        self.vfi_history.append(self.lines.vfi[0])
        
        # Geglätteter VFI
        self.lines.smoothed_vfi[0] = bt.indicators.EMA(
            self.lines.vfi, period=self.p.period
        )[0]
        
        # Flussstärke
        self.lines.flow_strength[0] = self.calculate_flow_strength()
        
        # Preismomentum
        self.lines.price_momentum[0] = self.calculate_price_momentum()
        
        # Marktphase
        self.lines.market_phase[0] = self.calculate_market_phase()
        
        # Historie aktualisieren
        self.price_history.append(self.data.close[0])
        self.volume_history.append(self.data.volume[0])
        
        # Historie begrenzen
        max_period = self.p.period
        for hist in [self.vfi_history, self.price_history,
                    self.volume_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_vfi[0] > 0 and
            self.lines.flow_strength[0] > 0 and
            self.lines.price_momentum[0] > 0 and
            self.lines.market_phase[0] > self.p.min_strength):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_vfi[0] < 0 and
            self.lines.flow_strength[0] < 0 and
            self.lines.price_momentum[0] < 0 and
            self.lines.market_phase[0] < -self.p.min_strength):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'volume_flow': {
                'current': self.lines.vfi[0],
                'smoothed': self.lines.smoothed_vfi[0],
                'strength': self.lines.flow_strength[0],
                'trend': (
                    'positive' if self.lines.vfi[0] > 0
                    else 'negative'
                )
            },
            'momentum': {
                'price': self.lines.price_momentum[0],
                'strength': abs(self.lines.price_momentum[0]),
                'quality': (
                    'strong' if abs(self.lines.price_momentum[0]) > 0.5
                    else 'weak'
                )
            },
            'market': {
                'phase': self.lines.market_phase[0],
                'condition': (
                    'bullish' if self.lines.market_phase[0] > 0
                    else 'bearish'
                ),
                'strength': abs(self.lines.market_phase[0])
            },
            'flow': {
                'strength': self.lines.flow_strength[0],
                'persistence': (
                    np.mean([
                        1 if vfi > 0 else -1
                        for vfi in self.vfi_history[-5:]
                    ]) if len(self.vfi_history) >= 5
                    else 0
                ),
                'quality': (
                    'improving' if self.lines.flow_strength[0] > 0
                    else 'deteriorating'
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(self.lines.market_phase[0]),
                'reliability': (
                    abs(self.lines.market_phase[0]) *
                    abs(self.lines.flow_strength[0])
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'flow_volatility': (
                    np.std(self.vfi_history)
                    if len(self.vfi_history) > 1
                    else 0
                ),
                'momentum_risk': abs(self.lines.price_momentum[0])
            }
        }
