import backtrader as bt

class OnBalanceVolume(bt.Indicator):
    """
    On-Balance Volume (OBV)
    
    Ein kumulativer Indikator, der Volumen addiert oder subtrahiert basierend auf der
    Preisbewegung. Die Idee ist, dass Volumenänderungen Preisbewegungen vorausgehen.
    
    Formel:
    Wenn Schlusskurs > Vortagesschluss: OBV = Vorheriger OBV + Aktuelles Volumen
    Wenn Schlusskurs < Vortagesschluss: OBV = Vorheriger OBV - Aktuelles Volumen
    Wenn Schlusskurs = Vortagesschluss: OBV = Vorheriger OBV
    
    Parameter:
    - movav (None): Optional, Moving Average Typ für Signallinie
    - movav_period (20): Periode für Moving Average
    """
    
    lines = ('obv', 'signal')
    params = (
        ('movav', None),  # Moving Average für Signallinie
        ('movav_period', 20)
    )
    
    plotlines = dict(
        obv=dict(color='green', _name='OBV'),
        signal=dict(color='red', _name='Signal')
    )
    
    def __init__(self):
        self.addminperiod(2)  # Mindestens 2 Perioden benötigt
        
    def next(self):
        if len(self) == 1:
            self.lines.obv[0] = self.data.volume[0]
            return
            
        prev_close = self.data.close[-1]
        curr_close = self.data.close[0]
        curr_volume = self.data.volume[0]
        prev_obv = self.lines.obv[-1]
        
        if curr_close > prev_close:
            self.lines.obv[0] = prev_obv + curr_volume
        elif curr_close < prev_close:
            self.lines.obv[0] = prev_obv - curr_volume
        else:
            self.lines.obv[0] = prev_obv
            
        # Optional: Berechne Signallinie
        if self.p.movav:
            self.lines.signal = self.p.movav(self.lines.obv, period=self.p.movav_period)
        else:
            self.lines.signal = bt.indicators.SMA(self.lines.obv, period=self.p.movav_period)
