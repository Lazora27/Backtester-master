import backtrader as bt
import numpy as np

class PriceVolumeTrend(bt.Indicator):
    """
    Price Volume Trend (PVT)
    
    Ein Indikator, der die Beziehung zwischen Preis und
    Volumen analysiert, um Trendstärke zu messen.
    
    Features:
    - Preis-Volumen-Analyse
    - Trendbestätigung
    - Divergenzanalyse
    - Momentumberechnung
    - Signal-Validierung
    
    Parameter:
    - period (20): Basisperiode
    - volume_factor (1.0): Volumenfaktor
    - momentum_period (10): Momentumperiode
    """
    
    lines = ('pvt', 'smoothed_pvt',
             'momentum', 'trend_strength',
             'divergence', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 20),
        ('volume_factor', 1.0),
        ('momentum_period', 10),
        ('min_strength', 0.3)
    )
    
    plotlines = dict(
        pvt=dict(color='blue', _name='PVT'),
        smoothed_pvt=dict(color='red', _name='Smoothed PVT'),
        momentum=dict(color='green', _name='Momentum'),
        trend_strength=dict(color='purple', _name='Trend Strength'),
        divergence=dict(color='orange', _name='Divergence'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(PriceVolumeTrend, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.pvt_history = []
        self.price_history = []
        self.volume_history = []
        
    def calculate_pvt(self):
        """
        Berechnet den Price Volume Trend.
        """
        if len(self.data) < 2:
            return 0
            
        # Preisänderung
        price_change = (
            self.data.close[0] - self.data.close[-1]
        ) / self.data.close[-1] if self.data.close[-1] != 0 else 0
        
        # Volumengewichtung
        volume_weight = (
            self.data.volume[0] ** self.p.volume_factor
        )
        
        # PVT berechnen
        pvt = price_change * volume_weight
        
        # Kumulativer PVT
        if len(self.pvt_history) > 0:
            pvt += self.pvt_history[-1]
            
        return pvt
        
    def calculate_momentum(self):
        """
        Berechnet das Momentum.
        """
        if len(self.pvt_history) < self.p.momentum_period:
            return 0
            
        # Momentum über Periode
        momentum = (
            self.pvt_history[-1] -
            self.pvt_history[-self.p.momentum_period]
        )
        
        return momentum
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und PVT.
        """
        if len(self.pvt_history) < self.p.period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.period:])
        price_low = min(self.price_history[-self.p.period:])
        
        # PVT-Hochs/-Tiefs
        pvt_high = max(self.pvt_history[-self.p.period:])
        pvt_low = min(self.pvt_history[-self.p.period:])
        
        # Bullische Divergenz
        if price_low < price_high and pvt_low > pvt_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and pvt_low < pvt_high:
            return -1
            
        return 0
        
    def next(self):
        # PVT berechnen
        self.lines.pvt[0] = self.calculate_pvt()
        self.pvt_history.append(self.lines.pvt[0])
        
        # Geglätteter PVT
        self.lines.smoothed_pvt[0] = bt.indicators.EMA(
            self.lines.pvt, period=self.p.period
        )[0]
        
        # Momentum
        self.lines.momentum[0] = self.calculate_momentum()
        
        # Trendstärke
        if len(self.pvt_history) >= self.p.period:
            self.lines.trend_strength[0] = abs(
                np.mean(self.pvt_history[-self.p.period:])
            )
        else:
            self.lines.trend_strength[0] = 0
            
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Historie aktualisieren
        self.price_history.append(self.data.close[0])
        self.volume_history.append(self.data.volume[0])
        
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.momentum_period
        )
        for hist in [self.pvt_history, self.price_history,
                    self.volume_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_pvt[0] > 0 and
            self.lines.momentum[0] > 0 and
            self.lines.trend_strength[0] > self.p.min_strength and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_pvt[0] < 0 and
            self.lines.momentum[0] < 0 and
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
            'pvt': {
                'current': self.lines.pvt[0],
                'smoothed': self.lines.smoothed_pvt[0],
                'momentum': self.lines.momentum[0],
                'trend': (
                    'bullish' if self.lines.pvt[0] > 0
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
                'momentum': (
                    'accelerating' if self.lines.momentum[0] > 0
                    else 'decelerating'
                ),
                'persistence': (
                    np.mean([
                        1 if pvt > 0 else -1
                        for pvt in self.pvt_history[-5:]
                    ]) if len(self.pvt_history) >= 5
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
                    abs(self.lines.momentum[0])
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'pvt_volatility': (
                    np.std(self.pvt_history)
                    if len(self.pvt_history) > 1
                    else 0
                ),
                'momentum_risk': abs(self.lines.momentum[0])
            }
        }
