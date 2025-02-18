import backtrader as bt
import numpy as np

class NormalizedVolatilityIndex(bt.Indicator):
    """
    Normalized Volatility Index (NVI)
    
    Ein Volatilitätsindikator, der die normalisierte Volatilität
    über verschiedene Zeiträume analysiert.
    
    Features:
    - Volatilitätsnormalisierung
    - Trendstärkeberechnung
    - Marktphasenanalyse
    - Signalgenerierung
    
    Parameter:
    - short_period (10): Kurzer Analysezeitraum
    - long_period (30): Langer Analysezeitraum
    - smooth_period (5): Glättungsperiode
    """
    
    lines = ('nvi', 'smoothed_nvi',
             'market_phase', 'volatility_ratio',
             'signal')
             
    params = (
        ('short_period', 10),
        ('long_period', 30),
        ('smooth_period', 5)
    )
    
    plotlines = dict(
        nvi=dict(color='blue', _name='NVI'),
        smoothed_nvi=dict(color='red', _name='Smoothed NVI'),
        market_phase=dict(color='green', _name='Market Phase'),
        volatility_ratio=dict(color='purple', _name='Volatility Ratio'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(NormalizedVolatilityIndex, self).__init__()
        
        # Historie
        self.vol_history = []
        self.nvi_history = []
        self.phase_history = []
        
    def calculate_volatility(self):
        """
        Berechnet die Volatilität.
        """
        if len(self.data) < 2:
            return 0
            
        return abs(
            self.data.close[0] - self.data.close[-1]
        ) / self.data.close[-1]
        
    def calculate_nvi(self):
        """
        Berechnet den normalisierten Volatilitätsindex.
        """
        if len(self.vol_history) < self.p.long_period:
            return 0
            
        # Kurzfristige Volatilität
        short_vol = np.std(
            self.vol_history[-self.p.short_period:]
        )
        
        # Langfristige Volatilität
        long_vol = np.std(
            self.vol_history[-self.p.long_period:]
        )
        
        if long_vol == 0:
            return 0
            
        # Normalisierung
        return (short_vol - long_vol) / long_vol * 100
        
    def calculate_market_phase(self):
        """
        Berechnet die Marktphase.
        """
        if len(self.nvi_history) < 2:
            return 0
            
        # Volatilitätstrend
        vol_trend = (
            self.nvi_history[-1] -
            np.mean(self.nvi_history[-self.p.short_period:])
        )
        
        # Preisrichtung
        if len(self.data) >= self.p.short_period:
            price_direction = (
                self.data.close[0] -
                self.data.close[-self.p.short_period]
            )
        else:
            price_direction = 0
            
        # Phasenberechnung
        if vol_trend > 0 and price_direction > 0:
            return 1  # Bullische Expansion
        elif vol_trend > 0 and price_direction < 0:
            return -1  # Bärische Expansion
        elif vol_trend < 0 and price_direction > 0:
            return 0.5  # Bullische Kontraktion
        else:
            return -0.5  # Bärische Kontraktion
            
    def calculate_volatility_ratio(self):
        """
        Berechnet das Volatilitätsverhältnis.
        """
        if len(self.vol_history) < self.p.long_period:
            return 1.0
            
        current_vol = np.std(self.vol_history[-5:])
        historical_vol = np.std(
            self.vol_history[-self.p.long_period:]
        )
        
        return (
            current_vol / historical_vol
            if historical_vol != 0 else 1.0
        )
        
    def next(self):
        # Volatilität berechnen
        volatility = self.calculate_volatility()
        self.vol_history.append(volatility)
        
        # NVI berechnen
        self.lines.nvi[0] = self.calculate_nvi()
        self.nvi_history.append(self.lines.nvi[0])
        
        # Geglätteter NVI
        if len(self.nvi_history) >= self.p.smooth_period:
            self.lines.smoothed_nvi[0] = np.mean(
                self.nvi_history[-self.p.smooth_period:]
            )
        else:
            self.lines.smoothed_nvi[0] = self.lines.nvi[0]
            
        # Marktphase
        phase = self.calculate_market_phase()
        self.lines.market_phase[0] = phase
        self.phase_history.append(phase)
        
        # Volatilitätsverhältnis
        self.lines.volatility_ratio[0] = self.calculate_volatility_ratio()
        
        # Signal
        if (self.lines.nvi[0] < -20 and
            phase > 0):
            self.lines.signal[0] = 1  # Kaufsignal
        elif (self.lines.nvi[0] > 20 and
              phase < 0):
            self.lines.signal[0] = -1  # Verkaufssignal
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.long_period,
            self.p.short_period,
            self.p.smooth_period
        )
        for hist in [self.vol_history, self.nvi_history,
                    self.phase_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'nvi': {
                'value': self.lines.nvi[0],
                'smoothed': self.lines.smoothed_nvi[0],
                'state': (
                    'high' if self.lines.nvi[0] > 20
                    else 'low' if self.lines.nvi[0] < -20
                    else 'normal'
                ),
                'trend': (
                    'increasing'
                    if self.lines.nvi[0] >
                       self.lines.smoothed_nvi[0]
                    else 'decreasing'
                )
            },
            'market_phase': {
                'value': self.lines.market_phase[0],
                'state': (
                    'bullish expansion'
                    if self.lines.market_phase[0] == 1
                    else 'bearish expansion'
                    if self.lines.market_phase[0] == -1
                    else 'bullish contraction'
                    if self.lines.market_phase[0] == 0.5
                    else 'bearish contraction'
                ),
                'strength': abs(self.lines.market_phase[0])
            },
            'volatility': {
                'ratio': self.lines.volatility_ratio[0],
                'state': (
                    'increasing'
                    if self.lines.volatility_ratio[0] > 1
                    else 'decreasing'
                ),
                'relative_level': (
                    'high'
                    if self.lines.volatility_ratio[0] > 1.5
                    else 'low'
                    if self.lines.volatility_ratio[0] < 0.5
                    else 'normal'
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
                    abs(self.lines.market_phase[0]) *
                    (1 - abs(self.lines.nvi[0]) / 100)
                    if abs(self.lines.nvi[0]) <= 100
                    else 0
                )
            },
            'risk': {
                'nvi_risk': (
                    abs(self.lines.nvi[0]) / 100
                    if abs(self.lines.nvi[0]) <= 100
                    else 1
                ),
                'phase_risk': (
                    1 - abs(self.lines.market_phase[0])
                    if abs(self.lines.market_phase[0]) <= 1
                    else 0
                ),
                'volatility_risk': (
                    self.lines.volatility_ratio[0]
                    if self.lines.volatility_ratio[0] > 1
                    else 1 / self.lines.volatility_ratio[0]
                    if self.lines.volatility_ratio[0] > 0
                    else 1
                )
            }
        }
