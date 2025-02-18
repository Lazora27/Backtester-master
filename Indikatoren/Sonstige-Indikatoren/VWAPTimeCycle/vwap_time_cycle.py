import backtrader as bt
import numpy as np
from datetime import datetime, timedelta
from enum import Enum

class CyclePhase(Enum):
    """VWAP Zyklus-Phasen"""
    ACCUMULATION = "Accumulation"
    MARKUP = "Markup"
    DISTRIBUTION = "Distribution"
    MARKDOWN = "Markdown"

class VWAPTimeCycleIndicator(bt.Indicator):
    """
    VWAP Time Cycle Indicator
    
    Ein fortgeschrittener Indikator zur Analyse von
    zeitbasierten VWAP-Zyklen.
    
    Features:
    - Intraday VWAP-Zyklen
    - Zeitbasierte Wendepunkte
    - Volumenprofile pro Zyklus
    - Zyklusbasierte Signale
    
    Parameter:
    - cycle_length (240): Zykluslänge in Minuten
    - num_cycles (4): Anzahl der Zyklen
    - vol_threshold (1.5): Volumenschwelle
    """
    
    lines = ('cycle_vwap', 'cycle_phase', 'strength')
    params = (
        ('cycle_length', 240),  # 4 Stunden
        ('num_cycles', 4),
        ('vol_threshold', 1.5),
    )
    
    plotlines = dict(
        cycle_vwap=dict(color='blue', _name='Cycle VWAP'),
        cycle_phase=dict(color='green', _name='Phase'),
        strength=dict(color='red', _name='Strength')
    )
    
    def __init__(self):
        super(VWAPTimeCycleIndicator, self).__init__()
        
        # Zyklusdaten
        self.cycles = []
        
        # Preispuffer
        self.price_buffer = []
        self.volume_buffer = []
        
        # Zeitpuffer
        self.time_buffer = []
        
        # Zyklusstatistiken
        self.cycle_stats = {}
        
    def initialize_cycle(self, time):
        """Initialisiert einen neuen Zyklus"""
        return {
            'start_time': time,
            'end_time': time + timedelta(
                minutes=self.p.cycle_length
            ),
            'prices': [],
            'volumes': [],
            'vwap': 0,
            'phase': CyclePhase.ACCUMULATION,
            'strength': 0
        }
        
    def update_cycle_vwap(self, cycle):
        """Aktualisiert VWAP für einen Zyklus"""
        if not cycle['prices']:
            return 0
            
        prices = np.array(cycle['prices'])
        volumes = np.array(cycle['volumes'])
        
        vwap = np.average(prices, weights=volumes)
        cycle['vwap'] = vwap
        
        return vwap
        
    def determine_cycle_phase(self, cycle, current_price):
        """Bestimmt die aktuelle Zyklusphase"""
        if not cycle['prices']:
            return CyclePhase.ACCUMULATION
            
        vwap = cycle['vwap']
        start_price = cycle['prices'][0]
        
        # Preisbewegung relativ zu VWAP
        price_rel_vwap = (current_price - vwap) / vwap
        
        # Volumenanalyse
        vol_profile = np.array(cycle['volumes'])
        vol_ma = np.mean(vol_profile)
        recent_vol = np.mean(vol_profile[-5:])
        
        if price_rel_vwap > 0.01:
            if recent_vol > vol_ma * self.p.vol_threshold:
                return CyclePhase.DISTRIBUTION
            else:
                return CyclePhase.MARKUP
        elif price_rel_vwap < -0.01:
            if recent_vol > vol_ma * self.p.vol_threshold:
                return CyclePhase.ACCUMULATION
            else:
                return CyclePhase.MARKDOWN
        else:
            if recent_vol > vol_ma * self.p.vol_threshold:
                return CyclePhase.ACCUMULATION
            else:
                return CyclePhase.MARKUP
                
    def calculate_cycle_strength(self, cycle):
        """Berechnet die Stärke des Zyklus"""
        if not cycle['prices']:
            return 0
            
        # Preisbewegung
        price_range = max(cycle['prices']) - min(cycle['prices'])
        avg_price = np.mean(cycle['prices'])
        price_strength = price_range / avg_price
        
        # Volumenanalyse
        vol_profile = np.array(cycle['volumes'])
        vol_strength = (
            np.mean(vol_profile[-5:]) /
            np.mean(vol_profile)
        )
        
        # Phasenkonsistenz
        phase_changes = sum(
            1 for i in range(1, len(cycle['prices']))
            if np.sign(cycle['prices'][i] - cycle['vwap']) !=
            np.sign(cycle['prices'][i-1] - cycle['vwap'])
        )
        phase_strength = 1 - (phase_changes / len(cycle['prices']))
        
        # Kombinierte Stärke
        strength = (
            price_strength * 0.4 +
            vol_strength * 0.4 +
            phase_strength * 0.2
        )
        
        return min(1.0, strength)
        
    def next(self):
        current_time = self.data.datetime.datetime()
        current_price = self.data.close[0]
        current_volume = self.data.volume[0]
        
        # Puffer aktualisieren
        self.time_buffer.append(current_time)
        self.price_buffer.append(current_price)
        self.volume_buffer.append(current_volume)
        
        # Neuer Zyklus?
        if not self.cycles or (
            current_time >= self.cycles[-1]['end_time']
        ):
            self.cycles.append(
                self.initialize_cycle(current_time)
            )
            
            # Alte Zyklen entfernen
            if len(self.cycles) > self.p.num_cycles:
                self.cycles.pop(0)
                
        # Aktuellen Zyklus aktualisieren
        current_cycle = self.cycles[-1]
        current_cycle['prices'].append(current_price)
        current_cycle['volumes'].append(current_volume)
        
        # VWAP berechnen
        cycle_vwap = self.update_cycle_vwap(current_cycle)
        
        # Phase bestimmen
        cycle_phase = self.determine_cycle_phase(
            current_cycle,
            current_price
        )
        current_cycle['phase'] = cycle_phase
        
        # Stärke berechnen
        cycle_strength = self.calculate_cycle_strength(
            current_cycle
        )
        current_cycle['strength'] = cycle_strength
        
        # Linien aktualisieren
        self.lines.cycle_vwap[0] = cycle_vwap
        self.lines.cycle_phase[0] = cycle_phase.value
        self.lines.strength[0] = cycle_strength
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        if not self.cycles:
            return None
            
        current_cycle = self.cycles[-1]
        current_price = self.data.close[0]
        
        return {
            'cycle_analysis': {
                'current_phase': current_cycle['phase'].value,
                'strength': current_cycle['strength'],
                'completion': (
                    (self.data.datetime.datetime() -
                     current_cycle['start_time']).total_seconds() /
                    (self.p.cycle_length * 60)
                )
            },
            'vwap_analysis': {
                'value': current_cycle['vwap'],
                'deviation': (
                    (current_price - current_cycle['vwap']) /
                    current_cycle['vwap']
                    if current_cycle['vwap'] != 0 else 0
                ),
                'trend': (
                    'up' if current_price > current_cycle['vwap']
                    else 'down' if current_price < current_cycle['vwap']
                    else 'neutral'
                )
            },
            'volume_profile': {
                'current_relative': (
                    self.data.volume[0] /
                    np.mean(current_cycle['volumes'])
                    if current_cycle['volumes'] else 1
                ),
                'accumulation': (
                    sum(1 for v in current_cycle['volumes'][-5:]
                        if v > np.mean(current_cycle['volumes']))
                    if current_cycle['volumes'] else 0
                )
            },
            'cycle_timing': {
                'time_left': (
                    current_cycle['end_time'] -
                    self.data.datetime.datetime()
                ).total_seconds() / 60,
                'optimal_entry': (
                    current_cycle['phase'] in
                    [CyclePhase.ACCUMULATION,
                     CyclePhase.MARKDOWN] and
                    current_cycle['strength'] > 0.7
                ),
                'optimal_exit': (
                    current_cycle['phase'] in
                    [CyclePhase.DISTRIBUTION,
                     CyclePhase.MARKUP] and
                    current_cycle['strength'] > 0.7
                )
            },
            'trading_signals': {
                'primary': (
                    'strong_buy'
                    if (current_cycle['phase'] ==
                        CyclePhase.ACCUMULATION and
                        current_cycle['strength'] > 0.8)
                    else 'buy'
                    if (current_cycle['phase'] ==
                        CyclePhase.MARKUP and
                        current_cycle['strength'] > 0.6)
                    else 'strong_sell'
                    if (current_cycle['phase'] ==
                        CyclePhase.DISTRIBUTION and
                        current_cycle['strength'] > 0.8)
                    else 'sell'
                    if (current_cycle['phase'] ==
                        CyclePhase.MARKDOWN and
                        current_cycle['strength'] > 0.6)
                    else 'neutral'
                ),
                'confidence': (
                    'high' if current_cycle['strength'] > 0.8
                    else 'moderate' if current_cycle['strength'] > 0.5
                    else 'low'
                ),
                'timing': (
                    'optimal'
                    if (abs(
                        current_price - current_cycle['vwap']
                    ) / current_cycle['vwap'] > 0.01 and
                    current_cycle['strength'] > 0.7)
                    else 'suboptimal'
                    if current_cycle['strength'] > 0.5
                    else 'poor'
                )
            }
        }
