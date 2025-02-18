import backtrader as bt
import numpy as np
from collections import defaultdict

class OrderBookHeatmap(bt.Indicator):
    """
    Order Book Heatmap Indicator
    
    Ein fortgeschrittener Indikator zur Visualisierung und
    Analyse des Order Books als Heatmap.
    
    Features:
    - Order Book Visualisierung
    - Liquiditätscluster-Erkennung
    - Preisdruck-Analyse
    - Signalgenerierung
    
    Parameter:
    - book_levels (20): Anzahl der Order Book Ebenen
    - heat_threshold (2000): Wärmeschwelle
    - update_period (10): Aktualisierungsperiode
    """
    
    lines = ('book_pressure', 'cluster_strength',
             'heat_distribution', 'book_imbalance',
             'signal')
             
    params = (
        ('book_levels', 20),
        ('heat_threshold', 2000),
        ('update_period', 10)
    )
    
    plotlines = dict(
        book_pressure=dict(color='blue', _name='Book Pressure'),
        cluster_strength=dict(color='red', _name='Cluster Strength'),
        heat_distribution=dict(color='green', _name='Heat Distribution'),
        book_imbalance=dict(color='purple', _name='Book Imbalance'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(OrderBookHeatmap, self).__init__()
        
        # Order Book Tracking
        self.bid_heat = defaultdict(float)
        self.ask_heat = defaultdict(float)
        self.price_levels = []
        self.volume_clusters = []
        
    def update_book_heat(self, price, volume, is_bid):
        """
        Aktualisiert die Order Book Heatmap.
        """
        level = self.get_price_level(price)
        
        # Wärme aktualisieren
        if is_bid:
            self.bid_heat[level] += volume
        else:
            self.ask_heat[level] += volume
            
        # Preisebene speichern
        if level not in self.price_levels:
            self.price_levels.append(level)
            self.price_levels.sort()
            
    def get_price_level(self, price):
        """
        Ordnet einen Preis einer Preisebene zu.
        """
        return round(price, 2)
        
    def calculate_book_pressure(self):
        """
        Berechnet den Order Book Druck.
        """
        if not (self.bid_heat and self.ask_heat):
            return 0
            
        total_bid_heat = sum(self.bid_heat.values())
        total_ask_heat = sum(self.ask_heat.values())
        
        if total_bid_heat + total_ask_heat == 0:
            return 0
            
        return (
            (total_bid_heat - total_ask_heat) /
            (total_bid_heat + total_ask_heat)
        )
        
    def find_volume_clusters(self):
        """
        Findet Volumencluster im Order Book.
        """
        if not self.price_levels:
            return 0
            
        clusters = []
        current_cluster = []
        
        for level in self.price_levels:
            total_heat = (
                self.bid_heat.get(level, 0) +
                self.ask_heat.get(level, 0)
            )
            
            if total_heat > self.p.heat_threshold:
                current_cluster.append((level, total_heat))
            elif current_cluster:
                clusters.append(current_cluster)
                current_cluster = []
                
        if current_cluster:
            clusters.append(current_cluster)
            
        self.volume_clusters = clusters
        return len(clusters)
        
    def calculate_heat_distribution(self):
        """
        Berechnet die Wärmeverteilung.
        """
        if not self.price_levels:
            return 0
            
        heat_values = []
        for level in self.price_levels:
            total_heat = (
                self.bid_heat.get(level, 0) +
                self.ask_heat.get(level, 0)
            )
            heat_values.append(total_heat)
            
        if not heat_values:
            return 0
            
        # Gini-Koeffizient der Wärmeverteilung
        heat_values.sort()
        n = len(heat_values)
        distribution = sum(
            (2 * i - n - 1) * v
            for i, v in enumerate(heat_values)
        ) / (n * sum(heat_values))
        
        return (distribution + 1) / 2
        
    def calculate_book_imbalance(self):
        """
        Berechnet das Order Book Ungleichgewicht.
        """
        if not self.price_levels:
            return 0
            
        current_price = self.data.close[0]
        current_level = self.get_price_level(current_price)
        
        # Ungleichgewicht um aktuellen Preis
        local_bid_heat = sum(
            self.bid_heat.get(level, 0)
            for level in range(
                current_level - 2,
                current_level + 1
            )
        )
        local_ask_heat = sum(
            self.ask_heat.get(level, 0)
            for level in range(
                current_level,
                current_level + 3
            )
        )
        
        if local_bid_heat + local_ask_heat == 0:
            return 0
            
        return (
            (local_bid_heat - local_ask_heat) /
            (local_bid_heat + local_ask_heat)
        )
        
    def next(self):
        # Order Book aktualisieren
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        is_bid = (
            self.data.close[0] > self.data.open[0]
            if len(self.price_levels) > 0
            else True
        )
        
        self.update_book_heat(price, volume, is_bid)
        
        # Metriken berechnen
        book_pressure = self.calculate_book_pressure()
        cluster_strength = self.find_volume_clusters()
        heat_distribution = self.calculate_heat_distribution()
        book_imbalance = self.calculate_book_imbalance()
        
        # Linien aktualisieren
        self.lines.book_pressure[0] = book_pressure
        self.lines.cluster_strength[0] = cluster_strength
        self.lines.heat_distribution[0] = heat_distribution
        self.lines.book_imbalance[0] = book_imbalance
        
        # Signal
        if cluster_strength > 0:
            if (book_pressure > 0.2 and
                book_imbalance > 0.15):
                self.lines.signal[0] = 1  # Kaufsignal
            elif (book_pressure < -0.2 and
                  book_imbalance < -0.15):
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Order Book periodisch aktualisieren
        if len(self.data) % self.p.update_period == 0:
            # Wärme abkühlen lassen
            for heat_dict in [self.bid_heat, self.ask_heat]:
                for level in heat_dict:
                    heat_dict[level] *= 0.8
                    
            # Inaktive Levels entfernen
            self.bid_heat = defaultdict(
                float,
                {k: v for k, v in self.bid_heat.items()
                 if v > self.p.heat_threshold * 0.1}
            )
            self.ask_heat = defaultdict(
                float,
                {k: v for k, v in self.ask_heat.items()
                 if v > self.p.heat_threshold * 0.1}
            )
            
            # Preisebenen aktualisieren
            self.price_levels = sorted(
                set(self.bid_heat.keys()) |
                set(self.ask_heat.keys())
            )
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'book_state': {
                'pressure': self.lines.book_pressure[0],
                'clusters': len(self.volume_clusters),
                'distribution': self.lines.heat_distribution[0],
                'imbalance': self.lines.book_imbalance[0]
            },
            'cluster_analysis': {
                'count': len(self.volume_clusters),
                'locations': [
                    [level for level, _ in cluster]
                    for cluster in self.volume_clusters
                ],
                'strengths': [
                    sum(heat for _, heat in cluster)
                    for cluster in self.volume_clusters
                ]
            },
            'heat_analysis': {
                'distribution_type': (
                    'concentrated'
                    if self.lines.heat_distribution[0] > 0.7
                    else 'distributed'
                ),
                'pressure_bias': (
                    'buying'
                    if self.lines.book_pressure[0] > 0.1
                    else 'selling'
                    if self.lines.book_pressure[0] < -0.1
                    else 'neutral'
                ),
                'imbalance_state': (
                    'significant'
                    if abs(self.lines.book_imbalance[0]) > 0.2
                    else 'balanced'
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
                    abs(self.lines.book_pressure[0]) *
                    self.lines.cluster_strength[0] / 5
                )
            },
            'market_conditions': {
                'book_quality': (
                    'high'
                    if len(self.volume_clusters) > 0
                    else 'low'
                ),
                'pressure_quality': (
                    'strong'
                    if abs(self.lines.book_pressure[0]) > 0.25
                    else 'weak'
                ),
                'trading_environment': (
                    'favorable'
                    if (len(self.volume_clusters) > 0 and
                        abs(self.lines.book_pressure[0]) > 0.2)
                    else 'unfavorable'
                )
            }
        }
