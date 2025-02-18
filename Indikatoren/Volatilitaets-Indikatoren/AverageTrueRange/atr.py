import backtrader as bt

class AverageTrueRange(bt.Indicator):
    """
    Average True Range (ATR)
    
    Ein Volatilitätsindikator, der die durchschnittliche Größe der Preisbewegungen
    über einen bestimmten Zeitraum misst. Berücksichtigt Gaps zwischen den
    Handelstagen.
    
    True Range ist der größte Wert aus:
    1. Current High - Current Low
    2. |Current High - Previous Close|
    3. |Current Low - Previous Close|
    
    ATR ist dann der gleitende Durchschnitt des True Range.
    
    Parameter:
    - period (14): Periode für den gleitenden Durchschnitt
    - movav (EMA): Typ des gleitenden Durchschnitts
    - normalize (False): Ob der ATR normalisiert werden soll (Prozent vom Preis)
    """
    
    lines = ('atr', 'normalized_atr', 'tr')
    params = (
        ('period', 14),
        ('movav', bt.indicators.EMA),
        ('normalize', False)
    )
    
    plotlines = dict(
        atr=dict(color='red', _name='ATR'),
        normalized_atr=dict(_plotskip=True),
        tr=dict(_plotskip=True)
    )
    
    def __init__(self):
        # True Range Berechnung
        self.lines.tr = tr = bt.indicators.TrueRange(self.data)
        
        # ATR Berechnung
        self.lines.atr = self.p.movav(tr, period=self.p.period)
        
        if self.p.normalize:
            # Normalisierter ATR (als Prozent vom Schlusskurs)
            self.lines.normalized_atr = (self.lines.atr / self.data.close) * 100
            
    def next(self):
        # Hier könnten zusätzliche Berechnungen oder Signale implementiert werden
        pass
        
class TrueRange(bt.Indicator):
    """
    True Range
    
    Hilfsindiktor zur Berechnung des True Range.
    """
    
    lines = ('tr',)
    
    def __init__(self):
        # Aktuelle Handelsspanne
        high_low = self.data.high - self.data.low
        
        # Gestern Schluss zu heute Hoch
        prev_close_high = abs(self.data.close(-1) - self.data.high)
        
        # Gestern Schluss zu heute Tief
        prev_close_low = abs(self.data.close(-1) - self.data.low)
        
        # True Range ist das Maximum der drei Werte
        self.lines.tr = bt.Max(high_low, prev_close_high, prev_close_low)
