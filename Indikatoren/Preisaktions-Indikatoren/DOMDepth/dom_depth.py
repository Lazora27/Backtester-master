import backtrader as bt
import numpy as np
from collections import defaultdict

class DOMDepth(bt.Indicator):
    """
    DOM Depth Indicator
    
    Ein fortgeschrittener Indikator zur Analyse der
    Markttiefe (Depth of Market).
    
    Features:
    - Order Book Analyse
    - Liquiditätstiefe
    - Preisdruck-Berechnung
    - Signalgenerierung
    
    Parameter:
    - depth_levels (10): Anzahl der DOM-Ebenen
    - volume_threshold (1000): Volumenschwelle
    - imbalance_threshold (0.2): Ungleichgewichtsschwelle
    """
    
    lines = ('depth_imbalance', 'liquidity_score',
             'price_pressure', 'order_flow',
             'signal')
             
    params = (
        ('depth_levels', 10),
        ('volume_threshold', 1000),
        ('imbalance_threshold', 0.2)
    )
    
    plotlines = dict(
        depth_imbalance=dict(color='blue', _name='Depth Imbalance'),
        liquidity_score=dict(color='red', _name='Liquidity Score'),
        price_pressure=dict(color='green', _name='Price Pressure'),
        order_flow=dict(color='purple', _name='Order Flow'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(DOMDepth, self).__init__()
        
        # Order Book Tracking
        self.bid_levels = defaultdict(float)
        self.ask_levels = defaultdict(float)
        self.price_history = []
        self.volume_history = []
        
    def update_order_book(self, price, volume, is_bid):
        """
        Aktualisiert das Order Book.
        """
        level_size = self.calculate_level_size()
        level = int(price / level_size)
        
        if is_bid:
            self.bid_levels[level] += volume
        else:
            self.ask_levels[level] += volume
            
    def calculate_level_size(self):
        """
        Berechnet die Größe einer Preisebene.
        """
        if len(self.price_history) < 2:
            return 1.0
            
        price_range = max(self.price_history) - min(self.price_history)
        return price_range / self.p.depth_levels
        
    def calculate_depth_imbalance(self):
        """
        Berechnet das Ungleichgewicht in der Markttiefe.
        """
        total_bids = sum(self.bid_levels.values())
        total_asks = sum(self.ask_levels.values())
        
        if total_bids + total_asks == 0:
            return 0
            
        return (total_bids - total_asks) / (total_bids + total_asks)
        
    def calculate_liquidity_score(self):
        """
        Berechnet den Liquiditätsscore.
        """
        if not (self.bid_levels and self.ask_levels):
            return 0
            
        # Durchschnittliches Volumen pro Level
        avg_bid_volume = (
            sum(self.bid_levels.values()) /
            len(self.bid_levels)
        )
        avg_ask_volume = (
            sum(self.ask_levels.values()) /
            len(self.ask_levels)
        )
        
        return (avg_bid_volume + avg_ask_volume) / (
            2 * self.p.volume_threshold
        )
        
    def calculate_price_pressure(self):
        """
        Berechnet den Preisdruck.
        """
        if not (self.bid_levels and self.ask_levels):
            return 0
            
        current_price = self.price_history[-1]
        level_size = self.calculate_level_size()
        current_level = int(current_price / level_size)
        
        # Druck von benachbarten Levels
        pressure = 0
        for level in range(
            current_level - 2,
            current_level + 3
        ):
            bid_volume = self.bid_levels.get(level, 0)
            ask_volume = self.ask_levels.get(level, 0)
            
            if bid_volume + ask_volume > 0:
                level_pressure = (
                    (bid_volume - ask_volume) /
                    (bid_volume + ask_volume)
                )
                pressure += level_pressure * (
                    1 - abs(level - current_level) * 0.2
                )
                
        return pressure / 3
        
    def calculate_order_flow(self):
        """
        Berechnet den Order Flow.
        """
        if len(self.volume_history) < 2:
            return 0
            
        # Volumenänderung
        volume_change = (
            self.volume_history[-1] -
            self.volume_history[-2]
        )
        
        # Preisänderung
        price_change = (
            self.price_history[-1] -
            self.price_history[-2]
        )
        
        if abs(price_change) > 0:
            return volume_change * np.sign(price_change)
        return 0
        
    def next(self):
        # Preis und Volumen speichern
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        self.price_history.append(price)
        self.volume_history.append(volume)
        
        # Order Book aktualisieren
        is_bid = (
            price > self.price_history[-2]
            if len(self.price_history) > 1
            else True
        )
        self.update_order_book(price, volume, is_bid)
        
        # Metriken berechnen
        depth_imbalance = self.calculate_depth_imbalance()
        liquidity_score = self.calculate_liquidity_score()
        price_pressure = self.calculate_price_pressure()
        order_flow = self.calculate_order_flow()
        
        # Linien aktualisieren
        self.lines.depth_imbalance[0] = depth_imbalance
        self.lines.liquidity_score[0] = liquidity_score
        self.lines.price_pressure[0] = price_pressure
        self.lines.order_flow[0] = order_flow
        
        # Signal
        if liquidity_score > 0.8:
            if (depth_imbalance > self.p.imbalance_threshold and
                price_pressure > 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (depth_imbalance < -self.p.imbalance_threshold and
                  price_pressure < 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_length = self.p.depth_levels * 2
        if len(self.price_history) > max_length:
            self.price_history.pop(0)
            self.volume_history.pop(0)
            
        # Order Book periodisch zurücksetzen
        if len(self.price_history) % 10 == 0:
            self.bid_levels.clear()
            self.ask_levels.clear()
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'depth': {
                'imbalance': self.lines.depth_imbalance[0],
                'liquidity': self.lines.liquidity_score[0],
                'pressure': self.lines.price_pressure[0],
                'flow': self.lines.order_flow[0]
            },
            'order_book': {
                'bid_levels': {
                    str(level): volume
                    for level, volume
                    in self.bid_levels.items()
                },
                'ask_levels': {
                    str(level): volume
                    for level, volume
                    in self.ask_levels.items()
                },
                'total_depth': (
                    sum(self.bid_levels.values()) +
                    sum(self.ask_levels.values())
                )
            },
            'market_structure': {
                'liquidity_state': (
                    'high'
                    if self.lines.liquidity_score[0] > 1.2
                    else 'moderate'
                    if self.lines.liquidity_score[0] > 0.8
                    else 'low'
                ),
                'pressure_bias': (
                    'buying'
                    if self.lines.price_pressure[0] > 0.1
                    else 'selling'
                    if self.lines.price_pressure[0] < -0.1
                    else 'neutral'
                ),
                'depth_distribution': (
                    'balanced'
                    if abs(self.lines.depth_imbalance[0]) < 0.1
                    else 'imbalanced'
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
                    self.lines.liquidity_score[0] *
                    abs(self.lines.depth_imbalance[0])
                )
            },
            'market_conditions': {
                'depth_quality': (
                    'high'
                    if self.lines.liquidity_score[0] > 1.0
                    else 'low'
                ),
                'order_flow_state': (
                    'aggressive'
                    if abs(self.lines.order_flow[0]) >
                       self.p.volume_threshold
                    else 'passive'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.liquidity_score[0] > 0.8 and
                        abs(self.lines.depth_imbalance[0]) >
                        self.p.imbalance_threshold * 0.8)
                    else 'unfavorable'
                )
            }
        }
