import backtrader as bt
from typing import List, Dict, Any, Optional
import numpy as np

class FlexibleStrategy(bt.Strategy):
    """
    Flexible Strategie-Basisklasse die mehrere Indikatoren kombinieren kann.
    
    Features:
    - Dynamische Indikator-Kombination
    - Gewichtete Signale
    - Anpassbare Ein- und Ausstiegsregeln
    - Risikomanagement-Integration
    """
    
    params = (
        ('indicators', {}),  # Dict mit Indikator-Konfigurationen
        ('weights', {}),     # Gewichtung der Indikatoren
        ('risk_perc', 2.0),  # Risiko pro Trade in Prozent
        ('stop_loss', 2.0),  # Stop Loss in Prozent
        ('take_profit', 4.0) # Take Profit in Prozent
    )
    
    def __init__(self):
        self.indicators = {}
        self.order = None
        self.stop_order = None
        self.profit_order = None
        
        # Indikatoren dynamisch initialisieren
        for ind_name, ind_config in self.p.indicators.items():
            ind_class = ind_config['class']
            ind_params = ind_config.get('params', {})
            self.indicators[ind_name] = ind_class(**ind_params)
    
    def get_signal_strength(self) -> float:
        """
        Berechnet die gewichtete Signalstärke aller Indikatoren
        Returns:
            float: Wert zwischen -1 (Strong Sell) und 1 (Strong Buy)
        """
        total_signal = 0
        total_weight = 0
        
        for ind_name, indicator in self.indicators.items():
            weight = self.p.weights.get(ind_name, 1.0)
            
            # Signallogik für verschiedene Indikatortypen
            if hasattr(indicator, 'buy_signal'):
                signal = 1.0 if indicator.buy_signal[0] else (-1.0 if indicator.sell_signal[0] else 0.0)
            elif hasattr(indicator, 'exhaustion'):
                # Für Trend Exhaustion
                signal = (indicator.exhaustion[0] - 50) / 50  # Normalisieren auf -1 bis 1
            else:
                # Generische Signalberechnung
                signal = 0
            
            total_signal += signal * weight
            total_weight += weight
        
        return total_signal / total_weight if total_weight else 0
    
    def next(self):
        if self.order:
            return
            
        signal = self.get_signal_strength()
        
        # Starkes Kaufsignal
        if signal > 0.7 and not self.position:
            size = self.calculate_position_size()
            self.order = self.buy(size=size)
            self.set_stop_and_profit()
            
        # Starkes Verkaufssignal
        elif signal < -0.7 and self.position:
            self.order = self.sell()
            
    def set_stop_and_profit(self):
        """Setzt Stop Loss und Take Profit Orders"""
        if not self.position:
            return
            
        price = self.position.price
        stop_price = price * (1 - self.p.stop_loss/100)
        profit_price = price * (1 + self.p.take_profit/100)
        
        self.stop_order = self.sell(exectype=bt.Order.Stop, price=stop_price)
        self.profit_order = self.sell(exectype=bt.Order.Limit, price=profit_price)
    
    def calculate_position_size(self) -> int:
        """Berechnet die Positionsgröße basierend auf Risikomanagement"""
        cash = self.broker.getcash()
        risk_amount = cash * (self.p.risk_perc / 100)
        price = self.data.close[0]
        stop_loss_amount = price * (self.p.stop_loss / 100)
        
        if stop_loss_amount == 0:
            return 1
            
        size = risk_amount / stop_loss_amount
        return int(size)
