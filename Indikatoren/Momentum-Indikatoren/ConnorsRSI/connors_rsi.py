import backtrader as bt

class ConnorsRSI(bt.Indicator):
    """
    Connors RSI (CRSI)
    
    Eine Variante des RSI, die drei Komponenten kombiniert:
    1. RSI des Preises
    2. RSI der Aufstiegstage (Streak)
    3. Percentile Rank der Preisänderungen
    
    Parameter:
    - rsi_period (3): Periode für den RSI
    - streak_period (2): Periode für den Streak RSI
    - rank_period (100): Periode für den Percentile Rank
    """
    
    lines = ('crsi',)
    params = (
        ('rsi_period', 3),
        ('streak_period', 2),
        ('rank_period', 100)
    )
    
    plotlines = dict(
        crsi=dict(color='blue', _name='CRSI')
    )
    
    def __init__(self):
        # 1. Preis RSI
        price_rsi = bt.indicators.RSI(
            self.data.close,
            period=self.p.rsi_period
        )
        
        # 2. Streak RSI
        # Zähle aufeinanderfolgende Up/Down Tage
        price_change = self.data.close - self.data.close(-1)
        streak = bt.indicators.StreakCounter(price_change)
        streak_rsi = bt.indicators.RSI(
            streak,
            period=self.p.streak_period
        )
        
        # 3. Percentile Rank der Preisänderungen
        rank = bt.indicators.PercentRank(
            price_change,
            period=self.p.rank_period
        )
        
        # Berechne Connors RSI als Durchschnitt der drei Komponenten
        self.lines.crsi = (price_rsi + streak_rsi + rank) / 3.0

class StreakCounter(bt.Indicator):
    """Hilfsindiktor zum Zählen aufeinanderfolgender Up/Down Tage"""
    
    lines = ('streak',)
    
    def next(self):
        current_change = self.data[0]
        if len(self) == 1:
            self.lines.streak[0] = 1 if current_change > 0 else -1
            return
            
        prev_streak = self.lines.streak[-1]
        if current_change > 0:
            self.lines.streak[0] = prev_streak + 1 if prev_streak > 0 else 1
        elif current_change < 0:
            self.lines.streak[0] = prev_streak - 1 if prev_streak < 0 else -1
        else:
            self.lines.streak[0] = 0
