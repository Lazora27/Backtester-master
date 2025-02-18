import backtrader as bt

class SchaffTrendCycle(bt.Indicator):
    """
    Schaff Trend Cycle (STC)
    
    Ein Momentum-Oszillator, der MACD, Stochastik und einen zyklischen
    Zeitfaktor kombiniert. Entwickelt von Doug Schaff.
    
    Der Indikator:
    - Kombiniert Trend- und Momentum-Analyse
    - Reduziert Whipsaws
    - Identifiziert Trendwechsel früher
    
    Parameter:
    - fast_ma (23): Schnelle MACD-Periode
    - slow_ma (50): Langsame MACD-Periode
    - stoch_period (10): Stochastik-Periode
    - smooth1 (23): Erste Glättung
    - smooth2 (50): Zweite Glättung
    """
    
    lines = ('stc', 'signal')
    params = (
        ('fast_ma', 23),
        ('slow_ma', 50),
        ('stoch_period', 10),
        ('smooth1', 23),
        ('smooth2', 50)
    )
    
    plotlines = dict(
        stc=dict(color='darkblue', _name='STC'),
        signal=dict(color='red', _name='Signal')
    )
    
    def __init__(self):
        # MACD
        macd = bt.indicators.MACD(
            self.data0,
            period_me1=self.p.fast_ma,
            period_me2=self.p.slow_ma
        )
        
        # Erste Stochastik auf MACD
        k1 = bt.indicators.Stochastic(
            macd.macd,
            period=self.p.stoch_period
        )
        
        # Erste Glättung
        d1 = bt.indicators.EMA(k1.percK, period=self.p.smooth1)
        
        # Zweite Stochastik
        k2 = bt.indicators.Stochastic(
            d1,
            period=self.p.stoch_period,
            upperband=100.0,
            lowerband=0.0
        )
        
        # Zweite Glättung
        self.lines.stc = bt.indicators.EMA(
            k2.percK,
            period=self.p.smooth2
        )
        
        # Signallinie
        self.lines.signal = bt.indicators.EMA(
            self.lines.stc,
            period=9
        )
        
class STCZones(bt.Indicator):
    """
    STC Zonen
    
    Identifiziert verschiedene Marktzonen basierend auf dem STC.
    
    Parameter:
    - overbought (75): Überkauft-Level
    - oversold (25): Überverkauft-Level
    """
    
    lines = ('zone',)
    params = (
        ('overbought', 75),
        ('oversold', 25)
    )
    
    plotlines = dict(
        zone=dict(
            _method='bar',
            alpha=0.7,
            width=0.7,
            _fill_gt=dict(_75=0.0, color='red'),
            _fill_lt=dict(_25=0.0, color='green'),
            _fill_gt=dict(_25=0.0, color='gray')
        )
    )
    
    def __init__(self):
        # STC berechnen
        self.stc = SchaffTrendCycle(self.data0)
        
        # Zonen definieren
        self.lines.zone = bt.If(
            self.stc.stc > self.p.overbought,
            2,  # Überkauft
            bt.If(
                self.stc.stc < self.p.oversold,
                0,  # Überverkauft
                1   # Neutral
            )
        )
