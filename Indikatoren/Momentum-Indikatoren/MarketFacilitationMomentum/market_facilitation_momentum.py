import backtrader as bt
import numpy as np

class MarketFacilitationMomentum(bt.Indicator):
    """
    Market Facilitation Momentum Indicator
    
    Ein fortgeschrittener Momentum-Indikator, der Marktfazilitation
    und Volumenanalyse kombiniert.
    
    Features:
    - Marktfazilitations-Index
    - Volumen-Momentum
    - Preisbewegungseffizienz
    - Marktphasen-Analyse
    - Signal-Validierung
    
    Parameter:
    - volume_period (14): Volumenperiode
    - momentum_period (10): Momentumperiode
    - smooth_period (5): Glättungsperiode
    - threshold (0.5): Signalschwelle
    """
    
    lines = ('mfi', 'volume_momentum', 'efficiency',
             'market_phase', 'strength',
             'buy_signal', 'sell_signal')
             
    params = (
        ('volume_period', 14),
        ('momentum_period', 10),
        ('smooth_period', 5),
        ('threshold', 0.5)
    )
    
    plotlines = dict(
        mfi=dict(color='blue', _name='MFI'),
        volume_momentum=dict(color='red', _name='Volume Mom'),
        efficiency=dict(color='green', _name='Efficiency'),
        market_phase=dict(color='purple', _name='Market Phase'),
        strength=dict(color='orange', _name='Strength'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(MarketFacilitationMomentum, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Glättung
        self.ema = bt.indicators.EMA(period=self.p.smooth_period)
        
        # Historie
        self.price_history = []
        self.volume_history = []
        self.mfi_history = []
        
    def calculate_mfi(self):
        """
        Berechnet den Market Facilitation Index.
        """
        if len(self.data) < 2:
            return 0
            
        # Preisbewegung
        high_low_range = self.data.high[0] - self.data.low[0]
        
        # Volumen
        if self.data.volume[0] == 0:
            return 0
            
        return high_low_range / self.data.volume[0]
        
    def calculate_volume_momentum(self):
        """
        Berechnet das Volumen-Momentum.
        """
        if len(self.volume_history) < self.p.volume_period:
            return 0
            
        current_vol = np.mean(self.volume_history[-5:])
        prev_vol = np.mean(self.volume_history[-self.p.volume_period:-5])
        
        if prev_vol == 0:
            return 0
            
        return (current_vol - prev_vol) / prev_vol
        
    def calculate_efficiency(self):
        """
        Berechnet die Preisbewegungseffizienz.
        """
        if len(self.price_history) < self.p.momentum_period:
            return 0
            
        # Direkte Distanz
        net_movement = abs(
            self.price_history[-1] -
            self.price_history[-self.p.momentum_period]
        )
        
        # Gesamtdistanz
        total_movement = sum(
            abs(self.price_history[i] - self.price_history[i-1])
            for i in range(-self.p.momentum_period+1, 0)
        )
        
        if total_movement == 0:
            return 0
            
        return net_movement / total_movement
        
    def identify_market_phase(self):
        """
        Identifiziert die aktuelle Marktphase.
        """
        if len(self.mfi_history) < 2 or len(self.volume_history) < 2:
            return 0
            
        # MFI-Änderung
        mfi_change = self.mfi_history[-1] - self.mfi_history[-2]
        
        # Volumen-Änderung
        vol_change = (
            self.volume_history[-1] - self.volume_history[-2]
        )
        
        # Phasen-Klassifikation
        if mfi_change > 0 and vol_change > 0:
            return 1  # Bullish
        elif mfi_change < 0 and vol_change < 0:
            return -1  # Bearish
        else:
            return 0  # Neutral
            
    def next(self):
        # Market Facilitation Index
        self.lines.mfi[0] = self.calculate_mfi()
        
        # Historie aktualisieren
        self.price_history.append(self.data[0])
        self.volume_history.append(self.data.volume[0])
        self.mfi_history.append(self.lines.mfi[0])
        
        # Volumen-Momentum
        self.lines.volume_momentum[0] = self.calculate_volume_momentum()
        
        # Effizienz
        self.lines.efficiency[0] = self.calculate_efficiency()
        
        # Marktphase
        self.lines.market_phase[0] = self.identify_market_phase()
        
        # Signalstärke
        self.lines.strength[0] = (
            abs(self.lines.volume_momentum[0]) *
            self.lines.efficiency[0]
        )
        
        # Historie begrenzen
        max_period = max(
            self.p.volume_period,
            self.p.momentum_period
        )
        for hist in [self.price_history, self.volume_history, self.mfi_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.market_phase[0] > 0 and
            self.lines.volume_momentum[0] > 0 and
            self.lines.efficiency[0] > self.p.threshold):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.market_phase[0] < 0 and
            self.lines.volume_momentum[0] < 0 and
            self.lines.efficiency[0] > self.p.threshold):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'facilitation': {
                'mfi': self.lines.mfi[0],
                'efficiency': self.lines.efficiency[0],
                'volume_momentum': self.lines.volume_momentum[0],
                'market_phase': self.lines.market_phase[0]
            },
            'market_conditions': {
                'phase': (
                    'bullish' if self.lines.market_phase[0] > 0
                    else 'bearish' if self.lines.market_phase[0] < 0
                    else 'neutral'
                ),
                'strength': self.lines.strength[0],
                'efficiency': (
                    'high' if self.lines.efficiency[0] > 0.7
                    else 'medium' if self.lines.efficiency[0] > 0.3
                    else 'low'
                )
            },
            'volume_analysis': {
                'momentum': self.lines.volume_momentum[0],
                'trend': (
                    'increasing' if self.lines.volume_momentum[0] > 0
                    else 'decreasing'
                ),
                'quality': (
                    'high' if abs(self.lines.volume_momentum[0]) > 0.1
                    else 'medium' if abs(self.lines.volume_momentum[0]) > 0.05
                    else 'low'
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.strength[0],
                'reliability': (
                    self.lines.efficiency[0] *
                    abs(self.lines.market_phase[0]) *
                    (1 + abs(self.lines.volume_momentum[0]))
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'volume_stability': (
                    np.std(self.volume_history) /
                    np.mean(self.volume_history)
                    if self.volume_history and np.mean(self.volume_history) != 0
                    else 0
                ),
                'mfi_stability': (
                    np.std(self.mfi_history)
                    if self.mfi_history
                    else 0
                )
            }
        }
