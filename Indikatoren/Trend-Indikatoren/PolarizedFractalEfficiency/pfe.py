import backtrader as bt
import numpy as np

class PolarizedFractalEfficiency(bt.Indicator):
    """
    Polarized Fractal Efficiency (PFE) Indicator
    
    Ein fortgeschrittener Trendfolge-Indikator, der die Effizienz der
    Preisbewegung durch fraktale Analyse misst.
    
    Features:
    - Fraktale Effizienzberechnung
    - Polarisierte Signalgenerierung
    - Trend-Effizienzanalyse
    - Adaptive Glättung
    - Multi-Timeframe Analyse
    
    Parameter:
    - period (10): Basisperiode für Berechnung
    - smooth_period (5): Glättungsperiode
    - threshold (50): Schwellenwert für Signale
    - fractal_dimension (2): Fraktale Dimension
    """
    
    lines = ('pfe', 'smooth_pfe', 'efficiency',
             'fractal_dimension', 'polarity',
             'upper_band', 'lower_band',
             'buy_signal', 'sell_signal')
             
    params = (
        ('period', 10),
        ('smooth_period', 5),
        ('threshold', 50),
        ('fractal_dimension', 2)
    )
    
    plotlines = dict(
        pfe=dict(color='blue', _name='PFE'),
        smooth_pfe=dict(color='red', _name='Smooth PFE'),
        efficiency=dict(color='green', _name='Efficiency'),
        fractal_dimension=dict(color='purple', _name='Fractal Dim'),
        polarity=dict(color='orange', _name='Polarity'),
        upper_band=dict(color='gray', _name='Upper Band'),
        lower_band=dict(color='gray', _name='Lower Band'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(PolarizedFractalEfficiency, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        
        # Glättung
        self.ema = bt.indicators.EMA(period=self.p.smooth_period)
        
        # Historie
        self.price_history = []
        self.pfe_history = []
        self.efficiency_history = []
        
    def calculate_fractal_length(self, prices):
        """
        Berechnet die fraktale Länge einer Preisreihe.
        """
        if len(prices) < 2:
            return 0
            
        # Direkte Distanz
        direct = abs(prices[-1] - prices[0])
        
        # Pfadlänge
        path = sum(
            abs(prices[i] - prices[i-1])
            for i in range(1, len(prices))
        )
        
        if path == 0:
            return 0
            
        # Fraktale Effizienz
        efficiency = (direct / path) ** self.p.fractal_dimension
        
        return efficiency * 100
        
    def calculate_polarity(self):
        """
        Berechnet die Polarität der Preisbewegung.
        """
        if len(self.price_history) < self.p.period:
            return 0
            
        # Preisänderung
        price_change = self.price_history[-1] - self.price_history[0]
        
        # Polarität (-1 bis 1)
        polarity = np.sign(price_change)
        
        return polarity
        
    def calculate_efficiency(self):
        """
        Berechnet die Effizienz der Preisbewegung.
        """
        if len(self.pfe_history) < self.p.period:
            return 0
            
        # Trend-Konsistenz
        consistency = np.std(self.pfe_history)
        
        # Trend-Stärke
        strength = abs(np.mean(self.pfe_history))
        
        # Effizienz (0-1)
        efficiency = (strength / 100) * (1 / (1 + consistency))
        
        return efficiency
        
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.data[0])
        if len(self.price_history) > self.p.period:
            self.price_history.pop(0)
            
        # PFE berechnen
        if len(self.price_history) >= self.p.period:
            self.lines.pfe[0] = (
                self.calculate_fractal_length(self.price_history) *
                self.calculate_polarity()
            )
        else:
            self.lines.pfe[0] = 0
            
        # Geglätteter PFE
        self.lines.smooth_pfe[0] = self.ema(self.lines.pfe)
        
        # Historie aktualisieren
        self.pfe_history.append(self.lines.pfe[0])
        if len(self.pfe_history) > self.p.period:
            self.pfe_history.pop(0)
            
        # Andere Metriken
        self.lines.efficiency[0] = self.calculate_efficiency()
        self.lines.fractal_dimension[0] = self.p.fractal_dimension
        self.lines.polarity[0] = self.calculate_polarity()
        
        # Bänder
        self.lines.upper_band[0] = self.p.threshold
        self.lines.lower_band[0] = -self.p.threshold
        
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smooth_pfe[0] > self.p.threshold and
            self.lines.efficiency[0] > 0.6 and
            self.lines.polarity[0] > 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smooth_pfe[0] < -self.p.threshold and
            self.lines.efficiency[0] > 0.6 and
            self.lines.polarity[0] < 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'pfe': {
                'current': self.lines.pfe[0],
                'smooth': self.lines.smooth_pfe[0],
                'efficiency': self.lines.efficiency[0],
                'polarity': self.lines.polarity[0]
            },
            'fractal': {
                'dimension': self.lines.fractal_dimension[0],
                'efficiency': self.calculate_efficiency(),
                'stability': np.std(self.pfe_history) if self.pfe_history else 0
            },
            'trend': {
                'direction': ('up' if self.lines.smooth_pfe[0] > 0
                            else 'down'),
                'strength': abs(self.lines.smooth_pfe[0]),
                'quality': self.lines.efficiency[0]
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(self.lines.smooth_pfe[0]) / 100,
                'reliability': (
                    self.lines.efficiency[0] *
                    abs(self.lines.smooth_pfe[0]) / 100
                )
            },
            'risk': {
                'volatility': self.atr[0] / self.data[0] if self.data[0] != 0 else 0,
                'fractal_risk': 1 - self.lines.efficiency[0],
                'trend_stability': (
                    1 - np.std(self.pfe_history) / 100
                    if self.pfe_history else 0
                )
            }
        }
