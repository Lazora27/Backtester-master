import backtrader as bt
import numpy as np
from collections import defaultdict

class LevelIILiquidity(bt.Indicator):
    """
    Level II Liquidity Indicator
    
    Ein fortgeschrittener Indikator zur Analyse der
    Level II Marktliquidität.
    
    Features:
    - Level II Datenanalyse
    - Liquiditätsflussberechnung
    - Markttiefenanalyse
    - Signalgenerierung
    
    Parameter:
    - depth_levels (10): Anzahl der Preisebenen
    - liquidity_threshold (5000): Liquiditätsschwelle
    - refresh_period (20): Aktualisierungsperiode
    """
    
    lines = ('liquidity_ratio', 'depth_score',
             'flow_strength', 'spread_quality',
             'signal')
             
    params = (
        ('depth_levels', 10),
        ('liquidity_threshold', 5000),
        ('refresh_period', 20)
    )
    
    plotlines = dict(
        liquidity_ratio=dict(color='blue', _name='Liquidity Ratio'),
        depth_score=dict(color='red', _name='Depth Score'),
        flow_strength=dict(color='green', _name='Flow Strength'),
        spread_quality=dict(color='purple', _name='Spread Quality'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(LevelIILiquidity, self).__init__()
        
        # Level II Daten
        self.bid_book = defaultdict(float)
        self.ask_book = defaultdict(float)
        self.price_levels = []
        self.spread_history = []
        
    def update_order_book(self, price, volume, is_bid):
        """
        Aktualisiert das Level II Order Book.
        """
        level = self.get_price_level(price)
        
        if is_bid:
            self.bid_book[level] += volume
        else:
            self.ask_book[level] += volume
            
        if level not in self.price_levels:
            self.price_levels.append(level)
            self.price_levels.sort()
            
    def get_price_level(self, price):
        """
        Ordnet einen Preis einer Preisebene zu.
        """
        return round(price, 2)
        
    def calculate_liquidity_ratio(self):
        """
        Berechnet das Liquiditätsverhältnis.
        """
        total_bid_liquidity = sum(self.bid_book.values())
        total_ask_liquidity = sum(self.ask_book.values())
        
        if total_bid_liquidity + total_ask_liquidity == 0:
            return 0
            
        return (
            (total_bid_liquidity - total_ask_liquidity) /
            (total_bid_liquidity + total_ask_liquidity)
        )
        
    def calculate_depth_score(self):
        """
        Berechnet den Tiefenscore.
        """
        if not self.price_levels:
            return 0
            
        depth_weights = np.linspace(
            1.0,
            0.2,
            min(len(self.price_levels),
                self.p.depth_levels)
        )
        
        weighted_depth = 0
        for i, level in enumerate(self.price_levels[:self.p.depth_levels]):
            bid_depth = self.bid_book.get(level, 0)
            ask_depth = self.ask_book.get(level, 0)
            
            weighted_depth += (
                (bid_depth + ask_depth) *
                depth_weights[i]
            )
            
        return weighted_depth / self.p.liquidity_threshold
        
    def calculate_flow_strength(self):
        """
        Berechnet die Flussstärke.
        """
        if not self.price_levels:
            return 0
            
        current_level = self.get_price_level(
            self.data.close[0]
        )
        
        # Fluss in der Nähe des aktuellen Preises
        flow = 0
        for level in self.price_levels:
            if abs(level - current_level) <= 0.02:
                bid_flow = self.bid_book.get(level, 0)
                ask_flow = self.ask_book.get(level, 0)
                
                if bid_flow + ask_flow > 0:
                    flow += (bid_flow - ask_flow) / (
                        bid_flow + ask_flow
                    )
                    
        return flow / min(
            len(self.price_levels),
            self.p.depth_levels
        )
        
    def calculate_spread_quality(self):
        """
        Berechnet die Spread-Qualität.
        """
        if len(self.spread_history) < 2:
            return 0
            
        avg_spread = np.mean(self.spread_history)
        if avg_spread == 0:
            return 0
            
        current_spread = self.spread_history[-1]
        return 1 - (current_spread / avg_spread)
        
    def next(self):
        # Order Book aktualisieren
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        is_bid = (
            self.data.close[0] > self.data.open[0]
            if len(self.price_levels) > 0
            else True
        )
        
        self.update_order_book(price, volume, is_bid)
        
        # Spread berechnen und speichern
        if len(self.price_levels) >= 2:
            spread = (
                min(self.ask_book.keys()) -
                max(self.bid_book.keys())
            )
            self.spread_history.append(spread)
            
        # Metriken berechnen
        liquidity_ratio = self.calculate_liquidity_ratio()
        depth_score = self.calculate_depth_score()
        flow_strength = self.calculate_flow_strength()
        spread_quality = self.calculate_spread_quality()
        
        # Linien aktualisieren
        self.lines.liquidity_ratio[0] = liquidity_ratio
        self.lines.depth_score[0] = depth_score
        self.lines.flow_strength[0] = flow_strength
        self.lines.spread_quality[0] = spread_quality
        
        # Signal
        if depth_score > 1.0:
            if (liquidity_ratio > 0.2 and
                flow_strength > 0):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (liquidity_ratio < -0.2 and
                  flow_strength < 0):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        if len(self.spread_history) > self.p.refresh_period:
            self.spread_history.pop(0)
            
        # Order Book periodisch zurücksetzen
        if len(self.data) % self.p.refresh_period == 0:
            self.bid_book.clear()
            self.ask_book.clear()
            self.price_levels = []
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'liquidity': {
                'ratio': self.lines.liquidity_ratio[0],
                'depth': self.lines.depth_score[0],
                'flow': self.lines.flow_strength[0],
                'spread': self.lines.spread_quality[0]
            },
            'order_book': {
                'bid_levels': len(self.bid_book),
                'ask_levels': len(self.ask_book),
                'total_depth': (
                    sum(self.bid_book.values()) +
                    sum(self.ask_book.values())
                ),
                'spread': (
                    self.spread_history[-1]
                    if self.spread_history
                    else None
                )
            },
            'market_quality': {
                'depth_state': (
                    'deep'
                    if self.lines.depth_score[0] > 1.2
                    else 'moderate'
                    if self.lines.depth_score[0] > 0.8
                    else 'shallow'
                ),
                'flow_bias': (
                    'buying'
                    if self.lines.flow_strength[0] > 0.1
                    else 'selling'
                    if self.lines.flow_strength[0] < -0.1
                    else 'neutral'
                ),
                'spread_state': (
                    'tight'
                    if self.lines.spread_quality[0] > 0.8
                    else 'wide'
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
                    self.lines.depth_score[0] *
                    abs(self.lines.liquidity_ratio[0])
                )
            },
            'market_conditions': {
                'liquidity_quality': (
                    'high'
                    if self.lines.depth_score[0] > 1.0
                    else 'low'
                ),
                'flow_quality': (
                    'strong'
                    if abs(self.lines.flow_strength[0]) > 0.15
                    else 'weak'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.depth_score[0] > 0.8 and
                        self.lines.spread_quality[0] > 0.7)
                    else 'unfavorable'
                )
            }
        }
