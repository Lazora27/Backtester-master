import backtrader as bt
import numpy as np

class VolumeTrendIndicator(bt.Indicator):
    """
    Volume Trend Indicator
    
    Ein fortgeschrittener Indikator, der Volumentrends und
    deren Beziehung zur Preisbewegung analysiert.
    
    Features:
    - Volumentrendanalyse
    - Trendstärkeberechnung
    - Preiskorrelation
    - Trendbestätigung
    - Signalgenerierung
    
    Parameter:
    - period (20): Analysezeitraum
    - trend_threshold (0.3): Trendschwelle
    - correlation_period (10): Korrelationsperiode
    """
    
    lines = ('vti', 'smoothed_vti',
             'trend_strength', 'price_correlation',
             'trend_quality', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 20),
        ('trend_threshold', 0.3),
        ('correlation_period', 10),
        ('min_strength', 0.3)
    )
    
    plotlines = dict(
        vti=dict(color='blue', _name='VTI'),
        smoothed_vti=dict(color='red', _name='Smoothed VTI'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        price_correlation=dict(color='purple', _name='Price Correlation'),
        trend_quality=dict(color='orange', _name='Trend Quality'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(VolumeTrendIndicator, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.vti_history = []
        self.price_history = []
        self.volume_history = []
        
    def calculate_vti(self):
        """
        Berechnet den Volume Trend Indicator.
        """
        if len(self.data) < 2:
            return 0
            
        # Volumenänderung
        volume_change = (
            self.data.volume[0] - self.data.volume[-1]
        ) / self.data.volume[-1] if self.data.volume[-1] != 0 else 0
        
        # Preisänderung
        price_change = (
            self.data.close[0] - self.data.close[-1]
        ) / self.data.close[-1] if self.data.close[-1] != 0 else 0
        
        # VTI berechnen
        vti = volume_change * np.sign(price_change)
        
        return vti
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.vti_history) < self.p.period:
            return 0
            
        # Durchschnittlicher VTI
        avg_vti = np.mean(self.vti_history[-self.p.period:])
        
        # Trendstärke
        strength = abs(avg_vti)
        
        return strength
        
    def calculate_price_correlation(self):
        """
        Berechnet die Preiskorrelation.
        """
        if len(self.price_history) < self.p.correlation_period:
            return 0
            
        # Preisänderungen
        price_changes = [
            (p - self.price_history[i-1]) / self.price_history[i-1]
            if self.price_history[i-1] != 0 else 0
            for i, p in enumerate(self.price_history[-self.p.correlation_period:])
            if i > 0
        ]
        
        # Volumenänderungen
        volume_changes = [
            (v - self.volume_history[i-1]) / self.volume_history[i-1]
            if self.volume_history[i-1] != 0 else 0
            for i, v in enumerate(self.volume_history[-self.p.correlation_period:])
            if i > 0
        ]
        
        # Korrelation berechnen
        if len(price_changes) > 1 and len(volume_changes) > 1:
            correlation = np.corrcoef(price_changes, volume_changes)[0, 1]
        else:
            correlation = 0
            
        return correlation
        
    def calculate_trend_quality(self):
        """
        Berechnet die Trendqualität.
        """
        if len(self.vti_history) < self.p.period:
            return 0
            
        # Trendrichtung
        trend_direction = np.mean([
            1 if vti > self.vti_history[i-1]
            else -1
            for i, vti in enumerate(self.vti_history[-5:])
            if i > 0
        ]) if len(self.vti_history) >= 5 else 0
        
        # Trendstärke
        trend_strength = self.lines.trend_strength[0]
        
        # Trendqualität
        quality = trend_direction * trend_strength
        
        return quality
        
    def next(self):
        # VTI berechnen
        self.lines.vti[0] = self.calculate_vti()
        self.vti_history.append(self.lines.vti[0])
        
        # Geglätteter VTI
        self.lines.smoothed_vti[0] = bt.indicators.EMA(
            self.lines.vti, period=self.p.period
        )[0]
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Preiskorrelation
        self.lines.price_correlation[0] = self.calculate_price_correlation()
        
        # Trendqualität
        self.lines.trend_quality[0] = self.calculate_trend_quality()
        
        # Historie aktualisieren
        self.price_history.append(self.data.close[0])
        self.volume_history.append(self.data.volume[0])
        
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.correlation_period
        )
        for hist in [self.vti_history, self.price_history,
                    self.volume_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_vti[0] > self.p.trend_threshold and
            self.lines.trend_strength[0] > self.p.min_strength and
            self.lines.price_correlation[0] > 0 and
            self.lines.trend_quality[0] > 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_vti[0] < -self.p.trend_threshold and
            self.lines.trend_strength[0] > self.p.min_strength and
            self.lines.price_correlation[0] > 0 and
            self.lines.trend_quality[0] < 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'trend': {
                'vti': self.lines.vti[0],
                'smoothed': self.lines.smoothed_vti[0],
                'strength': self.lines.trend_strength[0],
                'direction': (
                    'up' if self.lines.vti[0] > 0
                    else 'down'
                )
            },
            'correlation': {
                'price': self.lines.price_correlation[0],
                'strength': abs(self.lines.price_correlation[0]),
                'quality': (
                    'strong' if abs(self.lines.price_correlation[0]) > 0.7
                    else 'moderate' if abs(self.lines.price_correlation[0]) > 0.3
                    else 'weak'
                )
            },
            'quality': {
                'trend': self.lines.trend_quality[0],
                'strength': abs(self.lines.trend_quality[0]),
                'persistence': (
                    np.mean([
                        1 if vti > 0 else -1
                        for vti in self.vti_history[-5:]
                    ]) if len(self.vti_history) >= 5
                    else 0
                )
            },
            'volume': {
                'trend': (
                    'increasing' if self.data.volume[0] > np.mean(self.volume_history)
                    else 'decreasing'
                    if len(self.volume_history) > 0
                    else 'neutral'
                ),
                'strength': (
                    self.data.volume[0] / np.mean(self.volume_history)
                    if len(self.volume_history) > 0 and np.mean(self.volume_history) > 0
                    else 1.0
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    self.lines.trend_strength[0] *
                    abs(self.lines.price_correlation[0])
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'trend_volatility': (
                    np.std(self.vti_history)
                    if len(self.vti_history) > 1
                    else 0
                ),
                'correlation_risk': 1 - abs(self.lines.price_correlation[0])
            }
        }
