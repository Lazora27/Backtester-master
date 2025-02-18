import backtrader as bt
import numpy as np

class TwiggsMoneyFlow(bt.Indicator):
    """
    Twiggs Money Flow
    
    Ein fortgeschrittener Indikator, der eine verbesserte Version
    des Money Flow Index darstellt.
    
    Features:
    - Geldflussanalyse
    - Volumenfilterung
    - Trendbestätigung
    - Divergenzanalyse
    - Signalgenerierung
    
    Parameter:
    - period (21): Analysezeitraum
    - ema_period (13): EMA-Glättungsperiode
    - volume_factor (1.0): Volumenfaktor
    """
    
    lines = ('tmf', 'smoothed_tmf',
             'volume_trend', 'price_trend',
             'divergence', 'buy_signal',
             'sell_signal')
             
    params = (
        ('period', 21),
        ('ema_period', 13),
        ('volume_factor', 1.0),
        ('min_strength', 0.3)
    )
    
    plotlines = dict(
        tmf=dict(color='blue', _name='TMF'),
        smoothed_tmf=dict(color='red', _name='Smoothed TMF'),
        volume_trend=dict(color='green', _name='Volume Trend'),
        price_trend=dict(color='purple', _name='Price Trend'),
        divergence=dict(color='orange', _name='Divergence'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(TwiggsMoneyFlow, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=self.p.period)
        
        # Historie
        self.tmf_history = []
        self.price_history = []
        self.volume_history = []
        
    def calculate_tmf(self):
        """
        Berechnet den Twiggs Money Flow.
        """
        if len(self.data) < 2:
            return 0
            
        # Typischer Preis
        typical_price = (
            self.data.high[0] + self.data.low[0] +
            self.data.close[0]
        ) / 3
        
        # Volumengewichtung
        volume = (
            self.data.volume[0] ** self.p.volume_factor
        )
        
        # Money Flow
        if typical_price > typical_price:
            money_flow = volume
        elif typical_price < typical_price:
            money_flow = -volume
        else:
            money_flow = 0
            
        # Kumulativer Money Flow
        if len(self.tmf_history) > 0:
            money_flow += self.tmf_history[-1]
            
        # Twiggs Money Flow
        if len(self.volume_history) >= self.p.period:
            total_volume = sum(
                self.volume_history[-self.p.period:]
            )
            if total_volume > 0:
                tmf = money_flow / total_volume
            else:
                tmf = 0
        else:
            tmf = 0
            
        return tmf
        
    def calculate_volume_trend(self):
        """
        Berechnet den Volumentrend.
        """
        if len(self.volume_history) < self.p.period:
            return 0
            
        # Durchschnittliches Volumen
        avg_volume = np.mean(self.volume_history[-self.p.period:])
        
        # Volumentrend
        if avg_volume > 0:
            trend = (
                self.data.volume[0] / avg_volume - 1
            )
        else:
            trend = 0
            
        return trend
        
    def calculate_price_trend(self):
        """
        Berechnet den Preistrend.
        """
        if len(self.price_history) < self.p.period:
            return 0
            
        # Preisänderung
        price_change = (
            self.data.close[0] - self.price_history[-self.p.period]
        ) / self.price_history[-self.p.period]
        
        return price_change
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und TMF.
        """
        if len(self.tmf_history) < self.p.period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.period:])
        price_low = min(self.price_history[-self.p.period:])
        
        # TMF-Hochs/-Tiefs
        tmf_high = max(self.tmf_history[-self.p.period:])
        tmf_low = min(self.tmf_history[-self.p.period:])
        
        # Bullische Divergenz
        if price_low < price_high and tmf_low > tmf_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and tmf_low < tmf_high:
            return -1
            
        return 0
        
    def next(self):
        # TMF berechnen
        self.lines.tmf[0] = self.calculate_tmf()
        self.tmf_history.append(self.lines.tmf[0])
        
        # Geglätteter TMF
        self.lines.smoothed_tmf[0] = bt.indicators.EMA(
            self.lines.tmf, period=self.p.ema_period
        )[0]
        
        # Volumentrend
        self.lines.volume_trend[0] = self.calculate_volume_trend()
        
        # Preistrend
        self.lines.price_trend[0] = self.calculate_price_trend()
        
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Historie aktualisieren
        self.price_history.append(self.data.close[0])
        self.volume_history.append(self.data.volume[0])
        
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.ema_period
        )
        for hist in [self.tmf_history, self.price_history,
                    self.volume_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.smoothed_tmf[0] > 0 and
            self.lines.volume_trend[0] > 0 and
            self.lines.price_trend[0] > 0 and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.smoothed_tmf[0] < 0 and
            self.lines.volume_trend[0] < 0 and
            self.lines.price_trend[0] < 0 and
            self.lines.divergence[0] <= 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'tmf': {
                'current': self.lines.tmf[0],
                'smoothed': self.lines.smoothed_tmf[0],
                'trend': (
                    'bullish' if self.lines.tmf[0] > 0
                    else 'bearish'
                )
            },
            'volume': {
                'trend': self.lines.volume_trend[0],
                'strength': abs(self.lines.volume_trend[0]),
                'quality': (
                    'strong' if abs(self.lines.volume_trend[0]) > 0.5
                    else 'weak'
                )
            },
            'price': {
                'trend': self.lines.price_trend[0],
                'strength': abs(self.lines.price_trend[0]),
                'momentum': (
                    'increasing' if self.lines.price_trend[0] > 0
                    else 'decreasing'
                )
            },
            'divergence': {
                'type': (
                    'bullish' if self.lines.divergence[0] > 0
                    else 'bearish' if self.lines.divergence[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.divergence[0])
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(self.lines.tmf[0]),
                'reliability': (
                    abs(self.lines.tmf[0]) *
                    abs(self.lines.volume_trend[0])
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'tmf_volatility': (
                    np.std(self.tmf_history)
                    if len(self.tmf_history) > 1
                    else 0
                ),
                'trend_risk': abs(
                    self.lines.price_trend[0] -
                    self.lines.volume_trend[0]
                )
            }
        }
