import backtrader as bt
import numpy as np

class LiquidityIndex(bt.Indicator):
    """
    Liquidity Index
    
    Ein Indikator, der die Marktliquidität durch Analyse
    von Volumen, Spread und Handelsdynamik misst.
    
    Features:
    - Liquiditätsanalyse
    - Spreadanalyse
    - Handelseffizienz
    - Markttiefenanalyse
    - Signal-Validierung
    
    Parameter:
    - period (20): Basisperiode
    - volume_factor (1.0): Volumenfaktor
    - spread_weight (0.5): Spread-Gewichtung
    """
    
    lines = ('liquidity', 'smoothed_liquidity',
             'spread_efficiency', 'market_depth',
             'trading_activity', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 20),
        ('volume_factor', 1.0),
        ('spread_weight', 0.5),
        ('min_liquidity', 0.3)
    )
    
    plotlines = dict(
        liquidity=dict(color='blue', _name='Liquidity'),
        smoothed_liquidity=dict(color='red', _name='Smoothed Liquidity'),
        spread_efficiency=dict(color='purple', _name='Spread Efficiency'),
        market_depth=dict(color='orange', _name='Market Depth'),
        trading_activity=dict(color='green', _name='Trading Activity'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(LiquidityIndex, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.liquidity_history = []
        self.volume_history = []
        self.spread_history = []
        
    def calculate_liquidity(self):
        """
        Berechnet den Liquiditätsindex.
        """
        if len(self.data) < 2:
            return 0
            
        # Spread berechnen
        spread = self.data.high[0] - self.data.low[0]
        if spread == 0:
            return 0
            
        # Volumengewichtung
        volume_weight = 1.0
        if len(self.volume_history) >= self.p.period:
            avg_volume = np.mean(self.volume_history[-self.p.period:])
            if avg_volume > 0:
                volume_weight = (
                    self.data.volume[0] / avg_volume
                ) ** self.p.volume_factor
                
        # Spread-Effizienz
        spread_efficiency = 1.0 - (spread / self.data.close[0])
        
        # Liquidität berechnen
        liquidity = (
            volume_weight * (1 - self.p.spread_weight) +
            spread_efficiency * self.p.spread_weight
        )
        
        return liquidity
        
    def calculate_market_depth(self):
        """
        Berechnet die Markttiefe.
        """
        if len(self.volume_history) < self.p.period:
            return 0
            
        # Durchschnittliches Volumen
        avg_volume = np.mean(self.volume_history[-self.p.period:])
        
        # Volumentrend
        volume_trend = (
            self.data.volume[0] - avg_volume
        ) / avg_volume if avg_volume > 0 else 0
        
        return volume_trend
        
    def calculate_trading_activity(self):
        """
        Berechnet die Handelsaktivität.
        """
        if len(self.data) < self.p.period:
            return 0
            
        # Preisvolatilität
        price_volatility = self.vol[0]
        
        # Volumenvolatilität
        if len(self.volume_history) >= self.p.period:
            volume_volatility = np.std(
                self.volume_history[-self.p.period:]
            )
        else:
            volume_volatility = 0
            
        # Aktivitätsindex
        if price_volatility > 0 and volume_volatility > 0:
            activity = (
                (self.data.volume[0] * price_volatility) /
                (volume_volatility * self.data.close[0])
            )
        else:
            activity = 0
            
        return activity
        
    def next(self):
        # Liquidität berechnen
        self.lines.liquidity[0] = self.calculate_liquidity()
        self.liquidity_history.append(self.lines.liquidity[0])
        
        # Geglättete Liquidität
        self.lines.smoothed_liquidity[0] = bt.indicators.EMA(
            self.lines.liquidity, period=self.p.period
        )[0]
        
        # Spread-Effizienz
        spread = self.data.high[0] - self.data.low[0]
        if self.data.close[0] != 0:
            self.lines.spread_efficiency[0] = 1.0 - (
                spread / self.data.close[0]
            )
        else:
            self.lines.spread_efficiency[0] = 0
            
        # Historie aktualisieren
        self.volume_history.append(self.data.volume[0])
        self.spread_history.append(spread)
        
        # Markttiefe
        self.lines.market_depth[0] = self.calculate_market_depth()
        
        # Handelsaktivität
        self.lines.trading_activity[0] = self.calculate_trading_activity()
        
        # Historie begrenzen
        max_period = self.p.period
        for hist in [self.liquidity_history, self.volume_history,
                    self.spread_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_liquidity[0] > self.p.min_liquidity and
            self.lines.market_depth[0] > 0 and
            self.lines.trading_activity[0] > 1.0 and
            self.lines.spread_efficiency[0] > 0.5):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_liquidity[0] < self.p.min_liquidity and
            self.lines.market_depth[0] < 0 and
            self.lines.trading_activity[0] < 1.0 and
            self.lines.spread_efficiency[0] < 0.5):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'liquidity': {
                'current': self.lines.liquidity[0],
                'smoothed': self.lines.smoothed_liquidity[0],
                'trend': (
                    'improving' if self.lines.liquidity[0] > self.lines.liquidity[-1]
                    else 'deteriorating'
                )
            },
            'spread': {
                'efficiency': self.lines.spread_efficiency[0],
                'trend': (
                    'tightening' if self.lines.spread_efficiency[0] > 0.5
                    else 'widening'
                ),
                'stability': (
                    np.std(self.spread_history)
                    if len(self.spread_history) > 1
                    else 0
                )
            },
            'market': {
                'depth': self.lines.market_depth[0],
                'activity': self.lines.trading_activity[0],
                'quality': (
                    self.lines.liquidity[0] *
                    self.lines.spread_efficiency[0]
                )
            },
            'volume': {
                'trend': (
                    'increasing' if self.lines.market_depth[0] > 0
                    else 'decreasing'
                ),
                'consistency': (
                    np.mean([
                        1 if v > np.mean(self.volume_history)
                        else -1
                        for v in self.volume_history[-5:]
                    ]) if len(self.volume_history) >= 5
                    else 0
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.liquidity[0],
                'reliability': (
                    self.lines.liquidity[0] *
                    self.lines.spread_efficiency[0] *
                    self.lines.trading_activity[0]
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'liquidity_risk': 1 - self.lines.liquidity[0],
                'spread_risk': 1 - self.lines.spread_efficiency[0]
            }
        }
