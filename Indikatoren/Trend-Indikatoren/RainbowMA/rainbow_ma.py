import backtrader as bt
import numpy as np

class RainbowMovingAverage(bt.Indicator):
    """
    Rainbow Moving Average Indicator
    
    Ein fortgeschrittener Trendfolge-Indikator, der multiple gleitende
    Durchschnitte mit verschiedenen Perioden kombiniert.
    
    Features:
    - Multiple MA Berechnung
    - Gewichtete Trend-Analyse
    - Adaptive Bandbreite
    - Trend-Stärke Berechnung
    - Multi-Timeframe Signale
    
    Parameter:
    - ma_periods (None): Liste der MA Perioden
    - ma_type ('ema'): Typ der MAs ('sma', 'ema', 'wma')
    - weight_type ('linear'): Gewichtungstyp ('linear', 'exponential')
    - threshold (0.5): Signal-Schwelle
    """
    
    lines = ('rainbow', 'ma1', 'ma2', 'ma3', 'ma4',
             'ma5', 'ma6', 'ma7', 'ma8',
             'trend_strength', 'bandwidth',
             'buy_signal', 'sell_signal')
             
    params = (
        ('ma_periods', [10, 15, 20, 25, 30, 35, 40, 45]),
        ('ma_type', 'ema'),
        ('weight_type', 'linear'),
        ('threshold', 0.5)
    )
    
    plotlines = dict(
        rainbow=dict(color='blue', _name='Rainbow MA'),
        ma1=dict(color='red', _name='MA1'),
        ma2=dict(color='orange', _name='MA2'),
        ma3=dict(color='yellow', _name='MA3'),
        ma4=dict(color='green', _name='MA4'),
        ma5=dict(color='cyan', _name='MA5'),
        ma6=dict(color='blue', _name='MA6'),
        ma7=dict(color='purple', _name='MA7'),
        ma8=dict(color='gray', _name='MA8'),
        trend_strength=dict(color='brown', _name='Trend Strength'),
        bandwidth=dict(color='gray', _name='Bandwidth'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(RainbowMovingAverage, self).__init__()
        
        # Moving Averages initialisieren
        self.mas = []
        for period in self.p.ma_periods:
            if self.p.ma_type == 'ema':
                ma = bt.indicators.EMA(period=period)
            elif self.p.ma_type == 'wma':
                ma = bt.indicators.WMA(period=period)
            else:  # default to SMA
                ma = bt.indicators.SMA(period=period)
            self.mas.append(ma)
            
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        
        # Historie
        self.rainbow_history = []
        self.strength_history = []
        
    def calculate_weights(self):
        """
        Berechnet die Gewichte für die Moving Averages.
        """
        n = len(self.p.ma_periods)
        
        if self.p.weight_type == 'exponential':
            weights = [2 ** i for i in range(n)]
        else:  # linear
            weights = list(range(1, n + 1))
            
        # Normalisierung
        total = sum(weights)
        weights = [w / total for w in weights]
        
        return weights
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke basierend auf MA-Alignment.
        """
        if len(self.mas) < 2:
            return 0
            
        # MA Alignment prüfen
        alignments = []
        for i in range(len(self.mas)-1):
            for j in range(i+1, len(self.mas)):
                alignment = 1 if self.mas[i][0] > self.mas[j][0] else -1
                alignments.append(alignment)
                
        # Konsistenz der Alignments (-1 bis 1)
        if not alignments:
            return 0
            
        strength = abs(sum(alignments) / len(alignments))
        
        return strength
        
    def calculate_bandwidth(self):
        """
        Berechnet die Bandbreite zwischen den MAs.
        """
        if not self.mas:
            return 0
            
        values = [ma[0] for ma in self.mas]
        bandwidth = max(values) - min(values)
        
        # Normalisierung
        if self.data[0] != 0:
            bandwidth = bandwidth / self.data[0]
            
        return bandwidth
        
    def next(self):
        # MA Werte aktualisieren
        for i, ma in enumerate(self.mas):
            setattr(self.lines, f'ma{i+1}', ma[0])
            
        # Gewichteter Rainbow MA
        weights = self.calculate_weights()
        self.lines.rainbow[0] = sum(
            ma[0] * w for ma, w in zip(self.mas, weights)
        )
        
        # Trendstärke
        self.lines.trend_strength[0] = self.calculate_trend_strength()
        
        # Bandbreite
        self.lines.bandwidth[0] = self.calculate_bandwidth()
        
        # Historie aktualisieren
        self.rainbow_history.append(self.lines.rainbow[0])
        self.strength_history.append(self.lines.trend_strength[0])
        
        max_history = max(self.p.ma_periods)
        if len(self.rainbow_history) > max_history:
            self.rainbow_history.pop(0)
            self.strength_history.pop(0)
            
        # Signal-Generierung
        # Buy Signal
        if (self.lines.trend_strength[0] > self.p.threshold and
            all(self.data[0] > ma[0] for ma in self.mas) and
            self.lines.bandwidth[0] < 0.1):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.trend_strength[0] > self.p.threshold and
            all(self.data[0] < ma[0] for ma in self.mas) and
            self.lines.bandwidth[0] < 0.1):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'rainbow': {
                'value': self.lines.rainbow[0],
                'bandwidth': self.lines.bandwidth[0],
                'mas': {
                    f'ma{i+1}': getattr(self.lines, f'ma{i+1}')[0]
                    for i in range(len(self.mas))
                }
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': ('up' if self.data[0] > self.lines.rainbow[0]
                            else 'down'),
                'quality': (
                    'high' if self.lines.trend_strength[0] > 0.8
                    else 'medium' if self.lines.trend_strength[0] > 0.5
                    else 'low'
                )
            },
            'alignment': {
                'bullish': all(
                    ma1[0] > ma2[0]
                    for ma1, ma2 in zip(self.mas[:-1], self.mas[1:])
                ),
                'bearish': all(
                    ma1[0] < ma2[0]
                    for ma1, ma2 in zip(self.mas[:-1], self.mas[1:])
                ),
                'neutral': not (
                    all(ma1[0] > ma2[0] for ma1, ma2 in zip(self.mas[:-1], self.mas[1:])) or
                    all(ma1[0] < ma2[0] for ma1, ma2 in zip(self.mas[:-1], self.mas[1:]))
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    self.lines.trend_strength[0] *
                    (1 - self.lines.bandwidth[0])
                )
            },
            'risk': {
                'volatility': self.atr[0] / self.data[0] if self.data[0] != 0 else 0,
                'ma_spread': self.lines.bandwidth[0],
                'trend_stability': np.std(self.strength_history) if self.strength_history else 0
            }
        }
