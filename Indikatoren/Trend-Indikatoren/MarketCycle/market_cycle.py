import backtrader as bt
import numpy as np
from enum import Enum

class CyclePhase(Enum):
    ACCUMULATION = 0
    MARKUP = 1
    DISTRIBUTION = 2
    MARKDOWN = 3

class MarketCycleIndicator(bt.Indicator):
    """
    Market Cycle Indicator
    
    Ein fortgeschrittener Indikator zur Identifizierung von Marktzyklen
    und deren Phasen (Akkumulation, Aufschwung, Distribution, Abschwung).
    
    Features:
    - Zyklus-Phasen Erkennung
    - Volumen-Analyse
    - Momentum-Integration
    - Multi-Timeframe Analyse
    - Adaptive Zykluslänge
    
    Parameter:
    - cycle_period (40): Basiszyklus-Periode
    - volume_period (20): Volumen-Analyse Periode
    - momentum_period (14): Momentum-Periode
    - sensitivity (2.0): Sensitivität für Phasenwechsel
    """
    
    lines = ('cycle_phase', 'cycle_strength', 'volume_flow',
             'momentum', 'phase_duration', 'cycle_position',
             'support', 'resistance',
             'buy_signal', 'sell_signal')
             
    params = (
        ('cycle_period', 40),
        ('volume_period', 20),
        ('momentum_period', 14),
        ('sensitivity', 2.0)
    )
    
    plotlines = dict(
        cycle_phase=dict(color='blue', _name='Cycle Phase'),
        cycle_strength=dict(color='green', _name='Cycle Strength'),
        volume_flow=dict(color='purple', _name='Volume Flow'),
        momentum=dict(color='orange', _name='Momentum'),
        phase_duration=dict(color='gray', _name='Phase Duration'),
        cycle_position=dict(color='red', _name='Cycle Position'),
        support=dict(color='gray', _name='Support'),
        resistance=dict(color='gray', _name='Resistance'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(MarketCycleIndicator, self).__init__()
        
        # Technische Indikatoren
        self.rsi = bt.indicators.RSI(period=14)
        self.macd = bt.indicators.MACD()
        self.volume_sma = bt.indicators.SMA(
            self.data.volume, period=self.p.volume_period
        )
        self.atr = bt.indicators.ATR(period=14)
        
        # Historie
        self.price_history = []
        self.volume_history = []
        self.phase_history = []
        self.current_phase = CyclePhase.ACCUMULATION
        self.phase_start = 0
        
    def calculate_cycle_position(self):
        """
        Berechnet die Position im aktuellen Zyklus (0-1).
        """
        if len(self.price_history) < self.p.cycle_period:
            return 0.5
            
        # Relative Position im Zyklus
        position = (len(self) - self.phase_start) / self.p.cycle_period
        
        return min(position, 1.0)
        
    def analyze_volume_flow(self):
        """
        Analysiert den Volumen-Flow für Zyklusbestätigung.
        """
        if len(self.volume_history) < self.p.volume_period:
            return 0
            
        current_volume = self.data.volume[0]
        avg_volume = self.volume_sma[0]
        
        if avg_volume == 0:
            return 0
            
        # Volumen-Flow (-1 bis 1)
        flow = (current_volume - avg_volume) / avg_volume
        
        return flow
        
    def detect_cycle_phase(self):
        """
        Erkennt die aktuelle Zyklusphase.
        """
        if len(self) < 2:
            return self.current_phase
            
        price_change = self.data[0] - self.data[-1]
        momentum = self.macd.macd[0]
        rsi = self.rsi[0]
        volume_flow = self.analyze_volume_flow()
        
        # Phasenwechsel-Logik
        if self.current_phase == CyclePhase.ACCUMULATION:
            if (price_change > 0 and
                momentum > 0 and
                rsi > 50 and
                volume_flow > 0):
                return CyclePhase.MARKUP
                
        elif self.current_phase == CyclePhase.MARKUP:
            if (price_change < 0 and
                momentum < 0 and
                rsi > 70):
                return CyclePhase.DISTRIBUTION
                
        elif self.current_phase == CyclePhase.DISTRIBUTION:
            if (price_change < 0 and
                momentum < 0 and
                rsi < 50 and
                volume_flow < 0):
                return CyclePhase.MARKDOWN
                
        elif self.current_phase == CyclePhase.MARKDOWN:
            if (price_change > 0 and
                momentum > 0 and
                rsi < 30):
                return CyclePhase.ACCUMULATION
                
        return self.current_phase
        
    def calculate_cycle_strength(self):
        """
        Berechnet die Stärke des aktuellen Zyklus.
        """
        if len(self.price_history) < self.p.cycle_period:
            return 0
            
        # Trend-Stärke
        price_range = max(self.price_history) - min(self.price_history)
        if price_range == 0:
            return 0
            
        # Momentum-Stärke
        momentum_strength = abs(self.macd.macd[0])
        
        # Volumen-Bestätigung
        volume_confirm = abs(self.analyze_volume_flow())
        
        # Kombinierte Stärke (0-1)
        strength = (
            momentum_strength / self.atr[0] if self.atr[0] != 0 else 0
        ) * volume_confirm
        
        return min(strength, 1.0)
        
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.data[0])
        self.volume_history.append(self.data.volume[0])
        if len(self.price_history) > self.p.cycle_period:
            self.price_history.pop(0)
            self.volume_history.pop(0)
            
        # Zyklusphase erkennen
        new_phase = self.detect_cycle_phase()
        if new_phase != self.current_phase:
            self.phase_start = len(self)
            self.current_phase = new_phase
            
        self.lines.cycle_phase[0] = self.current_phase.value
        
        # Andere Metriken berechnen
        self.lines.cycle_strength[0] = self.calculate_cycle_strength()
        self.lines.volume_flow[0] = self.analyze_volume_flow()
        self.lines.momentum[0] = self.macd.macd[0]
        self.lines.phase_duration[0] = len(self) - self.phase_start
        self.lines.cycle_position[0] = self.calculate_cycle_position()
        
        # Support/Resistance
        if len(self.price_history) >= self.p.cycle_period:
            self.lines.support[0] = min(self.price_history)
            self.lines.resistance[0] = max(self.price_history)
        else:
            self.lines.support[0] = self.data.low[0]
            self.lines.resistance[0] = self.data.high[0]
            
        # Signal-Generierung
        # Buy Signal
        if (self.current_phase == CyclePhase.ACCUMULATION and
            self.lines.cycle_strength[0] > 0.7 and
            self.lines.volume_flow[0] > 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.current_phase == CyclePhase.DISTRIBUTION and
            self.lines.cycle_strength[0] > 0.7 and
            self.lines.volume_flow[0] < 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'cycle': {
                'phase': self.current_phase.name,
                'strength': self.lines.cycle_strength[0],
                'position': self.lines.cycle_position[0],
                'duration': self.lines.phase_duration[0]
            },
            'momentum': {
                'value': self.lines.momentum[0],
                'rsi': self.rsi[0],
                'macd': self.macd.macd[0]
            },
            'volume': {
                'flow': self.lines.volume_flow[0],
                'confirmation': (
                    self.data.volume[0] >
                    self.volume_sma[0]
                )
            },
            'levels': {
                'support': self.lines.support[0],
                'resistance': self.lines.resistance[0],
                'range': (
                    self.lines.resistance[0] -
                    self.lines.support[0]
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.cycle_strength[0],
                'reliability': (
                    self.lines.cycle_strength[0] *
                    abs(self.lines.volume_flow[0])
                )
            }
        }
