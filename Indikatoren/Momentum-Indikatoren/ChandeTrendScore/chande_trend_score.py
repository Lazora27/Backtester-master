import backtrader as bt
import numpy as np

class ChandeTrendScore(bt.Indicator):
    """
    Chande Trend Score Indicator
    
    Ein fortgeschrittener Trendstärke-Indikator basierend auf Tushar Chande's
    Trend Score Konzept mit erweiterten Funktionen.
    
    Features:
    - Multi-Timeframe Trend Score
    - Adaptive Gewichtung
    - Volumen-Integration
    - Momentum-Bestätigung
    - Trend-Qualitätsanalyse
    
    Parameter:
    - short_period (10): Kurze Analyseperiode
    - medium_period (20): Mittlere Analyseperiode
    - long_period (40): Lange Analyseperiode
    - volume_period (14): Volumen-Analyseperiode
    - threshold (30): Score-Schwelle für Signale
    """
    
    lines = ('trend_score', 'short_score', 'medium_score',
             'long_score', 'volume_score', 'quality',
             'upper_band', 'lower_band',
             'buy_signal', 'sell_signal')
             
    params = (
        ('short_period', 10),
        ('medium_period', 20),
        ('long_period', 40),
        ('volume_period', 14),
        ('threshold', 30)
    )
    
    plotlines = dict(
        trend_score=dict(color='blue', _name='Trend Score'),
        short_score=dict(color='green', _name='Short Score'),
        medium_score=dict(color='red', _name='Medium Score'),
        long_score=dict(color='purple', _name='Long Score'),
        volume_score=dict(color='orange', _name='Volume Score'),
        quality=dict(color='brown', _name='Quality'),
        upper_band=dict(color='gray', _name='Upper Band'),
        lower_band=dict(color='gray', _name='Lower Band'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(ChandeTrendScore, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.volume_sma = bt.indicators.SMA(
            self.data.volume, period=self.p.volume_period
        )
        
        # Gleitende Durchschnitte
        self.ema_short = bt.indicators.EMA(period=self.p.short_period)
        self.ema_medium = bt.indicators.EMA(period=self.p.medium_period)
        self.ema_long = bt.indicators.EMA(period=self.p.long_period)
        
        # Historie
        self.score_history = []
        self.volume_history = []
        self.quality_history = []
        
    def calculate_trend_score(self, period):
        """
        Berechnet den Trend Score für eine bestimmte Periode.
        """
        if len(self) < period:
            return 0
            
        # Preisbewegungen analysieren
        up_moves = 0
        down_moves = 0
        
        for i in range(period):
            if self.data[-i] > self.data[-i-1]:
                up_moves += 1
            elif self.data[-i] < self.data[-i-1]:
                down_moves += 1
                
        # Score berechnen (-100 bis +100)
        total_moves = up_moves + down_moves
        if total_moves == 0:
            return 0
            
        score = ((up_moves - down_moves) / total_moves) * 100
        
        return score
        
    def calculate_volume_score(self):
        """
        Berechnet den Volumen-Score.
        """
        if len(self) < self.p.volume_period:
            return 0
            
        current_volume = self.data.volume[0]
        avg_volume = self.volume_sma[0]
        
        if avg_volume == 0:
            return 0
            
        # Volumen-Trend
        volume_trend = (current_volume - avg_volume) / avg_volume
        
        # Preis-Trend
        price_trend = 1 if self.data[0] > self.data[-1] else -1
        
        # Volumen-Score (-100 bis +100)
        score = volume_trend * price_trend * 100
        
        return np.clip(score, -100, 100)
        
    def calculate_trend_quality(self):
        """
        Berechnet die Qualität des Trends.
        """
        if len(self.score_history) < self.p.medium_period:
            return 0
            
        # Trend-Konsistenz
        consistency = np.std(self.score_history)
        
        # Trend-Stärke
        strength = abs(np.mean(self.score_history))
        
        # Volumen-Bestätigung
        volume_confirm = np.mean([
            1 if s * v > 0 else -1
            for s, v in zip(
                self.score_history[-self.p.volume_period:],
                self.volume_history[-self.p.volume_period:]
            )
        ])
        
        # Qualitäts-Score (0-1)
        quality = (
            (1 / (1 + consistency)) *  # Konsistenz
            (strength / 100) *         # Stärke
            ((volume_confirm + 1) / 2) # Volumen-Bestätigung
        )
        
        return quality
        
    def next(self):
        # Trend Scores berechnen
        self.lines.short_score[0] = self.calculate_trend_score(
            self.p.short_period
        )
        self.lines.medium_score[0] = self.calculate_trend_score(
            self.p.medium_period
        )
        self.lines.long_score[0] = self.calculate_trend_score(
            self.p.long_period
        )
        
        # Volumen Score
        self.lines.volume_score[0] = self.calculate_volume_score()
        
        # Gewichteter Gesamt-Score
        self.lines.trend_score[0] = (
            self.lines.short_score[0] * 0.4 +
            self.lines.medium_score[0] * 0.4 +
            self.lines.long_score[0] * 0.2
        )
        
        # Historie aktualisieren
        self.score_history.append(self.lines.trend_score[0])
        self.volume_history.append(self.lines.volume_score[0])
        
        if len(self.score_history) > self.p.long_period:
            self.score_history.pop(0)
            self.volume_history.pop(0)
            
        # Trend-Qualität
        self.lines.quality[0] = self.calculate_trend_quality()
        self.quality_history.append(self.lines.quality[0])
        if len(self.quality_history) > self.p.medium_period:
            self.quality_history.pop(0)
            
        # Bänder
        self.lines.upper_band[0] = self.p.threshold
        self.lines.lower_band[0] = -self.p.threshold
        
        # Signal-Generierung
        # Buy Signal
        if (self.lines.trend_score[0] > self.p.threshold and
            self.lines.volume_score[0] > 0 and
            self.lines.quality[0] > 0.6):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.trend_score[0] < -self.p.threshold and
            self.lines.volume_score[0] < 0 and
            self.lines.quality[0] > 0.6):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'scores': {
                'trend': self.lines.trend_score[0],
                'components': {
                    'short': self.lines.short_score[0],
                    'medium': self.lines.medium_score[0],
                    'long': self.lines.long_score[0],
                    'volume': self.lines.volume_score[0]
                }
            },
            'quality': {
                'current': self.lines.quality[0],
                'average': np.mean(self.quality_history) if self.quality_history else 0,
                'stability': np.std(self.quality_history) if self.quality_history else 0
            },
            'trend': {
                'direction': ('up' if self.lines.trend_score[0] > 0
                            else 'down'),
                'strength': abs(self.lines.trend_score[0]),
                'consistency': (
                    1 - np.std(self.score_history) / 100
                    if self.score_history else 0
                )
            },
            'volume': {
                'confirmation': (
                    self.lines.trend_score[0] *
                    self.lines.volume_score[0] > 0
                ),
                'strength': abs(self.lines.volume_score[0]),
                'trend': ('up' if self.lines.volume_score[0] > 0
                         else 'down')
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.quality[0],
                'reliability': (
                    self.lines.quality[0] *
                    abs(self.lines.trend_score[0]) / 100
                )
            }
        }
