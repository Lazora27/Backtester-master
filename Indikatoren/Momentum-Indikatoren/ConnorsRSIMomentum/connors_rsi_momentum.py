import backtrader as bt
import numpy as np

class ConnorsRSIMomentum(bt.Indicator):
    """
    Connors RSI Momentum Indicator
    
    Eine erweiterte Version des Connors RSI mit zusätzlichen
    Momentum-Komponenten und Marktanalyse.
    
    Features:
    - Dreifache RSI Berechnung
    - Streak-RSI Integration
    - Percentile Rank Analyse
    - Momentum-Bestätigung
    - Adaptive Signalgenerierung
    
    Parameter:
    - rsi_period (3): RSI Basisperiode
    - streak_period (2): Streak RSI Periode
    - rank_period (100): Percentile Rank Periode
    - smooth_period (10): Glättungsperiode
    """
    
    lines = ('crsi', 'streak_rsi', 'rank_rsi',
             'momentum', 'signal_line',
             'overbought', 'oversold',
             'buy_signal', 'sell_signal')
             
    params = (
        ('rsi_period', 3),
        ('streak_period', 2),
        ('rank_period', 100),
        ('smooth_period', 10)
    )
    
    plotlines = dict(
        crsi=dict(color='blue', _name='CRSI'),
        streak_rsi=dict(color='green', _name='Streak RSI'),
        rank_rsi=dict(color='red', _name='Rank RSI'),
        momentum=dict(color='purple', _name='Momentum'),
        signal_line=dict(color='orange', _name='Signal'),
        overbought=dict(_name='Overbought', color='gray'),
        oversold=dict(_name='Oversold', color='gray'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(ConnorsRSIMomentum, self).__init__()
        
        # Basis RSI
        self.rsi = bt.indicators.RSI(
            period=self.p.rsi_period,
            movav=bt.indicators.ExponentialMovingAverage
        )
        
        # Glättung
        self.smooth = bt.indicators.EMA(period=self.p.smooth_period)
        
        # Historie
        self.price_history = []
        self.streak_history = []
        self.rank_history = []
        self.current_streak = 0
        
    def calculate_streak_rsi(self):
        """
        Berechnet den Streak-basierten RSI.
        """
        if len(self) < 2:
            return 50
            
        # Streak aktualisieren
        if self.data[0] > self.data[-1]:
            if self.current_streak < 0:
                self.current_streak = 1
            else:
                self.current_streak += 1
        elif self.data[0] < self.data[-1]:
            if self.current_streak > 0:
                self.current_streak = -1
            else:
                self.current_streak -= 1
                
        # Streak RSI berechnen
        if len(self.streak_history) < self.p.streak_period:
            return 50
            
        positive_streaks = sum(1 for x in self.streak_history if x > 0)
        negative_streaks = sum(1 for x in self.streak_history if x < 0)
        
        if negative_streaks == 0:
            return 100
        elif positive_streaks == 0:
            return 0
            
        rs = positive_streaks / negative_streaks
        streak_rsi = 100 - (100 / (1 + rs))
        
        return streak_rsi
        
    def calculate_rank_rsi(self):
        """
        Berechnet den Percentile Rank RSI.
        """
        if len(self.price_history) < self.p.rank_period:
            return 50
            
        current_close = self.data[0]
        rank = sum(1 for x in self.price_history
                  if current_close > x)
                  
        percentile = (rank / len(self.price_history)) * 100
        
        return percentile
        
    def calculate_momentum(self):
        """
        Berechnet die Momentum-Komponente.
        """
        if len(self) < self.p.rsi_period:
            return 0
            
        # Preisänderung
        price_change = (
            self.data[0] - self.data[-self.p.rsi_period]
        ) / self.data[-self.p.rsi_period] if self.data[-self.p.rsi_period] != 0 else 0
        
        # RSI Änderung
        rsi_change = self.rsi[0] - self.rsi[-self.p.rsi_period]
        
        # Kombiniertes Momentum (-1 bis 1)
        momentum = np.tanh((price_change + rsi_change / 100) / 2)
        
        return momentum
        
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.data[0])
        self.streak_history.append(self.current_streak)
        
        if len(self.price_history) > self.p.rank_period:
            self.price_history.pop(0)
        if len(self.streak_history) > self.p.streak_period:
            self.streak_history.pop(0)
            
        # Komponenten berechnen
        streak_rsi = self.calculate_streak_rsi()
        rank_rsi = self.calculate_rank_rsi()
        
        # Connors RSI
        self.lines.crsi[0] = (
            self.rsi[0] +
            streak_rsi +
            rank_rsi
        ) / 3
        
        self.lines.streak_rsi[0] = streak_rsi
        self.lines.rank_rsi[0] = rank_rsi
        
        # Momentum
        self.lines.momentum[0] = self.calculate_momentum()
        
        # Signal-Linie
        self.lines.signal_line[0] = self.smooth(self.lines.crsi)
        
        # Overbought/Oversold
        self.lines.overbought[0] = 80
        self.lines.oversold[0] = 20
        
        # Signal-Generierung
        # Buy Signal
        if (self.lines.crsi[0] < self.lines.oversold[0] and
            self.lines.momentum[0] > 0 and
            self.lines.crsi[0] > self.lines.crsi[-1]):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.crsi[0] > self.lines.overbought[0] and
            self.lines.momentum[0] < 0 and
            self.lines.crsi[0] < self.lines.crsi[-1]):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'crsi': {
                'value': self.lines.crsi[0],
                'signal': self.lines.signal_line[0],
                'components': {
                    'rsi': self.rsi[0],
                    'streak': self.lines.streak_rsi[0],
                    'rank': self.lines.rank_rsi[0]
                }
            },
            'momentum': {
                'value': self.lines.momentum[0],
                'direction': ('up' if self.lines.momentum[0] > 0
                            else 'down'),
                'strength': abs(self.lines.momentum[0])
            },
            'conditions': {
                'overbought': self.lines.crsi[0] > self.lines.overbought[0],
                'oversold': self.lines.crsi[0] < self.lines.oversold[0],
                'trend': ('up' if self.lines.crsi[0] > self.lines.signal_line[0]
                         else 'down')
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(self.lines.crsi[0] - 50) / 50,
                'reliability': (
                    abs(self.lines.momentum[0]) *
                    (1 - abs(self.lines.crsi[0] - 50) / 50)
                )
            },
            'streaks': {
                'current': self.current_streak,
                'average': np.mean(self.streak_history) if self.streak_history else 0,
                'distribution': {
                    'positive': sum(1 for x in self.streak_history if x > 0),
                    'negative': sum(1 for x in self.streak_history if x < 0)
                }
            }
        }
