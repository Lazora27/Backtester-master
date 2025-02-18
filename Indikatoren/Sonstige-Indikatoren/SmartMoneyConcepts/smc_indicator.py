import backtrader as bt
import numpy as np
from enum import Enum

class OrderBlockType(Enum):
    """Order Block Typen"""
    BULLISH = "Bullish"
    BEARISH = "Bearish"
    NEUTRAL = "Neutral"

class LiquidityType(Enum):
    """Liquiditäts-Typen"""
    PREMIUM = "Premium"
    DISCOUNT = "Discount"
    EQUILIBRIUM = "Equilibrium"

class SmartMoneyConceptsIndicator(bt.Indicator):
    """
    Smart Money Concepts (SMC) Indicator
    
    Ein fortgeschrittener Indikator zur Analyse von
    institutionellen Handelsbewegungen.
    
    Features:
    - Order Block Erkennung
    - Liquiditätsanalyse
    - Fair Value Gaps
    - Ineffiziente Preisbereiche
    - Imbalance-Zonen
    
    Parameter:
    - ob_lookback (20): Order Block Rückblick
    - min_ob_size (0.3): Min. Order Block Größe
    - liquidity_threshold (0.5): Liquiditätsschwelle
    """
    
    lines = ('ob_signal', 'liquidity', 'imbalance')
    params = (
        ('ob_lookback', 20),
        ('min_ob_size', 0.3),
        ('liquidity_threshold', 0.5),
    )
    
    plotlines = dict(
        ob_signal=dict(color='blue', _name='OB Signal'),
        liquidity=dict(color='green', _name='Liquidity'),
        imbalance=dict(color='red', _name='Imbalance')
    )
    
    def __init__(self):
        super(SmartMoneyConceptsIndicator, self).__init__()
        
        # Order Block Tracking
        self.order_blocks = []
        
        # Liquiditätszonen
        self.liquidity_zones = []
        
        # Fair Value Gaps
        self.fvg_zones = []
        
        # Preispuffer
        self.price_history = []
        self.volume_history = []
        
    def identify_order_block(self, candles):
        """Identifiziert Order Blocks"""
        if len(candles) < 3:
            return None
            
        # Letzte 3 Kerzen analysieren
        c1, c2, c3 = candles[-3:]
        
        # Bullish Order Block
        if (c1['close'] < c1['open'] and  # Bearish
            c2['close'] > c2['open'] and  # Bullish
            c3['close'] > c3['open'] and  # Bullish
            c3['close'] > c2['close']):   # Höheres Hoch
            
            return {
                'type': OrderBlockType.BULLISH,
                'level': c1['low'],
                'size': abs(c1['high'] - c1['low']),
                'volume': c1['volume']
            }
            
        # Bearish Order Block
        elif (c1['close'] > c1['open'] and  # Bullish
              c2['close'] < c2['open'] and  # Bearish
              c3['close'] < c3['open'] and  # Bearish
              c3['close'] < c2['close']):   # Tieferes Tief
              
            return {
                'type': OrderBlockType.BEARISH,
                'level': c1['high'],
                'size': abs(c1['high'] - c1['low']),
                'volume': c1['volume']
            }
            
        return None
        
    def analyze_liquidity(self, price, volume):
        """Analysiert Liquiditätszonen"""
        if not self.price_history:
            return 0
            
        # Volumengewichteter Durchschnittspreis
        vwap = np.average(
            self.price_history,
            weights=self.volume_history
        )
        
        # Liquiditätsberechnung
        if price > vwap:
            # Premium Zone
            liquidity = (price - vwap) / vwap
            return min(1, liquidity)
        else:
            # Discount Zone
            liquidity = (vwap - price) / vwap
            return max(-1, -liquidity)
            
    def find_fair_value_gaps(self, candles):
        """Findet Fair Value Gaps"""
        if len(candles) < 3:
            return None
            
        # Letzte 3 Kerzen
        c1, c2, c3 = candles[-3:]
        
        # Bullish FVG
        if c1['high'] < c3['low']:
            return {
                'type': 'bullish',
                'level': (c1['high'] + c3['low']) / 2,
                'size': c3['low'] - c1['high']
            }
            
        # Bearish FVG
        elif c1['low'] > c3['high']:
            return {
                'type': 'bearish',
                'level': (c1['low'] + c3['high']) / 2,
                'size': c1['low'] - c3['high']
            }
            
        return None
        
    def calculate_imbalance(self, candles):
        """Berechnet Marktungleichgewicht"""
        if len(candles) < 2:
            return 0
            
        # Letzte 2 Kerzen
        c1, c2 = candles[-2:]
        
        # Delta-Volumen
        delta = (
            c2['volume'] * (1 if c2['close'] > c2['open'] else -1)
        )
        
        # Normalisierung
        if c2['volume'] > 0:
            return delta / c2['volume']
        return 0
        
    def next(self):
        # Kerzen-Daten sammeln
        candle = {
            'open': self.data.open[0],
            'high': self.data.high[0],
            'low': self.data.low[0],
            'close': self.data.close[0],
            'volume': self.data.volume[0]
        }
        
        # Historie aktualisieren
        self.price_history.append(self.data.close[0])
        self.volume_history.append(self.data.volume[0])
        
        if len(self.price_history) > self.p.ob_lookback:
            self.price_history.pop(0)
            self.volume_history.pop(0)
            
        # Letzte Kerzen für Analyse
        candles = [
            {
                'open': self.data.open[-i],
                'high': self.data.high[-i],
                'low': self.data.low[-i],
                'close': self.data.close[-i],
                'volume': self.data.volume[-i]
            }
            for i in range(3)
            if len(self.data) > i
        ]
        
        # Order Block Analysis
        ob = self.identify_order_block(candles)
        if ob and ob['size'] > self.p.min_ob_size:
            self.order_blocks.append(ob)
            
        # Maximal 10 Order Blocks speichern
        if len(self.order_blocks) > 10:
            self.order_blocks.pop(0)
            
        # Liquiditätsanalyse
        liquidity = self.analyze_liquidity(
            self.data.close[0],
            self.data.volume[0]
        )
        
        # Fair Value Gaps
        fvg = self.find_fair_value_gaps(candles)
        if fvg:
            self.fvg_zones.append(fvg)
            
        # Maximal 5 FVGs speichern
        if len(self.fvg_zones) > 5:
            self.fvg_zones.pop(0)
            
        # Imbalance berechnen
        imbalance = self.calculate_imbalance(candles)
        
        # Linien aktualisieren
        self.lines.ob_signal[0] = (
            1 if ob and ob['type'] == OrderBlockType.BULLISH
            else -1 if ob and ob['type'] == OrderBlockType.BEARISH
            else 0
        )
        self.lines.liquidity[0] = liquidity
        self.lines.imbalance[0] = imbalance
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        current_price = self.data.close[0]
        
        # Aktive Order Blocks analysieren
        active_obs = [
            ob for ob in self.order_blocks
            if abs(ob['level'] - current_price) <
            current_price * self.p.min_ob_size
        ]
        
        # Liquiditätsstatus
        liquidity_status = (
            LiquidityType.PREMIUM
            if self.lines.liquidity[0] > self.p.liquidity_threshold
            else LiquidityType.DISCOUNT
            if self.lines.liquidity[0] < -self.p.liquidity_threshold
            else LiquidityType.EQUILIBRIUM
        )
        
        return {
            'order_blocks': {
                'active': len(active_obs),
                'types': {
                    'bullish': len([
                        ob for ob in active_obs
                        if ob['type'] == OrderBlockType.BULLISH
                    ]),
                    'bearish': len([
                        ob for ob in active_obs
                        if ob['type'] == OrderBlockType.BEARISH
                    ])
                },
                'nearest': (
                    min(active_obs,
                        key=lambda x: abs(x['level'] - current_price))
                    if active_obs else None
                )
            },
            'liquidity_analysis': {
                'status': liquidity_status.value,
                'level': self.lines.liquidity[0],
                'threshold_breach': (
                    abs(self.lines.liquidity[0]) >
                    self.p.liquidity_threshold
                )
            },
            'fair_value_gaps': {
                'active': len(self.fvg_zones),
                'nearest': (
                    min(self.fvg_zones,
                        key=lambda x: abs(x['level'] - current_price))
                    if self.fvg_zones else None
                )
            },
            'market_structure': {
                'imbalance': self.lines.imbalance[0],
                'bias': (
                    'bullish'
                    if self.lines.imbalance[0] > 0.3
                    else 'bearish'
                    if self.lines.imbalance[0] < -0.3
                    else 'neutral'
                ),
                'efficiency': (
                    1 - abs(self.lines.imbalance[0])
                )
            },
            'trading_opportunities': {
                'setup_quality': (
                    'excellent'
                    if (len(active_obs) > 0 and
                        abs(self.lines.liquidity[0]) >
                        self.p.liquidity_threshold and
                        abs(self.lines.imbalance[0]) > 0.5)
                    else 'good'
                    if (len(active_obs) > 0 and
                        abs(self.lines.liquidity[0]) >
                        self.p.liquidity_threshold)
                    else 'moderate'
                    if len(active_obs) > 0
                    else 'poor'
                ),
                'entry_zones': [
                    {
                        'level': ob['level'],
                        'type': ob['type'].value,
                        'strength': (
                            ob['volume'] /
                            np.mean(self.volume_history)
                        )
                    }
                    for ob in active_obs
                ]
            }
        }
