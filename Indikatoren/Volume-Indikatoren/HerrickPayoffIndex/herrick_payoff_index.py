import backtrader as bt
import numpy as np

class HerrickPayoffIndex(bt.Indicator):
    """
    Herrick Payoff Index
    
    Ein Indikator, der die Beziehung zwischen Preis,
    Volumen und Open Interest analysiert.
    
    Features:
    - Payoff-Analyse
    - Volumengewichtung
    - Open Interest Integration
    - Trendstärkeberechnung
    - Signal-Validierung
    
    Parameter:
    - period (20): Basisperiode
    - volume_factor (1.0): Volumenfaktor
    - payoff_threshold (100): Payoff-Schwelle
    """
    
    lines = ('hpi', 'smoothed_hpi',
             'open_interest_impact', 'trend_strength',
             'volume_efficiency', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 20),
        ('volume_factor', 1.0),
        ('payoff_threshold', 100),
        ('min_trend_strength', 0.3)
    )
    
    plotlines = dict(
        hpi=dict(color='blue', _name='HPI'),
        smoothed_hpi=dict(color='red', _name='Smoothed HPI'),
        open_interest_impact=dict(color='purple', _name='OI Impact'),
        trend_strength=dict(color='orange', _name='Trend Strength'),
        volume_efficiency=dict(color='green', _name='Volume Efficiency'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(HerrickPayoffIndex, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.hpi_history = []
        self.volume_history = []
        self.oi_history = []
        
    def calculate_hpi(self):
        """
        Berechnet den Herrick Payoff Index.
        """
        if len(self.data) < 2:
            return 0
            
        # Preisbewegung
        price_change = self.data.close[0] - self.data.close[-1]
        
        # Volumengewichtung
        volume_weight = 1.0
        if len(self.volume_history) >= self.p.period:
            avg_volume = np.mean(self.volume_history[-self.p.period:])
            if avg_volume > 0:
                volume_weight = (
                    self.data.volume[0] / avg_volume
                ) ** self.p.volume_factor
                
        # Open Interest Einfluss
        oi_impact = 1.0
        if hasattr(self.data, 'openinterest') and self.data.openinterest:
            if len(self.oi_history) >= 2:
                oi_change = (
                    self.data.openinterest[0] -
                    self.data.openinterest[-1]
                )
                if self.data.openinterest[-1] != 0:
                    oi_impact = 1 + (oi_change / self.data.openinterest[-1])
                    
        # HPI berechnen
        hpi = price_change * volume_weight * oi_impact * self.data.volume[0]
        
        # Normalisierung
        if self.data.close[0] != 0:
            hpi = hpi / self.data.close[0]
            
        return hpi
        
    def calculate_volume_efficiency(self):
        """
        Berechnet die Volumeneffizienz.
        """
        if len(self.volume_history) < self.p.period:
            return 0
            
        # Durchschnittliches Volumen
        avg_volume = np.mean(self.volume_history[-self.p.period:])
        
        # Effizienzmaß
        if avg_volume > 0:
            efficiency = (
                abs(self.data.close[0] - self.data.close[-self.p.period]) /
                (sum(abs(self.data.close[-i] - self.data.close[-i-1])
                     for i in range(self.p.period)) + 1e-10)
            )
        else:
            efficiency = 0
            
        return efficiency
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.hpi_history) < 2:
            return 0
            
        # HPI-Momentum
        momentum = self.hpi_history[-1] - self.hpi_history[-2]
        
        # Relative Stärke
        strength = abs(momentum)
        
        return min(1.0, strength)
        
    def next(self):
        # HPI berechnen
        self.lines.hpi[0] = self.calculate_hpi()
        self.hpi_history.append(self.lines.hpi[0])
        
        # Geglätteter HPI
        self.lines.smoothed_hpi[0] = bt.indicators.EMA(
            self.lines.hpi, period=self.p.period
        )[0]
        
        # Historie aktualisieren
        self.volume_history.append(self.data.volume[0])
        if hasattr(self.data, 'openinterest') and self.data.openinterest:
            self.oi_history.append(self.data.openinterest[0])
            
        # Open Interest Einfluss
        if len(self.oi_history) >= 2:
            self.lines.open_interest_impact[0] = (
                self.oi_history[-1] / self.oi_history[-2]
                if self.oi_history[-2] > 0
                else 1.0
            )
        else:
            self.lines.open_interest_impact[0] = 1.0
            
        # Volumeneffizienz
        self.lines.volume_efficiency[0] = self.calculate_volume_efficiency()
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Historie begrenzen
        max_period = self.p.period
        for hist in [self.hpi_history, self.volume_history,
                    self.oi_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_hpi[0] > self.p.payoff_threshold and
            self.lines.volume_efficiency[0] > 0.5 and
            self.lines.trend_strength[0] > self.p.min_trend_strength and
            self.lines.open_interest_impact[0] > 1.0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_hpi[0] < -self.p.payoff_threshold and
            self.lines.volume_efficiency[0] > 0.5 and
            self.lines.trend_strength[0] > self.p.min_trend_strength and
            self.lines.open_interest_impact[0] > 1.0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'payoff': {
                'hpi': self.lines.hpi[0],
                'smoothed': self.lines.smoothed_hpi[0],
                'momentum': (
                    self.lines.hpi[0] - self.hpi_history[-2]
                    if len(self.hpi_history) > 1
                    else 0
                )
            },
            'open_interest': {
                'impact': self.lines.open_interest_impact[0],
                'trend': (
                    'increasing'
                    if self.lines.open_interest_impact[0] > 1
                    else 'decreasing'
                ),
                'significance': (
                    abs(self.lines.open_interest_impact[0] - 1)
                )
            },
            'volume': {
                'efficiency': self.lines.volume_efficiency[0],
                'trend': (
                    'efficient' if self.lines.volume_efficiency[0] > 0.5
                    else 'inefficient'
                ),
                'quality': self.lines.volume_efficiency[0] * 100
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': np.sign(self.lines.smoothed_hpi[0]),
                'persistence': (
                    np.mean([
                        1 if hpi > 0
                        else -1 if hpi < 0
                        else 0
                        for hpi in self.hpi_history[-5:]
                    ]) if len(self.hpi_history) >= 5
                    else 0
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    self.lines.trend_strength[0] *
                    self.lines.volume_efficiency[0] *
                    self.lines.open_interest_impact[0]
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'hpi_stability': (
                    np.std(self.hpi_history)
                    if len(self.hpi_history) > 1
                    else 0
                ),
                'volume_risk': (
                    1 - self.lines.volume_efficiency[0]
                    if self.lines.volume_efficiency[0] > 0
                    else 1
                )
            }
        }
