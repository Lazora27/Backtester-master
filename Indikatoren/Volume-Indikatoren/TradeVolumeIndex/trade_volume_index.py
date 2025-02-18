import backtrader as bt
import numpy as np

class TradeVolumeIndex(bt.Indicator):
    """
    Trade Volume Index (TVI)
    
    Ein fortgeschrittener Indikator, der Handelsvolumen basierend
    auf der Preisdynamik akkumuliert.
    
    Features:
    - Volumenakkumulation
    - Preisdynamikanalyse
    - Trendbestätigung
    - Divergenzanalyse
    - Signalgenerierung
    
    Parameter:
    - min_tick (0.01): Minimale Preisänderung
    - period (20): Analysezeitraum
    - volume_factor (1.0): Volumenfaktor
    """
    
    lines = ('tvi', 'smoothed_tvi',
             'volume_force', 'trend_quality',
             'divergence', 'buy_signal',
             'sell_signal')
             
    params = (
        ('min_tick', 0.01),
        ('period', 20),
        ('volume_factor', 1.0),
        ('min_strength', 0.3)
    )
    
    plotlines = dict(
        tvi=dict(color='blue', _name='TVI'),
        smoothed_tvi=dict(color='red', _name='Smoothed TVI'),
        volume_force=dict(color='green', _name='Volume Force'),
        trend_quality=dict(color='purple', _name='Trend Quality'),
        divergence=dict(color='orange', _name='Divergence'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(TradeVolumeIndex, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.tvi_history = []
        self.price_history = []
        self.volume_history = []
        
    def calculate_tvi(self):
        """
        Berechnet den Trade Volume Index.
        """
        if len(self.data) < 2:
            return 0
            
        # Preisänderung
        price_change = self.data.close[0] - self.data.close[-1]
        
        # Minimale Preisänderung prüfen
        if abs(price_change) < self.p.min_tick:
            return 0
            
        # Volumengewichtung
        volume = (
            self.data.volume[0] ** self.p.volume_factor
        )
        
        # TVI berechnen
        tvi = volume if price_change > 0 else -volume
        
        # Kumulativer TVI
        if len(self.tvi_history) > 0:
            tvi += self.tvi_history[-1]
            
        return tvi
        
    def calculate_volume_force(self):
        """
        Berechnet die Volumenkraft.
        """
        if len(self.volume_history) < self.p.period:
            return 0
            
        # Durchschnittliches Volumen
        avg_volume = np.mean(self.volume_history[-self.p.period:])
        
        # Volumenkraft
        if avg_volume > 0:
            force = (
                self.data.volume[0] / avg_volume - 1
            )
        else:
            force = 0
            
        return force
        
    def calculate_trend_quality(self):
        """
        Berechnet die Trendqualität.
        """
        if len(self.tvi_history) < self.p.period:
            return 0
            
        # Trendrichtung
        trend_direction = np.mean([
            1 if tvi > self.tvi_history[i-1]
            else -1
            for i, tvi in enumerate(self.tvi_history[-5:])
            if i > 0
        ]) if len(self.tvi_history) >= 5 else 0
        
        # Trendstärke
        trend_strength = abs(
            np.mean(self.tvi_history[-self.p.period:])
        )
        
        return trend_direction * trend_strength
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und TVI.
        """
        if len(self.tvi_history) < self.p.period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.period:])
        price_low = min(self.price_history[-self.p.period:])
        
        # TVI-Hochs/-Tiefs
        tvi_high = max(self.tvi_history[-self.p.period:])
        tvi_low = min(self.tvi_history[-self.p.period:])
        
        # Bullische Divergenz
        if price_low < price_high and tvi_low > tvi_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and tvi_low < tvi_high:
            return -1
            
        return 0
        
    def next(self):
        # TVI berechnen
        self.lines.tvi[0] = self.calculate_tvi()
        self.tvi_history.append(self.lines.tvi[0])
        
        # Geglätteter TVI
        self.lines.smoothed_tvi[0] = bt.indicators.EMA(
            self.lines.tvi, period=self.p.period
        )[0]
        
        # Volumenkraft
        self.lines.volume_force[0] = self.calculate_volume_force()
        
        # Trendqualität
        self.lines.trend_quality[0] = self.calculate_trend_quality()
        
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Historie aktualisieren
        self.price_history.append(self.data.close[0])
        self.volume_history.append(self.data.volume[0])
        
        # Historie begrenzen
        max_period = self.p.period
        for hist in [self.tvi_history, self.price_history,
                    self.volume_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_tvi[0] > 0 and
            self.lines.volume_force[0] > 0 and
            self.lines.trend_quality[0] > self.p.min_strength and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_tvi[0] < 0 and
            self.lines.volume_force[0] < 0 and
            self.lines.trend_quality[0] < -self.p.min_strength and
            self.lines.divergence[0] <= 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'tvi': {
                'current': self.lines.tvi[0],
                'smoothed': self.lines.smoothed_tvi[0],
                'trend': (
                    'bullish' if self.lines.tvi[0] > 0
                    else 'bearish'
                )
            },
            'volume': {
                'force': self.lines.volume_force[0],
                'trend': (
                    'increasing' if self.lines.volume_force[0] > 0
                    else 'decreasing'
                ),
                'quality': (
                    'strong' if abs(self.lines.volume_force[0]) > 0.5
                    else 'weak'
                )
            },
            'trend': {
                'quality': self.lines.trend_quality[0],
                'strength': abs(self.lines.trend_quality[0]),
                'persistence': (
                    np.mean([
                        1 if tvi > 0 else -1
                        for tvi in self.tvi_history[-5:]
                    ]) if len(self.tvi_history) >= 5
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
                'strength': abs(self.lines.trend_quality[0]),
                'reliability': (
                    abs(self.lines.trend_quality[0]) *
                    abs(self.lines.volume_force[0])
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'tvi_volatility': (
                    np.std(self.tvi_history)
                    if len(self.tvi_history) > 1
                    else 0
                ),
                'volume_risk': abs(self.lines.volume_force[0])
            }
        }
