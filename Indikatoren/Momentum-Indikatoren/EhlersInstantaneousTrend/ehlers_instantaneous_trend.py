import backtrader as bt
import numpy as np

class EhlersInstantaneousTrend(bt.Indicator):
    """
    Ehlers Instantaneous Trend
    
    Ein fortgeschrittener Trend-Indikator, der Zyklusanalyse und
    adaptive Glättung kombiniert.
    
    Features:
    - Adaptive Zyklusberechnung
    - Instantane Trendbestimmung
    - Phasenkorrektur
    - Rauschfilterung
    - Signal-Validierung
    
    Parameter:
    - alpha (0.07): Alpha Parameter
    - cycle_period (20): Zyklusperiode
    - smooth_period (10): Glättungsperiode
    - phase_lag (0): Phasenverschiebung
    """
    
    lines = ('trend', 'cycle', 'phase',
             'smooth', 'trigger',
             'buy_signal', 'sell_signal')
             
    params = (
        ('alpha', 0.07),
        ('cycle_period', 20),
        ('smooth_period', 10),
        ('phase_lag', 0)
    )
    
    plotlines = dict(
        trend=dict(color='blue', _name='Trend'),
        cycle=dict(color='red', _name='Cycle'),
        phase=dict(color='green', _name='Phase'),
        smooth=dict(color='orange', _name='Smooth'),
        trigger=dict(color='purple', _name='Trigger'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(EhlersInstantaneousTrend, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Glättung
        self.ema = bt.indicators.EMA(period=self.p.smooth_period)
        
        # Historie
        self.trend_history = []
        self.cycle_history = []
        self.phase_history = []
        
        # Hilfsarrays
        self.price = []
        self.smooth_price = []
        self.cycle = []
        self.trend = []
        
    def smooth_data(self, data):
        """
        Adaptive Glättung der Daten.
        """
        if len(data) < 4:
            return data[-1] if data else 0
            
        a1 = np.exp(-self.p.alpha)
        b1 = 2 * a1 * np.cos(2 * np.pi / self.p.cycle_period)
        c2 = a1 * a1
        c3 = 1 - 2 * a1 * np.cos(2 * np.pi / self.p.cycle_period) + a1 * a1
        
        return (c3 * data[-1] + b1 * data[-2] - c2 * data[-3]) / 2
        
    def calculate_cycle(self):
        """
        Berechnet die zyklische Komponente.
        """
        if len(self.smooth_price) < 2:
            return 0
            
        # Medianpreis
        price = (self.data.high[0] + self.data.low[0]) / 2
        
        # Zyklische Komponente
        cycle = (
            (1 - 0.5 * self.p.alpha) * (1 - 0.5 * self.p.alpha) *
            (price - 2 * self.smooth_price[-1] + self.smooth_price[-2])
        )
        
        return cycle
        
    def calculate_phase(self):
        """
        Berechnet die Phasenkomponente.
        """
        if len(self.cycle) < self.p.cycle_period:
            return 0
            
        # Dominanter Zyklus
        cycle_period = self.p.cycle_period
        phase = np.arctan2(
            sum(self.cycle[-cycle_period:] * np.sin(
                2 * np.pi * np.arange(cycle_period) / cycle_period
            )),
            sum(self.cycle[-cycle_period:] * np.cos(
                2 * np.pi * np.arange(cycle_period) / cycle_period
            ))
        )
        
        return phase
        
    def next(self):
        # Preisdaten aktualisieren
        price = (self.data.high[0] + self.data.low[0]) / 2
        self.price.append(price)
        
        # Glättung
        smooth_price = self.smooth_data(self.price)
        self.smooth_price.append(smooth_price)
        self.lines.smooth[0] = smooth_price
        
        # Zyklus berechnen
        cycle = self.calculate_cycle()
        self.cycle.append(cycle)
        self.lines.cycle[0] = cycle
        
        # Phase berechnen
        phase = self.calculate_phase()
        self.lines.phase[0] = phase
        
        # Trend berechnen
        if len(self.smooth_price) > 1:
            trend = (
                (1 + 0.5 * self.p.alpha) * smooth_price -
                (0.5 * self.p.alpha) * self.smooth_price[-1]
            )
            self.trend.append(trend)
            self.lines.trend[0] = trend
        else:
            self.lines.trend[0] = smooth_price
            
        # Trigger-Linie
        self.lines.trigger[0] = self.ema(self.lines.trend)
        
        # Historie begrenzen
        max_length = max(
            self.p.cycle_period,
            self.p.smooth_period
        )
        for arr in [self.price, self.smooth_price,
                   self.cycle, self.trend]:
            if len(arr) > max_length:
                arr.pop(0)
                
        # Historie aktualisieren
        self.trend_history.append(self.lines.trend[0])
        self.cycle_history.append(self.lines.cycle[0])
        self.phase_history.append(self.lines.phase[0])
        
        if len(self.trend_history) > self.p.cycle_period:
            self.trend_history.pop(0)
            self.cycle_history.pop(0)
            self.phase_history.pop(0)
            
        # Signal-Generierung
        # Buy Signal
        if (self.lines.trend[0] > self.lines.trigger[0] and
            self.lines.cycle[0] > 0 and
            abs(self.lines.phase[0]) < np.pi/4):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.trend[0] < self.lines.trigger[0] and
            self.lines.cycle[0] < 0 and
            abs(self.lines.phase[0]) < np.pi/4):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'trend': {
                'value': self.lines.trend[0],
                'direction': np.sign(self.lines.trend[0]),
                'strength': abs(
                    self.lines.trend[0] - self.lines.trigger[0]
                ),
                'acceleration': (
                    self.lines.trend[0] - self.trend_history[-2]
                    if len(self.trend_history) > 1
                    else 0
                )
            },
            'cycle': {
                'value': self.lines.cycle[0],
                'phase': self.lines.phase[0],
                'period': self.p.cycle_period,
                'amplitude': np.std(self.cycle_history) if self.cycle_history else 0
            },
            'momentum': {
                'direction': np.sign(
                    self.lines.trend[0] * self.lines.cycle[0]
                ),
                'strength': abs(
                    self.lines.trend[0] * self.lines.cycle[0]
                ),
                'quality': (
                    1 - abs(self.lines.phase[0]) / np.pi
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(
                    self.lines.trend[0] - self.lines.trigger[0]
                ),
                'reliability': (
                    (1 - abs(self.lines.phase[0]) / np.pi) *
                    abs(self.lines.cycle[0])
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'trend_stability': np.std(self.trend_history) if self.trend_history else 0,
                'cycle_stability': np.std(self.cycle_history) if self.cycle_history else 0
            }
        }
