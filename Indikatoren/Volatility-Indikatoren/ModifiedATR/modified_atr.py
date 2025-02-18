import backtrader as bt
import numpy as np

class ModifiedATR(bt.Indicator):
    """
    Modified Average True Range (MATR)
    
    Eine modifizierte Version des ATR, die zusätzliche
    Volatilitätskomponenten und Marktphasen berücksichtigt.
    
    Features:
    - Erweiterte ATR-Berechnung
    - Marktphasenanalyse
    - Volatilitätsnormalisierung
    - Signalgenerierung
    
    Parameter:
    - period (14): ATR Periode
    - smooth_period (10): Glättungsperiode
    - phase_period (20): Marktphasenperiode
    """
    
    lines = ('matr', 'smoothed_matr',
             'market_phase', 'volatility_ratio',
             'signal')
             
    params = (
        ('period', 14),
        ('smooth_period', 10),
        ('phase_period', 20)
    )
    
    plotlines = dict(
        matr=dict(color='blue', _name='MATR'),
        smoothed_matr=dict(color='red', _name='Smoothed MATR'),
        market_phase=dict(color='green', _name='Market Phase'),
        volatility_ratio=dict(color='purple', _name='Volatility Ratio'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(ModifiedATR, self).__init__()
        
        # Historie
        self.tr_history = []
        self.matr_history = []
        self.phase_history = []
        
    def calculate_tr(self):
        """
        Berechnet den True Range.
        """
        if len(self.data) < 2:
            return self.data.high[0] - self.data.low[0]
            
        return max(
            self.data.high[0] - self.data.low[0],
            abs(self.data.high[0] - self.data.close[-1]),
            abs(self.data.low[0] - self.data.close[-1])
        )
        
    def calculate_matr(self):
        """
        Berechnet den modifizierten ATR.
        """
        if len(self.tr_history) < self.p.period:
            return np.mean(self.tr_history)
            
        # Basiskomponente (klassischer ATR)
        atr = np.mean(self.tr_history[-self.p.period:])
        
        # Volatilitätsgewichtung
        vol_weight = np.std(self.tr_history[-self.p.period:])
        
        # Trendkomponente
        if len(self.data) >= self.p.period:
            price_change = abs(
                self.data.close[0] -
                self.data.close[-self.p.period]
            )
            trend_weight = price_change / (
                self.data.close[-self.p.period]
                if self.data.close[-self.p.period] != 0
                else 1
            )
        else:
            trend_weight = 0
            
        # Modifizierter ATR
        return atr * (1 + vol_weight) * (1 + trend_weight)
        
    def calculate_market_phase(self):
        """
        Berechnet die Marktphase.
        """
        if len(self.matr_history) < self.p.phase_period:
            return 0
            
        # Volatilitätstrend
        vol_trend = (
            self.matr_history[-1] -
            np.mean(self.matr_history[-self.p.phase_period:])
        )
        
        # Preisrichtung
        if len(self.data) >= self.p.phase_period:
            price_direction = (
                self.data.close[0] -
                self.data.close[-self.p.phase_period]
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
        if len(self.matr_history) < self.p.period:
            return 1.0
            
        current_vol = np.mean(self.matr_history[-5:])
        historical_vol = np.mean(
            self.matr_history[-self.p.period:]
        )
        
        return (
            current_vol / historical_vol
            if historical_vol != 0 else 1.0
        )
        
    def next(self):
        # True Range berechnen
        tr = self.calculate_tr()
        self.tr_history.append(tr)
        
        # MATR berechnen
        self.lines.matr[0] = self.calculate_matr()
        self.matr_history.append(self.lines.matr[0])
        
        # Geglätteter MATR
        if len(self.matr_history) >= self.p.smooth_period:
            self.lines.smoothed_matr[0] = np.mean(
                self.matr_history[-self.p.smooth_period:]
            )
        else:
            self.lines.smoothed_matr[0] = self.lines.matr[0]
            
        # Marktphase
        phase = self.calculate_market_phase()
        self.lines.market_phase[0] = phase
        self.phase_history.append(phase)
        
        # Volatilitätsverhältnis
        self.lines.volatility_ratio[0] = self.calculate_volatility_ratio()
        
        # Signal
        if (phase > 0 and
            self.lines.matr[0] < self.lines.smoothed_matr[0]):
            self.lines.signal[0] = 1  # Kaufsignal
        elif (phase < 0 and
              self.lines.matr[0] > self.lines.smoothed_matr[0]):
            self.lines.signal[0] = -1  # Verkaufssignal
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.smooth_period,
            self.p.phase_period
        )
        for hist in [self.tr_history, self.matr_history,
                    self.phase_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'matr': {
                'value': self.lines.matr[0],
                'smoothed': self.lines.smoothed_matr[0],
                'trend': (
                    'increasing'
                    if self.lines.matr[0] >
                       self.lines.smoothed_matr[0]
                    else 'decreasing'
                ),
                'divergence': (
                    self.lines.matr[0] -
                    self.lines.smoothed_matr[0]
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
                    (1 - abs(
                        self.lines.matr[0] -
                        self.lines.smoothed_matr[0]
                    ) / self.lines.matr[0])
                    if self.lines.matr[0] != 0
                    else 0
                )
            },
            'risk': {
                'matr_risk': (
                    self.lines.matr[0] /
                    self.lines.smoothed_matr[0]
                    if self.lines.smoothed_matr[0] != 0
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
