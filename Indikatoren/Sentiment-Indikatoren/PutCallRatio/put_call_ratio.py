import backtrader as bt
import numpy as np
from datetime import datetime, timedelta

class PutCallRatio(bt.Indicator):
    """
    Put-Call Ratio Indicator
    
    Erweiterte Version mit:
    - Volume-Weighted PCR
    - Open Interest Analysis
    - Multi-Timeframe PCR
    - Sentiment Extremes
    - Options Flow Integration
    
    Features:
    - Standard Put-Call Ratio
    - Volume-Weighted PCR
    - Open Interest PCR
    - PCR Momentum
    - Extreme Detection
    
    Parameter:
    - period (14): Basisperiode für Berechnungen
    - smooth_period (5): Glättungsperiode
    - volume_period (10): Volumen-Analyse Periode
    - extreme_threshold (2.0): Schwelle für Extreme
    - momentum_period (5): Momentum Periode
    """
    
    lines = ('pcr', 'pcr_volume', 'pcr_oi',
             'pcr_momentum', 'pcr_ma',
             'extreme_signal', 'bullish_signal',
             'bearish_signal', 'flow_signal')
             
    params = (
        ('period', 14),
        ('smooth_period', 5),
        ('volume_period', 10),
        ('extreme_threshold', 2.0),
        ('momentum_period', 5)
    )
    
    plotlines = dict(
        pcr=dict(color='blue', _name='Put-Call Ratio'),
        pcr_volume=dict(color='red', _name='Volume PCR'),
        pcr_oi=dict(color='green', _name='OI PCR'),
        pcr_momentum=dict(color='purple', _name='PCR Momentum'),
        pcr_ma=dict(color='orange', _name='PCR MA'),
        extreme_signal=dict(_name='Extreme', color='red', marker='o'),
        bullish_signal=dict(_name='Bullish', color='green', marker='^'),
        bearish_signal=dict(_name='Bearish', color='red', marker='v'),
        flow_signal=dict(_name='Flow', color='blue', marker='s')
    )
    
    def __init__(self):
        super(PutCallRatio, self).__init__()
        
        # Gleitende Durchschnitte
        self.sma = bt.indicators.SMA(
            self.lines.pcr,
            period=self.p.smooth_period
        )
        
        # Momentum
        self.roc = bt.indicators.RateOfChange(
            self.lines.pcr,
            period=self.p.momentum_period
        )
        
        # Volumen MA
        self.volume_ma = bt.indicators.SMA(
            self.data.volume,
            period=self.p.volume_period
        )
        
        # Historie für Extremwerte
        self.pcr_history = []
        self.volume_history = []
        
    def simulate_options_data(self):
        """
        Simuliert Options-Daten basierend auf Preis und Volumen.
        Returns: (put_volume, call_volume, put_oi, call_oi)
        """
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        # Basis-Verteilung
        base_ratio = 0.6 + 0.2 * np.sin(len(self) / 10)
        
        # Put/Call Volumen
        total_options_volume = volume * 0.4  # 40% des Aktienvolumens
        put_volume = total_options_volume * base_ratio
        call_volume = total_options_volume * (1 - base_ratio)
        
        # Put/Call Open Interest
        total_oi = volume * 2  # Simuliertes Open Interest
        put_oi = total_oi * (base_ratio + 0.1 * np.cos(len(self) / 20))
        call_oi = total_oi * (1 - base_ratio + 0.1 * np.sin(len(self) / 20))
        
        return put_volume, call_volume, put_oi, call_oi
        
    def calculate_volume_weighted_pcr(self, put_volume, call_volume):
        """Berechnet das volumengewichtete Put-Call Ratio."""
        if call_volume == 0:
            return 1.0
            
        # Volumen-Gewichtung
        volume_factor = (
            self.data.volume[0] / self.volume_ma[0]
            if self.volume_ma[0] != 0 else 1.0
        )
        
        return (put_volume / call_volume) * volume_factor
        
    def calculate_oi_pcr(self, put_oi, call_oi):
        """Berechnet das Open Interest Put-Call Ratio."""
        if call_oi == 0:
            return 1.0
            
        return put_oi / call_oi
        
    def calculate_pcr_momentum(self):
        """Berechnet das PCR Momentum."""
        if len(self.pcr_history) < 2:
            return 0
            
        # Momentum über mehrere Perioden
        short_ma = np.mean(self.pcr_history[-5:])
        long_ma = np.mean(self.pcr_history[-20:])
        
        return ((short_ma / long_ma) - 1) * 100
        
    def detect_options_flow(self, put_volume, call_volume):
        """
        Erkennt signifikante Options-Flow Bewegungen.
        Returns: 1 (Bullish Flow), -1 (Bearish Flow), 0 (Neutral)
        """
        if len(self.volume_history) < 20:
            return 0
            
        # Durchschnittliches Options-Volumen
        avg_volume = np.mean(self.volume_history)
        current_volume = put_volume + call_volume
        
        # Volume Spike Check
        if current_volume > avg_volume * 2:
            if call_volume > put_volume * 1.5:
                return 1  # Bullish Flow
            elif put_volume > call_volume * 1.5:
                return -1  # Bearish Flow
                
        return 0  # Neutral
        
    def next(self):
        # Options-Daten simulieren
        put_volume, call_volume, put_oi, call_oi = self.simulate_options_data()
        
        # Standard PCR
        if call_volume != 0:
            self.lines.pcr[0] = put_volume / call_volume
        else:
            self.lines.pcr[0] = 1.0
            
        # Volumen-gewichtetes PCR
        self.lines.pcr_volume[0] = self.calculate_volume_weighted_pcr(
            put_volume, call_volume
        )
        
        # Open Interest PCR
        self.lines.pcr_oi[0] = self.calculate_oi_pcr(put_oi, call_oi)
        
        # Historie aktualisieren
        self.pcr_history.append(self.lines.pcr[0])
        self.volume_history.append(put_volume + call_volume)
        
        if len(self.pcr_history) > self.p.period:
            self.pcr_history.pop(0)
        if len(self.volume_history) > self.p.period:
            self.volume_history.pop(0)
            
        # PCR Momentum
        self.lines.pcr_momentum[0] = self.calculate_pcr_momentum()
        
        # Gleitender Durchschnitt
        self.lines.pcr_ma[0] = self.sma[0]
        
        # Signale generieren
        # Extreme Signale
        if self.lines.pcr[0] > self.p.extreme_threshold:
            self.lines.extreme_signal[0] = self.data.high[0]
            self.lines.bearish_signal[0] = float('nan')
        elif self.lines.pcr[0] < 1/self.p.extreme_threshold:
            self.lines.extreme_signal[0] = self.data.low[0]
            self.lines.bullish_signal[0] = float('nan')
        else:
            self.lines.extreme_signal[0] = float('nan')
            
            # Bullish/Bearish Signale nur außerhalb von Extremen
            if (self.lines.pcr[0] < self.lines.pcr_ma[0] and
                self.lines.pcr_momentum[0] < 0):
                self.lines.bullish_signal[0] = self.data.low[0]
            else:
                self.lines.bullish_signal[0] = float('nan')
                
            if (self.lines.pcr[0] > self.lines.pcr_ma[0] and
                self.lines.pcr_momentum[0] > 0):
                self.lines.bearish_signal[0] = self.data.high[0]
            else:
                self.lines.bearish_signal[0] = float('nan')
                
        # Options Flow Signal
        flow = self.detect_options_flow(put_volume, call_volume)
        if flow != 0:
            self.lines.flow_signal[0] = (
                self.data.low[0] if flow == 1 else self.data.high[0]
            )
        else:
            self.lines.flow_signal[0] = float('nan')
