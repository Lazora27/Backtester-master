import backtrader as bt
import numpy as np
from enum import Enum

class DeviationState(Enum):
    """Abweichungs-Zustände"""
    EXTREME_HIGH = "Extreme High"
    HIGH = "High"
    NORMAL = "Normal"
    LOW = "Low"
    EXTREME_LOW = "Extreme Low"

class VWAPDeviationBands(bt.Indicator):
    """
    VWAP Deviation Bands Indicator
    
    Ein fortgeschrittener Indikator zur Analyse von
    Preisabweichungen vom VWAP.
    
    Features:
    - Adaptive Abweichungsbänder
    - Volumengewichtete Analyse
    - Mean-Reversion-Signale
    - Trendstärke-Messung
    - Volatilitätsanalyse
    
    Parameter:
    - period (20): VWAP-Periode
    - dev_periods (5): Abweichungsperioden
    - vol_factor (1.0): Volumenfaktor
    """
    
    lines = ('vwap', 'dev_high', 'dev_low', 'mean_dev')
    params = (
        ('period', 20),
        ('dev_periods', 5),
        ('vol_factor', 1.0),
    )
    
    plotlines = dict(
        vwap=dict(color='blue', _name='VWAP'),
        dev_high=dict(color='red', _name='Dev High'),
        dev_low=dict(color='green', _name='Dev Low'),
        mean_dev=dict(color='purple', _name='Mean Dev')
    )
    
    def __init__(self):
        super(VWAPDeviationBands, self).__init__()
        
        # Preis- und Volumenpuffer
        self.price_buffer = []
        self.volume_buffer = []
        
        # Abweichungspuffer
        self.deviation_buffer = []
        
        # VWAP-Historie
        self.vwap_history = []
        
        # Volatilitätspuffer
        self.volatility_buffer = []
        
    def calculate_vwap(self):
        """Berechnet VWAP"""
        if not self.price_buffer:
            return 0
            
        # Typische Preise
        typical_prices = [
            (p['high'] + p['low'] + p['close']) / 3
            for p in self.price_buffer
        ]
        
        # VWAP berechnen
        vwap = np.average(
            typical_prices,
            weights=self.volume_buffer
        )
        
        return vwap
        
    def calculate_deviations(self, price, vwap):
        """Berechnet Preisabweichungen"""
        if vwap == 0:
            return 0, 0, 0
            
        # Aktuelle Abweichung
        current_dev = (price - vwap) / vwap
        
        # Abweichungspuffer aktualisieren
        self.deviation_buffer.append(current_dev)
        if len(self.deviation_buffer) > self.p.dev_periods:
            self.deviation_buffer.pop(0)
            
        if not self.deviation_buffer:
            return 0, 0, 0
            
        # Mittlere Abweichung
        mean_dev = np.mean(self.deviation_buffer)
        
        # Standardabweichung der Abweichungen
        dev_std = np.std(self.deviation_buffer)
        
        # Bänder berechnen
        dev_high = mean_dev + (dev_std * self.p.vol_factor)
        dev_low = mean_dev - (dev_std * self.p.vol_factor)
        
        return dev_high, dev_low, mean_dev
        
    def calculate_volatility(self):
        """Berechnet Volatilität"""
        if len(self.price_buffer) < 2:
            return 0
            
        # True Range
        true_ranges = []
        for i in range(1, len(self.price_buffer)):
            prev = self.price_buffer[i-1]
            curr = self.price_buffer[i]
            
            true_range = max(
                curr['high'] - curr['low'],
                abs(curr['high'] - prev['close']),
                abs(curr['low'] - prev['close'])
            )
            true_ranges.append(true_range)
            
        if not true_ranges:
            return 0
            
        return np.mean(true_ranges)
        
    def get_deviation_state(self, current_dev, mean_dev, dev_std):
        """Bestimmt Abweichungszustand"""
        if current_dev > mean_dev + (2 * dev_std):
            return DeviationState.EXTREME_HIGH
        elif current_dev > mean_dev + dev_std:
            return DeviationState.HIGH
        elif current_dev < mean_dev - (2 * dev_std):
            return DeviationState.EXTREME_LOW
        elif current_dev < mean_dev - dev_std:
            return DeviationState.LOW
        else:
            return DeviationState.NORMAL
            
    def next(self):
        # Preisdaten sammeln
        price_data = {
            'high': self.data.high[0],
            'low': self.data.low[0],
            'close': self.data.close[0]
        }
        
        # Puffer aktualisieren
        self.price_buffer.append(price_data)
        self.volume_buffer.append(self.data.volume[0])
        
        if len(self.price_buffer) > self.p.period:
            self.price_buffer.pop(0)
            self.volume_buffer.pop(0)
            
        # VWAP berechnen
        vwap = self.calculate_vwap()
        
        # VWAP-Historie aktualisieren
        self.vwap_history.append(vwap)
        if len(self.vwap_history) > self.p.period:
            self.vwap_history.pop(0)
            
        # Abweichungen berechnen
        dev_high, dev_low, mean_dev = self.calculate_deviations(
            self.data.close[0],
            vwap
        )
        
        # Volatilität berechnen
        volatility = self.calculate_volatility()
        self.volatility_buffer.append(volatility)
        if len(self.volatility_buffer) > self.p.period:
            self.volatility_buffer.pop(0)
            
        # Linien aktualisieren
        self.lines.vwap[0] = vwap
        self.lines.dev_high[0] = vwap * (1 + dev_high)
        self.lines.dev_low[0] = vwap * (1 + dev_low)
        self.lines.mean_dev[0] = vwap * (1 + mean_dev)
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        current_price = self.data.close[0]
        current_vwap = self.lines.vwap[0]
        
        if current_vwap == 0:
            return None
            
        # Aktuelle Abweichung
        current_dev = (current_price - current_vwap) / current_vwap
        
        # Statistiken
        if self.deviation_buffer:
            mean_dev = np.mean(self.deviation_buffer)
            dev_std = np.std(self.deviation_buffer)
        else:
            mean_dev = 0
            dev_std = 0
            
        # Abweichungszustand
        dev_state = self.get_deviation_state(
            current_dev,
            mean_dev,
            dev_std
        )
        
        return {
            'vwap_analysis': {
                'value': current_vwap,
                'current_deviation': current_dev,
                'mean_deviation': mean_dev,
                'deviation_std': dev_std
            },
            'deviation_state': {
                'current': dev_state.value,
                'magnitude': abs(current_dev),
                'direction': (
                    'positive' if current_dev > 0
                    else 'negative' if current_dev < 0
                    else 'neutral'
                )
            },
            'volatility_analysis': {
                'current': (
                    self.volatility_buffer[-1]
                    if self.volatility_buffer else 0
                ),
                'trend': (
                    'increasing'
                    if (len(self.volatility_buffer) > 1 and
                        self.volatility_buffer[-1] >
                        self.volatility_buffer[-2])
                    else 'decreasing'
                    if (len(self.volatility_buffer) > 1 and
                        self.volatility_buffer[-1] <
                        self.volatility_buffer[-2])
                    else 'stable'
                )
            },
            'mean_reversion': {
                'probability': (
                    'high'
                    if dev_state in [
                        DeviationState.EXTREME_HIGH,
                        DeviationState.EXTREME_LOW
                    ]
                    else 'moderate'
                    if dev_state in [
                        DeviationState.HIGH,
                        DeviationState.LOW
                    ]
                    else 'low'
                ),
                'target': (
                    self.lines.mean_dev[0]
                    if dev_state != DeviationState.NORMAL
                    else None
                )
            },
            'trading_signals': {
                'primary': (
                    'strong_sell'
                    if dev_state == DeviationState.EXTREME_HIGH
                    else 'sell'
                    if dev_state == DeviationState.HIGH
                    else 'strong_buy'
                    if dev_state == DeviationState.EXTREME_LOW
                    else 'buy'
                    if dev_state == DeviationState.LOW
                    else 'neutral'
                ),
                'confidence': (
                    'high'
                    if dev_state in [
                        DeviationState.EXTREME_HIGH,
                        DeviationState.EXTREME_LOW
                    ]
                    else 'moderate'
                    if dev_state in [
                        DeviationState.HIGH,
                        DeviationState.LOW
                    ]
                    else 'low'
                ),
                'risk_level': (
                    'high'
                    if abs(current_dev) > 2 * dev_std
                    else 'moderate'
                    if abs(current_dev) > dev_std
                    else 'low'
                )
            },
            'volume_profile': {
                'current_relative': (
                    self.data.volume[0] /
                    np.mean(self.volume_buffer)
                    if self.volume_buffer else 1
                ),
                'trend': (
                    'increasing'
                    if (len(self.volume_buffer) > 1 and
                        self.volume_buffer[-1] >
                        np.mean(self.volume_buffer[:-1]))
                    else 'decreasing'
                    if (len(self.volume_buffer) > 1 and
                        self.volume_buffer[-1] <
                        np.mean(self.volume_buffer[:-1]))
                    else 'stable'
                )
            }
        }
