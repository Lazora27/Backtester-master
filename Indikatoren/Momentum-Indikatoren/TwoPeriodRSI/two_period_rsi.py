import backtrader as bt
import numpy as np

class TwoPeriodRSI(bt.Indicator):
    """
    2-Period RSI Indicator
    
    Ein hochreaktiver Momentum-Indikator basierend auf Larry Connors'
    2-Perioden RSI Strategie mit erweiterten Funktionen.
    
    Features:
    - Kurzfristige Überkauft/Überverkauft Zustände
    - Momentum-Bestätigung
    - Divergenz-Erkennung
    - Adaptiver Mittelwert
    - Signal-Generierung
    
    Parameter:
    - period (2): RSI Basisperiode
    - ma_period (20): Gleitender Durchschnitt Periode
    - overbought (80): Überkauft-Schwelle
    - oversold (20): Überverkauft-Schwelle
    """
    
    lines = ('rsi', 'ma', 'divergence',
             'overbought', 'oversold',
             'buy_signal', 'sell_signal')
             
    params = (
        ('period', 2),
        ('ma_period', 20),
        ('overbought', 80),
        ('oversold', 20)
    )
    
    plotlines = dict(
        rsi=dict(color='blue', _name='2-Period RSI'),
        ma=dict(color='red', _name='MA'),
        divergence=dict(color='green', _name='Divergence'),
        overbought=dict(_name='Overbought', color='gray'),
        oversold=dict(_name='Oversold', color='gray'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(TwoPeriodRSI, self).__init__()
        
        # RSI Berechnung
        self.rsi = bt.indicators.RSI(
            self.data,
            period=self.p.period,
            movav=bt.indicators.ExponentialMovingAverage
        )
        
        # Gleitender Durchschnitt des RSI
        self.ma = bt.indicators.EMA(
            self.rsi,
            period=self.p.ma_period
        )
        
        # Historie für Divergenz
        self.price_highs = []
        self.price_lows = []
        self.rsi_highs = []
        self.rsi_lows = []
        
    def detect_divergence(self):
        """
        Erkennt bullische und bärische Divergenzen.
        """
        if len(self) < 2:
            return 0
            
        # Neue Extrema speichern
        if self.data[0] > self.data[-1]:
            self.price_highs.append(self.data[0])
            self.rsi_highs.append(self.rsi[0])
        elif self.data[0] < self.data[-1]:
            self.price_lows.append(self.data[0])
            self.rsi_lows.append(self.rsi[0])
            
        # Liste begrenzen
        max_history = 10
        if len(self.price_highs) > max_history:
            self.price_highs.pop(0)
            self.rsi_highs.pop(0)
        if len(self.price_lows) > max_history:
            self.price_lows.pop(0)
            self.rsi_lows.pop(0)
            
        # Divergenz prüfen
        if len(self.price_highs) >= 2 and len(self.price_lows) >= 2:
            # Bärische Divergenz
            if (self.price_highs[-1] > self.price_highs[-2] and
                self.rsi_highs[-1] < self.rsi_highs[-2]):
                return -1
                
            # Bullische Divergenz
            if (self.price_lows[-1] < self.price_lows[-2] and
                self.rsi_lows[-1] > self.rsi_lows[-2]):
                return 1
                
        return 0
        
    def next(self):
        # RSI und MA
        self.lines.rsi[0] = self.rsi[0]
        self.lines.ma[0] = self.ma[0]
        
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Overbought/Oversold Linien
        self.lines.overbought[0] = self.p.overbought
        self.lines.oversold[0] = self.p.oversold
        
        # Signal-Generierung
        # Buy Signal
        if (self.lines.rsi[0] < self.p.oversold and
            self.lines.rsi[0] > self.lines.rsi[-1] and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.rsi[0] > self.p.overbought and
            self.lines.rsi[0] < self.lines.rsi[-1] and
            self.lines.divergence[0] <= 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'rsi': {
                'current': self.lines.rsi[0],
                'ma': self.lines.ma[0],
                'trend': ('up' if self.lines.rsi[0] > self.lines.ma[0]
                         else 'down'),
                'condition': (
                    'overbought' if self.lines.rsi[0] > self.p.overbought
                    else 'oversold' if self.lines.rsi[0] < self.p.oversold
                    else 'neutral'
                )
            },
            'divergence': {
                'current': self.lines.divergence[0],
                'bullish': self.lines.divergence[0] > 0,
                'bearish': self.lines.divergence[0] < 0
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(
                    self.lines.rsi[0] - 50
                ) / 50,
                'momentum': self.lines.rsi[0] - self.lines.rsi[-1]
            },
            'analysis': {
                'volatility': np.std([
                    self.lines.rsi[i] for i in range(-5, 1)
                ]) if len(self) > 5 else 0,
                'trend_quality': (
                    'strong' if abs(self.lines.rsi[0] - 50) > 30
                    else 'moderate' if abs(self.lines.rsi[0] - 50) > 15
                    else 'weak'
                ),
                'reversal_potential': (
                    'high' if (
                        (self.lines.rsi[0] < self.p.oversold and
                         self.lines.divergence[0] > 0) or
                        (self.lines.rsi[0] > self.p.overbought and
                         self.lines.divergence[0] < 0)
                    )
                    else 'low'
                )
            }
        }
