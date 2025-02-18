import backtrader as bt
import numpy as np

class OpenInterest(bt.Indicator):
    """
    Open Interest Indicator
    
    Ein Indikator, der das offene Interesse in Verbindung
    mit Preis und Volumen analysiert.
    
    Features:
    - Open Interest Analyse
    - Volumenbestätigung
    - Marktliquidität
    - Trendstärkeberechnung
    - Signal-Validierung
    
    Parameter:
    - period (20): Basisperiode
    - volume_weight (0.4): Volumengewichtung
    - oi_weight (0.6): Open Interest Gewichtung
    """
    
    lines = ('oi_strength', 'smoothed_oi',
             'volume_confirm', 'market_depth',
             'trend_quality', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 20),
        ('volume_weight', 0.4),
        ('oi_weight', 0.6),
        ('min_strength', 0.3)
    )
    
    plotlines = dict(
        oi_strength=dict(color='blue', _name='OI Strength'),
        smoothed_oi=dict(color='red', _name='Smoothed OI'),
        volume_confirm=dict(color='green', _name='Volume Confirmation'),
        market_depth=dict(color='purple', _name='Market Depth'),
        trend_quality=dict(color='orange', _name='Trend Quality'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(OpenInterest, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.oi_history = []
        self.volume_history = []
        self.price_history = []
        
    def calculate_oi_strength(self):
        """
        Berechnet die Open Interest Stärke.
        """
        if len(self.data) < 2:
            return 0
            
        # Open Interest Änderung
        oi_change = (
            self.data.openinterest[0] -
            self.data.openinterest[-1]
        ) if self.data.openinterest[-1] != 0 else 0
        
        # Volumenbestätigung
        volume_confirm = 1.0
        if len(self.volume_history) >= self.p.period:
            avg_volume = np.mean(self.volume_history[-self.p.period:])
            if avg_volume > 0:
                volume_confirm = self.data.volume[0] / avg_volume
                
        # Stärke berechnen
        strength = (
            oi_change * self.p.oi_weight +
            volume_confirm * self.p.volume_weight
        )
        
        return strength
        
    def calculate_market_depth(self):
        """
        Berechnet die Markttiefe.
        """
        if len(self.oi_history) < self.p.period:
            return 0
            
        # Durchschnittliches Open Interest
        avg_oi = np.mean(self.oi_history[-self.p.period:])
        
        # Markttiefe
        if avg_oi != 0:
            depth = self.data.openinterest[0] / avg_oi - 1
        else:
            depth = 0
            
        return depth
        
    def calculate_trend_quality(self):
        """
        Berechnet die Trendqualität.
        """
        if len(self.oi_history) < self.p.period:
            return 0
            
        # Open Interest Trend
        oi_trend = np.mean([
            1 if oi > self.oi_history[i-1]
            else -1
            for i, oi in enumerate(self.oi_history[-5:])
            if i > 0
        ]) if len(self.oi_history) >= 5 else 0
        
        # Preistrend
        price_trend = np.mean([
            1 if p > self.price_history[i-1]
            else -1
            for i, p in enumerate(self.price_history[-5:])
            if i > 0
        ]) if len(self.price_history) >= 5 else 0
        
        # Trendqualität
        quality = oi_trend * price_trend
        
        return quality
        
    def next(self):
        # Open Interest Stärke berechnen
        self.lines.oi_strength[0] = self.calculate_oi_strength()
        self.oi_history.append(self.data.openinterest[0])
        
        # Geglättetes Open Interest
        self.lines.smoothed_oi[0] = bt.indicators.EMA(
            self.lines.oi_strength, period=self.p.period
        )[0]
        
        # Volumenbestätigung
        if len(self.volume_history) >= self.p.period:
            self.lines.volume_confirm[0] = (
                self.data.volume[0] /
                np.mean(self.volume_history[-self.p.period:])
            )
        else:
            self.lines.volume_confirm[0] = 1.0
            
        # Markttiefe
        self.lines.market_depth[0] = self.calculate_market_depth()
        
        # Trendqualität
        self.lines.trend_quality[0] = self.calculate_trend_quality()
        
        # Historie aktualisieren
        self.volume_history.append(self.data.volume[0])
        self.price_history.append(self.data.close[0])
        
        # Historie begrenzen
        max_period = self.p.period
        for hist in [self.oi_history, self.volume_history,
                    self.price_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_oi[0] > 0 and
            self.lines.volume_confirm[0] > 1.0 and
            self.lines.market_depth[0] > 0 and
            self.lines.trend_quality[0] > self.p.min_strength):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_oi[0] < 0 and
            self.lines.volume_confirm[0] > 1.0 and
            self.lines.market_depth[0] < 0 and
            self.lines.trend_quality[0] < -self.p.min_strength):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'open_interest': {
                'strength': self.lines.oi_strength[0],
                'smoothed': self.lines.smoothed_oi[0],
                'trend': (
                    'increasing' if self.lines.oi_strength[0] > 0
                    else 'decreasing'
                )
            },
            'volume': {
                'confirmation': self.lines.volume_confirm[0],
                'trend': (
                    'supporting' if self.lines.volume_confirm[0] > 1.0
                    else 'weakening'
                )
            },
            'market': {
                'depth': self.lines.market_depth[0],
                'quality': self.lines.trend_quality[0],
                'liquidity': (
                    'improving' if self.lines.market_depth[0] > 0
                    else 'deteriorating'
                )
            },
            'trend': {
                'quality': self.lines.trend_quality[0],
                'persistence': (
                    np.mean([
                        1 if oi > 0 else -1
                        for oi in self.oi_history[-5:]
                    ]) if len(self.oi_history) >= 5
                    else 0
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(self.lines.trend_quality[0]),
                'reliability': (
                    abs(self.lines.trend_quality[0]) *
                    self.lines.volume_confirm[0]
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'oi_volatility': (
                    np.std(self.oi_history)
                    if len(self.oi_history) > 1
                    else 0
                ),
                'depth_risk': abs(self.lines.market_depth[0])
            }
        }
