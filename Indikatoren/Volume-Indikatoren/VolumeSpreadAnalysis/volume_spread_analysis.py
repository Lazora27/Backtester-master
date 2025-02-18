import backtrader as bt
import numpy as np

class VolumeSpreadAnalysis(bt.Indicator):
    """
    Volume Spread Analysis (VSA)
    
    Ein fortgeschrittener Indikator, der Volumen, Spread und
    Preisbewegungen analysiert, um Marktmanipulationen zu erkennen.
    
    Features:
    - Spread-Analyse
    - Volumenklassifizierung
    - Preisbereichsanalyse
    - Marktphasenidentifikation
    - Signalgenerierung
    
    Parameter:
    - period (20): Analysezeitraum
    - volume_threshold (1.5): Volumenschwelle
    - spread_factor (0.5): Spread-Gewichtung
    """
    
    lines = ('vsa', 'effort',
             'spread_strength', 'volume_class',
             'market_phase', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 20),
        ('volume_threshold', 1.5),
        ('spread_factor', 0.5),
        ('min_strength', 0.3)
    )
    
    plotlines = dict(
        vsa=dict(color='blue', _name='VSA'),
        effort=dict(color='red', _name='Effort'),
        spread_strength=dict(color='green', _name='Spread Strength'),
        volume_class=dict(color='purple', _name='Volume Class'),
        market_phase=dict(color='orange', _name='Market Phase'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(VolumeSpreadAnalysis, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.vsa_history = []
        self.spread_history = []
        self.volume_history = []
        
    def calculate_vsa(self):
        """
        Berechnet den VSA-Wert.
        """
        if len(self.data) < 2:
            return 0
            
        # Spread berechnen
        spread = self.data.high[0] - self.data.low[0]
        
        # Volumenklassifizierung
        if len(self.volume_history) >= self.p.period:
            avg_volume = np.mean(self.volume_history[-self.p.period:])
            volume_ratio = (
                self.data.volume[0] / avg_volume
                if avg_volume > 0 else 1.0
            )
        else:
            volume_ratio = 1.0
            
        # VSA berechnen
        vsa = (
            spread * self.p.spread_factor +
            volume_ratio * (1 - self.p.spread_factor)
        )
        
        return vsa
        
    def calculate_effort(self):
        """
        Berechnet den Aufwand (Effort).
        """
        if len(self.data) < 2:
            return 0
            
        # Preisänderung
        price_change = abs(
            self.data.close[0] - self.data.close[-1]
        )
        
        # Volumenaufwand
        volume_effort = (
            self.data.volume[0] /
            np.mean(self.volume_history[-self.p.period:])
            if len(self.volume_history) >= self.p.period
            else 1.0
        )
        
        # Effort berechnen
        effort = price_change * volume_effort
        
        return effort
        
    def classify_volume(self):
        """
        Klassifiziert das Volumen.
        """
        if len(self.volume_history) < self.p.period:
            return 0
            
        # Durchschnittliches Volumen
        avg_volume = np.mean(self.volume_history[-self.p.period:])
        
        # Volumenklassifizierung
        if self.data.volume[0] > avg_volume * self.p.volume_threshold:
            volume_class = 1  # Hohes Volumen
        elif self.data.volume[0] < avg_volume / self.p.volume_threshold:
            volume_class = -1  # Niedriges Volumen
        else:
            volume_class = 0  # Normales Volumen
            
        return volume_class
        
    def identify_market_phase(self):
        """
        Identifiziert die Marktphase.
        """
        if len(self.vsa_history) < self.p.period:
            return 0
            
        # VSA-Trend
        vsa_trend = np.mean([
            1 if vsa > self.vsa_history[i-1]
            else -1
            for i, vsa in enumerate(self.vsa_history[-5:])
            if i > 0
        ]) if len(self.vsa_history) >= 5 else 0
        
        # Effort-Trend
        effort_trend = (
            1 if self.lines.effort[0] > self.lines.effort[-1]
            else -1
        )
        
        # Marktphase
        phase = vsa_trend * effort_trend
        
        return phase
        
    def next(self):
        # VSA berechnen
        self.lines.vsa[0] = self.calculate_vsa()
        self.vsa_history.append(self.lines.vsa[0])
        
        # Effort berechnen
        self.lines.effort[0] = self.calculate_effort()
        
        # Spread-Stärke
        spread = self.data.high[0] - self.data.low[0]
        self.lines.spread_strength[0] = (
            spread / self.data.close[0]
            if self.data.close[0] != 0
            else 0
        )
        
        # Volumenklassifizierung
        self.lines.volume_class[0] = self.classify_volume()
        
        # Marktphase
        self.lines.market_phase[0] = self.identify_market_phase()
        
        # Historie aktualisieren
        self.spread_history.append(spread)
        self.volume_history.append(self.data.volume[0])
        
        # Historie begrenzen
        max_period = self.p.period
        for hist in [self.vsa_history, self.spread_history,
                    self.volume_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.vsa[0] > self.p.min_strength and
            self.lines.effort[0] > 0 and
            self.lines.volume_class[0] > 0 and
            self.lines.market_phase[0] > 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.vsa[0] > self.p.min_strength and
            self.lines.effort[0] < 0 and
            self.lines.volume_class[0] > 0 and
            self.lines.market_phase[0] < 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'vsa': {
                'value': self.lines.vsa[0],
                'effort': self.lines.effort[0],
                'trend': (
                    'increasing' if self.lines.vsa[0] > self.lines.vsa[-1]
                    else 'decreasing'
                )
            },
            'spread': {
                'strength': self.lines.spread_strength[0],
                'trend': (
                    'widening' if self.lines.spread_strength[0] > self.lines.spread_strength[-1]
                    else 'narrowing'
                ),
                'quality': (
                    'high' if self.lines.spread_strength[0] > 0.5
                    else 'low'
                )
            },
            'volume': {
                'class': (
                    'high' if self.lines.volume_class[0] > 0
                    else 'low' if self.lines.volume_class[0] < 0
                    else 'normal'
                ),
                'effort': abs(self.lines.effort[0]),
                'quality': (
                    'strong' if abs(self.lines.effort[0]) > 0.5
                    else 'weak'
                )
            },
            'market': {
                'phase': self.lines.market_phase[0],
                'condition': (
                    'accumulation' if self.lines.market_phase[0] > 0
                    else 'distribution' if self.lines.market_phase[0] < 0
                    else 'neutral'
                ),
                'strength': abs(self.lines.market_phase[0])
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(self.lines.market_phase[0]),
                'reliability': (
                    abs(self.lines.market_phase[0]) *
                    abs(self.lines.effort[0])
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'spread_risk': self.lines.spread_strength[0],
                'volume_risk': abs(self.lines.volume_class[0])
            }
        }
