import backtrader as bt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

class COTReport(bt.Indicator):
    """
    Commitment of Traders (COT) Report Indicator
    
    Erweiterte Version mit:
    - Commercials/Non-Commercials Ratio
    - Net Position Index
    - Position Change Momentum
    - Extreme Levels Detection
    - Historical Percentile Ranking
    
    Features:
    - Commercials Net Position
    - Non-Commercials Net Position
    - Small Traders Net Position
    - Open Interest Analysis
    - Position Change Velocity
    - Sentiment Score
    
    Parameter:
    - period (14): Berechnungsperiode
    - ma_period (5): Glättungsperiode
    - extreme_threshold (90): Perzentil für Extreme
    - change_threshold (0.1): Schwelle für Positionsänderungen
    """
    
    lines = ('comm_net', 'noncomm_net', 'small_net',
             'comm_ratio', 'noncomm_ratio',
             'net_position_index', 'position_momentum',
             'sentiment_score', 'extreme_signal',
             'bullish_signal', 'bearish_signal')
             
    params = (
        ('period', 14),
        ('ma_period', 5),
        ('extreme_threshold', 90),
        ('change_threshold', 0.1)
    )
    
    plotlines = dict(
        comm_net=dict(color='blue', _name='Commercial Net'),
        noncomm_net=dict(color='red', _name='Non-Commercial Net'),
        small_net=dict(color='gray', _name='Small Traders Net'),
        comm_ratio=dict(color='green', _name='Commercial Ratio'),
        noncomm_ratio=dict(color='orange', _name='Non-Commercial Ratio'),
        net_position_index=dict(color='purple', _name='Net Position Index'),
        position_momentum=dict(color='brown', _name='Position Momentum'),
        sentiment_score=dict(color='black', _name='Sentiment Score'),
        extreme_signal=dict(_name='Extreme', color='red', marker='o'),
        bullish_signal=dict(_name='Bullish', color='green', marker='^'),
        bearish_signal=dict(_name='Bearish', color='red', marker='v')
    )
    
    def __init__(self):
        super(COTReport, self).__init__()
        
        # Gleitende Durchschnitte
        self.comm_ma = bt.indicators.SMA(
            self.lines.comm_net,
            period=self.p.ma_period
        )
        self.noncomm_ma = bt.indicators.SMA(
            self.lines.noncomm_net,
            period=self.p.ma_period
        )
        
        # Historische Daten für Perzentilberechnung
        self.history = {
            'comm_net': [],
            'noncomm_net': [],
            'small_net': []
        }
        
        # Positionsänderungs-Tracking
        self.prev_comm = 0
        self.prev_noncomm = 0
        
    def calculate_net_positions(self):
        """
        Berechnet die Netto-Positionen der verschiedenen Händlergruppen.
        Simulierte Werte basierend auf Preis und Volumen.
        """
        price = self.data.close[0]
        volume = self.data.volume[0]
        
        # Commercials (typischerweise Hedger)
        comm_long = volume * 0.4 * (1 + np.sin(len(self) / 10))
        comm_short = volume * 0.4 * (1 + np.cos(len(self) / 10))
        comm_net = comm_long - comm_short
        
        # Non-Commercials (Spekulanten)
        noncomm_long = volume * 0.5 * (1 + np.cos(len(self) / 8))
        noncomm_short = volume * 0.5 * (1 + np.sin(len(self) / 8))
        noncomm_net = noncomm_long - noncomm_short
        
        # Small Traders
        small_net = -(comm_net + noncomm_net)  # Muss sich ausgleichen
        
        return comm_net, noncomm_net, small_net
        
    def calculate_ratios(self, comm_net, noncomm_net):
        """Berechnet die Verhältnisse der Händlergruppen."""
        total = abs(comm_net) + abs(noncomm_net)
        if total == 0:
            return 0.5, 0.5
            
        comm_ratio = (comm_net + total) / (2 * total)
        noncomm_ratio = (noncomm_net + total) / (2 * total)
        
        return comm_ratio, noncomm_ratio
        
    def calculate_position_momentum(self, comm_net, noncomm_net):
        """Berechnet das Momentum der Positionsänderungen."""
        comm_change = comm_net - self.prev_comm
        noncomm_change = noncomm_net - self.prev_noncomm
        
        # Aktualisiere vorherige Werte
        self.prev_comm = comm_net
        self.prev_noncomm = noncomm_net
        
        # Normalisierte Änderung (-100 bis +100)
        total_change = abs(comm_change) + abs(noncomm_change)
        if total_change == 0:
            return 0
            
        momentum = ((comm_change - noncomm_change) / total_change) * 100
        return momentum
        
    def calculate_sentiment_score(self, comm_ratio, noncomm_ratio):
        """
        Berechnet einen Sentiment Score basierend auf den Positionen.
        Score von -100 (extrem bearish) bis +100 (extrem bullish).
        """
        # Gewichtung: Commercials haben mehr Gewicht
        comm_weight = 0.6
        noncomm_weight = 0.4
        
        # Score Berechnung
        score = (
            (comm_ratio - 0.5) * 200 * comm_weight +
            (noncomm_ratio - 0.5) * 200 * noncomm_weight
        )
        
        return max(-100, min(100, score))
        
    def check_extreme_levels(self, value, history):
        """Überprüft ob ein Wert extreme Level erreicht hat."""
        if len(history) < 20:  # Mindestens 20 Datenpunkte
            return False
            
        percentile = np.percentile(history, self.p.extreme_threshold)
        return abs(value) > abs(percentile)
        
    def next(self):
        # Netto-Positionen berechnen
        comm_net, noncomm_net, small_net = self.calculate_net_positions()
        
        self.lines.comm_net[0] = comm_net
        self.lines.noncomm_net[0] = noncomm_net
        self.lines.small_net[0] = small_net
        
        # Historie aktualisieren
        self.history['comm_net'].append(comm_net)
        self.history['noncomm_net'].append(noncomm_net)
        self.history['small_net'].append(small_net)
        
        # Verhältnisse berechnen
        comm_ratio, noncomm_ratio = self.calculate_ratios(comm_net, noncomm_net)
        self.lines.comm_ratio[0] = comm_ratio * 100
        self.lines.noncomm_ratio[0] = noncomm_ratio * 100
        
        # Net Position Index (-100 bis +100)
        self.lines.net_position_index[0] = (comm_ratio - noncomm_ratio) * 100
        
        # Position Momentum
        self.lines.position_momentum[0] = self.calculate_position_momentum(
            comm_net, noncomm_net
        )
        
        # Sentiment Score
        self.lines.sentiment_score[0] = self.calculate_sentiment_score(
            comm_ratio, noncomm_ratio
        )
        
        # Extreme Signale
        if self.check_extreme_levels(comm_net, self.history['comm_net']):
            self.lines.extreme_signal[0] = self.lines.sentiment_score[0]
        else:
            self.lines.extreme_signal[0] = float('nan')
            
        # Trading Signale
        if (self.lines.sentiment_score[0] > 50 and
            self.lines.position_momentum[0] > 0):
            self.lines.bullish_signal[0] = self.data.low[0]
        else:
            self.lines.bullish_signal[0] = float('nan')
            
        if (self.lines.sentiment_score[0] < -50 and
            self.lines.position_momentum[0] < 0):
            self.lines.bearish_signal[0] = self.data.high[0]
        else:
            self.lines.bearish_signal[0] = float('nan')
