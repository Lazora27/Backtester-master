import backtrader as bt
import numpy as np

class BidAskVolumeDelta(bt.Indicator):
    """
    Bid-Ask Volume Delta Indicator
    
    Ein fortgeschrittener Indikator zur Analyse des
    Verhältnisses zwischen Bid- und Ask-Volumen.
    
    Features:
    - Bid-Ask Volumenanalyse
    - Kumulativer Volumendelta
    - Volumenimpulsberechnung
    - Signalgenerierung
    
    Parameter:
    - delta_period (20): Deltaberechnungsperiode
    - volume_threshold (1000): Volumenschwelle
    - smooth_period (5): Glättungsperiode
    """
    
    lines = ('volume_delta', 'cumulative_delta',
             'volume_impulse', 'pressure_ratio',
             'signal')
             
    params = (
        ('delta_period', 20),
        ('volume_threshold', 1000),
        ('smooth_period', 5)
    )
    
    plotlines = dict(
        volume_delta=dict(color='blue', _name='Volume Delta'),
        cumulative_delta=dict(color='red', _name='Cumulative Delta'),
        volume_impulse=dict(color='green', _name='Volume Impulse'),
        pressure_ratio=dict(color='purple', _name='Pressure Ratio'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(BidAskVolumeDelta, self).__init__()
        
        # Historie
        self.bid_volume_history = []
        self.ask_volume_history = []
        self.delta_history = []
        self.price_history = []
        
    def calculate_volume_delta(self):
        """
        Berechnet den Volumendelta.
        """
        if not self.bid_volume_history:
            return 0
            
        # Bid-Ask Differenz
        bid_volume = self.bid_volume_history[-1]
        ask_volume = self.ask_volume_history[-1]
        
        return ask_volume - bid_volume
        
    def calculate_cumulative_delta(self):
        """
        Berechnet den kumulativen Delta.
        """
        if len(self.delta_history) < self.p.delta_period:
            return sum(self.delta_history)
            
        return sum(
            self.delta_history[-self.p.delta_period:]
        )
        
    def calculate_volume_impulse(self):
        """
        Berechnet den Volumenimpuls.
        """
        if len(self.delta_history) < self.p.smooth_period:
            return 0
            
        recent_deltas = self.delta_history[
            -self.p.smooth_period:
        ]
        
        # Impuls basierend auf Delta-Änderung
        return (
            sum(recent_deltas) /
            (self.p.smooth_period * self.p.volume_threshold)
        )
        
    def calculate_pressure_ratio(self):
        """
        Berechnet das Druckverhältnis.
        """
        if not (self.bid_volume_history and
                self.ask_volume_history):
            return 0
            
        total_volume = (
            self.bid_volume_history[-1] +
            self.ask_volume_history[-1]
        )
        
        if total_volume > 0:
            return (
                self.ask_volume_history[-1] /
                total_volume
            )
        return 0.5
        
    def next(self):
        # Volumen und Preis speichern
        bid_volume = self.data.volume[0] * (
            1 if self.data.close[0] <= self.data.open[0]
            else 0.5
        )
        ask_volume = self.data.volume[0] * (
            1 if self.data.close[0] > self.data.open[0]
            else 0.5
        )
        
        self.bid_volume_history.append(bid_volume)
        self.ask_volume_history.append(ask_volume)
        self.price_history.append(self.data.close[0])
        
        # Delta berechnen
        volume_delta = self.calculate_volume_delta()
        self.delta_history.append(volume_delta)
        
        # Weitere Metriken
        cumulative_delta = self.calculate_cumulative_delta()
        volume_impulse = self.calculate_volume_impulse()
        pressure_ratio = self.calculate_pressure_ratio()
        
        # Linien aktualisieren
        self.lines.volume_delta[0] = volume_delta
        self.lines.cumulative_delta[0] = cumulative_delta
        self.lines.volume_impulse[0] = volume_impulse
        self.lines.pressure_ratio[0] = pressure_ratio
        
        # Signal
        if abs(volume_delta) > self.p.volume_threshold:
            if (volume_delta > 0 and
                pressure_ratio > 0.6):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (volume_delta < 0 and
                  pressure_ratio < 0.4):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.delta_period,
            self.p.smooth_period
        )
        for hist in [self.bid_volume_history,
                    self.ask_volume_history,
                    self.delta_history,
                    self.price_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'volume': {
                'delta': self.lines.volume_delta[0],
                'cumulative': self.lines.cumulative_delta[0],
                'impulse': self.lines.volume_impulse[0],
                'pressure': self.lines.pressure_ratio[0]
            },
            'flow_analysis': {
                'direction': (
                    'buying'
                    if self.lines.volume_delta[0] > 0
                    else 'selling'
                ),
                'strength': (
                    abs(self.lines.volume_delta[0]) /
                    self.p.volume_threshold
                ),
                'persistence': (
                    'persistent'
                    if abs(
                        self.lines.cumulative_delta[0]
                    ) > self.p.volume_threshold * 5
                    else 'temporary'
                )
            },
            'pressure_analysis': {
                'level': self.lines.pressure_ratio[0],
                'bias': (
                    'bullish'
                    if self.lines.pressure_ratio[0] > 0.55
                    else 'bearish'
                    if self.lines.pressure_ratio[0] < 0.45
                    else 'neutral'
                ),
                'intensity': (
                    'high'
                    if abs(
                        self.lines.pressure_ratio[0] - 0.5
                    ) > 0.1
                    else 'low'
                )
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'reliability': (
                    abs(self.lines.volume_delta[0]) /
                    self.p.volume_threshold *
                    abs(self.lines.pressure_ratio[0] - 0.5) * 2
                )
            },
            'market_conditions': {
                'volume_quality': (
                    'high'
                    if self.data.volume[0] >
                       self.p.volume_threshold
                    else 'low'
                ),
                'flow_balance': (
                    'balanced'
                    if abs(
                        self.lines.pressure_ratio[0] - 0.5
                    ) < 0.05
                    else 'imbalanced'
                ),
                'trading_environment': (
                    'favorable'
                    if (abs(self.lines.volume_delta[0]) >
                        self.p.volume_threshold * 0.8 and
                        abs(self.lines.pressure_ratio[0] - 0.5) > 0.08)
                    else 'unfavorable'
                )
            }
        }
