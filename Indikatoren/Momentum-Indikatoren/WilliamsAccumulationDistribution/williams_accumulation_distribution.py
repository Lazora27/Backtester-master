import backtrader as bt
import numpy as np

class WilliamsAccumulationDistribution(bt.Indicator):
    """
    Williams Accumulation/Distribution (WAD)
    
    Ein Indikator, der Akkumulation und Distribution basierend
    auf der Preisbewegung und dem Schlusskurs misst.
    
    Features:
    - Akkumulations-/Distributionsanalyse
    - Trendbestätigung
    - Divergenz-Erkennung
    - Volumenanalyse
    - Signal-Validierung
    
    Parameter:
    - period (14): Basisperiode
    - smooth_period (3): Glättungsperiode
    - divergence_period (20): Divergenzperiode
    """
    
    lines = ('wad', 'smoothed_wad',
             'trend_strength', 'divergence',
             'volume_flow', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 14),
        ('smooth_period', 3),
        ('divergence_period', 20),
        ('volume_threshold', 1.5)
    )
    
    plotlines = dict(
        wad=dict(color='blue', _name='WAD'),
        smoothed_wad=dict(color='red', _name='Smoothed WAD'),
        trend_strength=dict(color='purple', _name='Trend Strength'),
        divergence=dict(color='orange', _name='Divergence'),
        volume_flow=dict(color='green', _name='Volume Flow'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(WilliamsAccumulationDistribution, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Historie
        self.wad_history = []
        self.price_history = []
        self.volume_history = []
        
    def calculate_wad(self):
        """
        Berechnet den WAD-Wert.
        """
        if len(self.price_history) < 2:
            return 0
            
        close = self.data.close[0]
        prev_close = self.data.close[-1]
        
        # True High/Low
        true_high = max(self.data.high[0], prev_close)
        true_low = min(self.data.low[0], prev_close)
        
        # WAD Berechnung
        if close > prev_close:
            # Akkumulation
            wad = close - true_low
        else:
            # Distribution
            wad = close - true_high
            
        # Kumulativer WAD
        if len(self.wad_history) > 0:
            wad += self.wad_history[-1]
            
        return wad
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.wad_history) < 2:
            return 0
            
        # WAD-Momentum
        momentum = self.wad_history[-1] - self.wad_history[-2]
        
        # Relative Stärke
        strength = abs(momentum)
        if self.data[0] != 0:
            strength = strength / self.data[0]
            
        return min(1.0, strength)
        
    def calculate_volume_flow(self):
        """
        Berechnet den Volumenfluss.
        """
        if len(self.volume_history) < self.p.period:
            return 0
            
        # Durchschnittliches Volumen
        avg_volume = np.mean(self.volume_history[-self.p.period:])
        if avg_volume == 0:
            return 0
            
        # Aktuelles relatives Volumen
        current_volume = self.data.volume[0]
        return current_volume / avg_volume
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und WAD.
        """
        if len(self.price_history) < self.p.divergence_period or len(self.wad_history) < self.p.divergence_period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.divergence_period:])
        price_low = min(self.price_history[-self.p.divergence_period:])
        
        # WAD-Hochs/-Tiefs
        wad_high = max(self.wad_history[-self.p.divergence_period:])
        wad_low = min(self.wad_history[-self.p.divergence_period:])
        
        # Bullische Divergenz
        if price_low < price_high and wad_low > wad_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and wad_low < wad_high:
            return -1
            
        return 0
        
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.data[0])
        self.volume_history.append(self.data.volume[0])
        
        # WAD berechnen
        self.lines.wad[0] = self.calculate_wad()
        self.wad_history.append(self.lines.wad[0])
        
        # Geglätteter WAD
        self.lines.smoothed_wad[0] = bt.indicators.EMA(
            self.lines.wad, period=self.p.smooth_period
        )[0]
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Volumenfluss
        self.lines.volume_flow[0] = self.calculate_volume_flow()
        
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.divergence_period
        )
        for hist in [self.wad_history, self.price_history, self.volume_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_wad[0] > self.lines.smoothed_wad[-1] and
            self.lines.volume_flow[0] > self.p.volume_threshold and
            self.lines.trend_strength[0] > 0.3 and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_wad[0] < self.lines.smoothed_wad[-1] and
            self.lines.volume_flow[0] > self.p.volume_threshold and
            self.lines.trend_strength[0] > 0.3 and
            self.lines.divergence[0] <= 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'accumulation': {
                'wad': self.lines.wad[0],
                'smoothed': self.lines.smoothed_wad[0],
                'trend_strength': self.lines.trend_strength[0],
                'volume_flow': self.lines.volume_flow[0]
            },
            'trend': {
                'direction': np.sign(
                    self.lines.smoothed_wad[0] -
                    self.lines.smoothed_wad[-1]
                ),
                'strength': self.lines.trend_strength[0],
                'momentum': (
                    self.lines.wad[0] - self.wad_history[-2]
                    if len(self.wad_history) > 1
                    else 0
                )
            },
            'volume': {
                'flow': self.lines.volume_flow[0],
                'trend': (
                    'increasing' if self.lines.volume_flow[0] > 1
                    else 'decreasing'
                ),
                'strength': abs(self.lines.volume_flow[0] - 1)
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
                    self.lines.volume_flow[0] *
                    (1 + abs(self.lines.divergence[0]))
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'wad_stability': (
                    np.std(self.wad_history)
                    if len(self.wad_history) > 1
                    else 0
                ),
                'volume_stability': (
                    np.std(self.volume_history)
                    if len(self.volume_history) > 1
                    else 0
                )
            }
        }
