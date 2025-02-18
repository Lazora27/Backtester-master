import backtrader as bt
import numpy as np

class KaufmanEfficiencyRatio(bt.Indicator):
    """
    Kaufman Efficiency Ratio (KER)
    
    Ein fortgeschrittener Momentum-Indikator, der die Effizienz der Preisbewegung misst.
    Entwickelt von Perry Kaufman, hilft der KER bei der Identifizierung von Trend- und
    Seitwärtsphasen.
    
    Features:
    - Basis KER Berechnung
    - Adaptive Smoothing
    - Trend Strength Analysis
    - Multi-Timeframe Integration
    - Signal Generation
    
    Parameter:
    - period (10): Basisperiode für Berechnungen
    - smooth_period (3): Glättungsperiode
    - threshold_high (0.7): Obere Schwelle für starken Trend
    - threshold_low (0.3): Untere Schwelle für schwachen Trend
    - mtf_periods ([5,10,20]): Multi-Timeframe Perioden
    """
    
    lines = ('ker', 'ker_smooth', 'trend_strength',
             'mtf_ker_fast', 'mtf_ker_mid', 'mtf_ker_slow',
             'strong_trend', 'weak_trend')
             
    params = (
        ('period', 10),
        ('smooth_period', 3),
        ('threshold_high', 0.7),
        ('threshold_low', 0.3),
        ('mtf_periods', [5, 10, 20])
    )
    
    plotlines = dict(
        ker=dict(color='blue', _name='KER'),
        ker_smooth=dict(color='red', _name='Smooth KER'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        mtf_ker_fast=dict(color='purple', _name='Fast KER'),
        mtf_ker_mid=dict(color='orange', _name='Mid KER'),
        mtf_ker_slow=dict(color='brown', _name='Slow KER'),
        strong_trend=dict(_name='Strong Trend', color='green', marker='^'),
        weak_trend=dict(_name='Weak Trend', color='red', marker='v')
    )
    
    def __init__(self):
        super(KaufmanEfficiencyRatio, self).__init__()
        
        # Preisänderung und Volatilität
        self.price_change = self.data - self.data(-self.p.period)
        self.volatility = bt.indicators.SumN(abs(self.data - self.data(-1)),
                                           period=self.p.period)
                                           
        # Multi-Timeframe KERs
        self.ker_fast = self.calculate_ker(self.p.mtf_periods[0])
        self.ker_mid = self.calculate_ker(self.p.mtf_periods[1])
        self.ker_slow = self.calculate_ker(self.p.mtf_periods[2])
        
        # Gleitender Durchschnitt
        self.ker_ma = bt.indicators.SMA(self.lines.ker,
                                      period=self.p.smooth_period)
                                      
    def calculate_ker(self, period):
        """
        Berechnet den KER für eine bestimmte Periode.
        
        Parameter:
        - period: Berechnungsperiode
        """
        price_change = self.data - self.data(-period)
        volatility = bt.indicators.SumN(abs(self.data - self.data(-1)),
                                      period=period)
                                      
        return abs(price_change) / volatility
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke basierend auf Multi-Timeframe KERs.
        """
        # Gewichtete Summe der verschiedenen Timeframes
        weights = [0.5, 0.3, 0.2]  # Gewichtung: Fast, Mid, Slow
        
        strength = (self.lines.mtf_ker_fast[0] * weights[0] +
                   self.lines.mtf_ker_mid[0] * weights[1] +
                   self.lines.mtf_ker_slow[0] * weights[2])
                   
        return strength
        
    def next(self):
        # Basis KER
        if self.volatility[0] != 0:
            self.lines.ker[0] = abs(self.price_change[0]) / self.volatility[0]
        else:
            self.lines.ker[0] = 0
            
        # Geglätteter KER
        self.lines.ker_smooth[0] = self.ker_ma[0]
        
        # Multi-Timeframe KERs
        self.lines.mtf_ker_fast[0] = self.ker_fast[0]
        self.lines.mtf_ker_mid[0] = self.ker_mid[0]
        self.lines.mtf_ker_slow[0] = self.ker_slow[0]
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Signal-Generierung
        if self.lines.ker[0] > self.p.threshold_high:
            # Starker Trend
            self.lines.strong_trend[0] = self.data.low[0]
            self.lines.weak_trend[0] = float('nan')
        elif self.lines.ker[0] < self.p.threshold_low:
            # Schwacher Trend
            self.lines.strong_trend[0] = float('nan')
            self.lines.weak_trend[0] = self.data.high[0]
        else:
            # Neutral
            self.lines.strong_trend[0] = float('nan')
            self.lines.weak_trend[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des aktuellen Marktzustands.
        """
        return {
            'current_ker': self.lines.ker[0],
            'smooth_ker': self.lines.ker_smooth[0],
            'trend_strength': self.lines.trend_strength[0],
            'market_state': ('Strong Trend' if self.lines.ker[0] > self.p.threshold_high
                           else 'Weak Trend' if self.lines.ker[0] < self.p.threshold_low
                           else 'Neutral'),
            'mtf_analysis': {
                'fast': self.lines.mtf_ker_fast[0],
                'mid': self.lines.mtf_ker_mid[0],
                'slow': self.lines.mtf_ker_slow[0]
            }
        }
