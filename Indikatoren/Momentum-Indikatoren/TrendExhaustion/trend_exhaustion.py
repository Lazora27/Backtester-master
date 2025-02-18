import backtrader as bt
import numpy as np

class TrendExhaustion(bt.Indicator):
    """
    Trend Exhaustion Indicator
    
    Ein fortgeschrittener Indikator zur Erkennung von
    Trenderschöpfung und potenziellen Trendwendepunkten.
    
    Features:
    - Momentum-Analyse
    - Volumen-Bestätigung
    - Erschöpfungserkennung
    - Divergenz-Detektion
    - Signal-Validierung
    
    Parameter:
    - period (14): Basisperiode
    - volume_period (10): Volumenperiode
    - momentum_period (5): Momentumperiode
    - exhaustion_threshold (0.7): Erschöpfungsschwelle
    """
    
    lines = ('exhaustion', 'momentum',
             'volume_trend', 'divergence',
             'upper', 'lower', 'mid',
             'buy_signal', 'sell_signal')
             
    params = (
        ('period', 14),
        ('volume_period', 10),
        ('momentum_period', 5),
        ('exhaustion_threshold', 0.7),
        ('upper_threshold', 80),
        ('lower_threshold', 20)
    )
    
    plotlines = dict(
        exhaustion=dict(color='blue', _name='Exhaustion'),
        momentum=dict(color='red', _name='Momentum'),
        volume_trend=dict(color='green', _name='Volume Trend'),
        divergence=dict(color='purple', _name='Divergence'),
        upper=dict(color='gray', _name='Upper'),
        lower=dict(color='gray', _name='Lower'),
        mid=dict(color='gray', _name='Mid'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(TrendExhaustion, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.rsi = bt.indicators.RSI(period=self.p.period)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Historie
        self.exhaustion_history = []
        self.momentum_history = []
        self.price_history = []
        self.volume_history = []
        
    def calculate_exhaustion(self):
        """
        Berechnet den Erschöpfungswert.
        """
        if len(self.price_history) < self.p.period:
            return 50
            
        # Momentum-Komponente
        momentum = self.calculate_momentum()
        
        # Volumen-Komponente
        volume_trend = self.calculate_volume_trend()
        
        # RSI-Komponente
        rsi = self.rsi[0]
        
        # Erschöpfungswert
        if momentum > 0:
            exhaustion = (
                100 - ((100 - rsi) * (1 + abs(momentum)))
            ) * (1 + volume_trend)
        else:
            exhaustion = (
                rsi * (1 + abs(momentum))
            ) * (1 + volume_trend)
            
        return min(100, max(0, exhaustion))
        
    def calculate_momentum(self):
        """
        Berechnet den Momentum-Wert.
        """
        if len(self.price_history) < self.p.momentum_period:
            return 0
            
        # Preisänderung
        price_change = (
            self.price_history[-1] -
            self.price_history[-self.p.momentum_period]
        )
        
        # Relative Änderung
        if self.price_history[-self.p.momentum_period] != 0:
            return price_change / self.price_history[-self.p.momentum_period]
        return 0
        
    def calculate_volume_trend(self):
        """
        Berechnet den Volumentrend.
        """
        if len(self.volume_history) < self.p.volume_period:
            return 0
            
        # Volumenänderung
        current_vol = np.mean(self.volume_history[-self.p.momentum_period:])
        prev_vol = np.mean(
            self.volume_history[
                -self.p.volume_period:-self.p.momentum_period
            ]
        )
        
        if prev_vol == 0:
            return 0
            
        return (current_vol - prev_vol) / prev_vol
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und Erschöpfung.
        """
        if len(self.price_history) < self.p.period or len(self.exhaustion_history) < self.p.period:
            return 0
            
        # Preishochs/-tiefs
        price_high = max(self.price_history[-self.p.period:])
        price_low = min(self.price_history[-self.p.period:])
        
        # Erschöpfungs-Hochs/-Tiefs
        exhaustion_high = max(self.exhaustion_history[-self.p.period:])
        exhaustion_low = min(self.exhaustion_history[-self.p.period:])
        
        # Bullische Divergenz
        if price_low < price_high and exhaustion_low > exhaustion_high:
            return 1
            
        # Bärische Divergenz
        if price_low > price_high and exhaustion_low < exhaustion_high:
            return -1
            
        return 0
        
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.data[0])
        self.volume_history.append(self.data.volume[0])
        
        # Erschöpfung berechnen
        self.lines.exhaustion[0] = self.calculate_exhaustion()
        self.exhaustion_history.append(self.lines.exhaustion[0])
        
        # Momentum
        self.lines.momentum[0] = self.calculate_momentum()
        self.momentum_history.append(self.lines.momentum[0])
        
        # Volumentrend
        self.lines.volume_trend[0] = self.calculate_volume_trend()
        
        # Divergenz
        self.lines.divergence[0] = self.detect_divergence()
        
        # Bänder
        self.lines.upper[0] = self.p.upper_threshold
        self.lines.lower[0] = self.p.lower_threshold
        self.lines.mid[0] = 50
        
        # Historie begrenzen
        max_period = max(
            self.p.period,
            self.p.volume_period,
            self.p.momentum_period
        )
        for hist in [
            self.exhaustion_history,
            self.momentum_history,
            self.price_history,
            self.volume_history
        ]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.exhaustion[0] < self.p.lower_threshold and
            self.lines.momentum[0] > 0 and
            self.lines.volume_trend[0] > 0 and
            self.lines.divergence[0] >= 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.exhaustion[0] > self.p.upper_threshold and
            self.lines.momentum[0] < 0 and
            self.lines.volume_trend[0] < 0 and
            self.lines.divergence[0] <= 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'exhaustion': {
                'value': self.lines.exhaustion[0],
                'momentum': self.lines.momentum[0],
                'volume_trend': self.lines.volume_trend[0],
                'divergence': self.lines.divergence[0]
            },
            'trend': {
                'direction': np.sign(self.lines.momentum[0]),
                'strength': abs(self.lines.momentum[0]),
                'exhaustion_level': (
                    'high' if self.lines.exhaustion[0] > self.p.upper_threshold
                    else 'low' if self.lines.exhaustion[0] < self.p.lower_threshold
                    else 'normal'
                )
            },
            'volume': {
                'trend': self.lines.volume_trend[0],
                'confirmation': (
                    self.lines.volume_trend[0] > 0 and
                    self.lines.momentum[0] > 0
                ) or (
                    self.lines.volume_trend[0] < 0 and
                    self.lines.momentum[0] < 0
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
                'strength': abs(self.lines.momentum[0]),
                'reliability': (
                    abs(self.lines.momentum[0]) *
                    (1 + abs(self.lines.volume_trend[0])) *
                    (1 + abs(self.lines.divergence[0]))
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'exhaustion_stability': (
                    np.std(self.exhaustion_history)
                    if len(self.exhaustion_history) > 1
                    else 0
                ),
                'momentum_stability': (
                    np.std(self.momentum_history)
                    if len(self.momentum_history) > 1
                    else 0
                )
            }
        }
