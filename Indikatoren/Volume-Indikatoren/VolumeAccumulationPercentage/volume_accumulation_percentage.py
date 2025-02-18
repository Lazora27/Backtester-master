import backtrader as bt
import numpy as np

class VolumeAccumulationPercentage(bt.Indicator):
    """
    Volume Accumulation Percentage
    
    Ein Indikator, der die prozentuale Akkumulation des Volumens
    in Relation zum Preistrend analysiert.
    
    Features:
    - Volumenakkumulation
    - Preistrendanalyse
    - Akkumulationsrate
    - Trendstärkeberechnung
    - Signalgenerierung
    
    Parameter:
    - period (20): Analysezeitraum
    - volume_factor (1.0): Volumenfaktor
    - smooth_period (5): Glättungsperiode
    """
    
    lines = ('vap', 'smoothed_vap',
             'accum_rate', 'price_impact',
             'trend_strength', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 20),
        ('volume_factor', 1.0),
        ('smooth_period', 5),
        ('min_strength', 0.3)
    )
    
    plotlines = dict(
        vap=dict(color='blue', _name='VAP'),
        smoothed_vap=dict(color='red', _name='Smoothed VAP'),
        accum_rate=dict(color='green', _name='Accumulation Rate'),
        price_impact=dict(color='purple', _name='Price Impact'),
        trend_strength=dict(color='orange', _name='Trend Strength'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(VolumeAccumulationPercentage, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.vap_history = []
        self.volume_history = []
        self.price_history = []
        
    def calculate_vap(self):
        """
        Berechnet die Volumenakkumulationsrate.
        """
        if len(self.data) < 2:
            return 0
            
        # Preisänderung
        price_change = (
            self.data.close[0] - self.data.close[-1]
        ) / self.data.close[-1] if self.data.close[-1] != 0 else 0
        
        # Volumengewichtung
        volume = (
            self.data.volume[0] ** self.p.volume_factor
        )
        
        # Akkumulationsrate
        if price_change > 0:
            vap = volume
        elif price_change < 0:
            vap = -volume
        else:
            vap = 0
            
        # Prozentuale Akkumulation
        if len(self.volume_history) >= self.p.period:
            total_volume = sum(
                self.volume_history[-self.p.period:]
            )
            if total_volume > 0:
                vap = (vap / total_volume) * 100
                
        return vap
        
    def calculate_accum_rate(self):
        """
        Berechnet die Akkumulationsrate.
        """
        if len(self.vap_history) < self.p.period:
            return 0
            
        # Durchschnittliche Akkumulation
        avg_vap = np.mean(self.vap_history[-self.p.period:])
        
        # Akkumulationsrate
        if avg_vap != 0:
            rate = (
                self.lines.vap[0] / avg_vap - 1
            )
        else:
            rate = 0
            
        return rate
        
    def calculate_price_impact(self):
        """
        Berechnet den Preiseinfluss.
        """
        if len(self.price_history) < self.p.period:
            return 0
            
        # Preisänderung
        price_change = (
            self.data.close[0] - self.price_history[-self.p.period]
        ) / self.price_history[-self.p.period]
        
        # Volumeneinfluss
        volume_impact = (
            self.data.volume[0] /
            np.mean(self.volume_history[-self.p.period:])
            if len(self.volume_history) >= self.p.period
            else 1.0
        )
        
        # Preiseinfluss
        impact = price_change * volume_impact
        
        return impact
        
    def next(self):
        # VAP berechnen
        self.lines.vap[0] = self.calculate_vap()
        self.vap_history.append(self.lines.vap[0])
        
        # Geglätteter VAP
        self.lines.smoothed_vap[0] = bt.indicators.EMA(
            self.lines.vap, period=self.p.smooth_period
        )[0]
        
        # Akkumulationsrate
        self.lines.accum_rate[0] = self.calculate_accum_rate()
        
        # Preiseinfluss
        self.lines.price_impact[0] = self.calculate_price_impact()
        
        # Trendstärke
        if len(self.vap_history) >= self.p.period:
            self.lines.trend_strength[0] = abs(
                np.mean(self.vap_history[-self.p.period:])
            )
        else:
            self.lines.trend_strength[0] = 0
            
        # Historie aktualisieren
        self.volume_history.append(self.data.volume[0])
        self.price_history.append(self.data.close[0])
        
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.smooth_period
        )
        for hist in [self.vap_history, self.volume_history,
                    self.price_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_vap[0] > 0 and
            self.lines.accum_rate[0] > 0 and
            self.lines.price_impact[0] > 0 and
            self.lines.trend_strength[0] > self.p.min_strength):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_vap[0] < 0 and
            self.lines.accum_rate[0] < 0 and
            self.lines.price_impact[0] < 0 and
            self.lines.trend_strength[0] > self.p.min_strength):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'accumulation': {
                'current': self.lines.vap[0],
                'smoothed': self.lines.smoothed_vap[0],
                'rate': self.lines.accum_rate[0],
                'trend': (
                    'accumulation' if self.lines.vap[0] > 0
                    else 'distribution'
                )
            },
            'volume': {
                'impact': self.lines.price_impact[0],
                'strength': abs(self.lines.price_impact[0]),
                'quality': (
                    'high' if abs(self.lines.price_impact[0]) > 0.5
                    else 'low'
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'persistence': (
                    np.mean([
                        1 if v > 0 else -1
                        for v in self.vap_history[-5:]
                    ]) if len(self.vap_history) >= 5
                    else 0
                ),
                'quality': (
                    'improving' if self.lines.accum_rate[0] > 0
                    else 'deteriorating'
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    self.lines.trend_strength[0] *
                    abs(self.lines.price_impact[0])
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'accumulation_volatility': (
                    np.std(self.vap_history)
                    if len(self.vap_history) > 1
                    else 0
                ),
                'price_risk': abs(self.lines.price_impact[0])
            }
        }
