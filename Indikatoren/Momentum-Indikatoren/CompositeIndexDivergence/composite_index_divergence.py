import backtrader as bt
import numpy as np

class CompositeIndexDivergence(bt.Indicator):
    """
    Composite Index Divergence Indicator
    
    Ein fortgeschrittener Momentum-Indikator, der mehrere technische Indikatoren
    kombiniert, um Divergenzen zu identifizieren.
    
    Features:
    - Multi-Indikator Komposition
    - Divergenz-Erkennung
    - Adaptive Gewichtung
    - Momentum-Analyse
    - Signal-Validierung
    
    Parameter:
    - rsi_period (14): RSI Periode
    - macd_fast (12): MACD schnelle Periode
    - macd_slow (26): MACD langsame Periode
    - macd_signal (9): MACD Signal Periode
    - stoch_period (14): Stochastic Periode
    - div_lookback (20): Divergenz Lookback Periode
    """
    
    lines = ('composite', 'divergence', 'signal',
             'rsi_component', 'macd_component', 'stoch_component',
             'buy_signal', 'sell_signal')
             
    params = (
        ('rsi_period', 14),
        ('macd_fast', 12),
        ('macd_slow', 26),
        ('macd_signal', 9),
        ('stoch_period', 14),
        ('div_lookback', 20)
    )
    
    plotlines = dict(
        composite=dict(color='blue', _name='Composite'),
        divergence=dict(color='red', _name='Divergence'),
        signal=dict(color='green', _name='Signal'),
        rsi_component=dict(color='orange', _name='RSI Comp'),
        macd_component=dict(color='purple', _name='MACD Comp'),
        stoch_component=dict(color='cyan', _name='Stoch Comp'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(CompositeIndexDivergence, self).__init__()
        
        # Basis-Indikatoren
        self.rsi = bt.indicators.RSI(period=self.p.rsi_period)
        self.macd = bt.indicators.MACD(
            period_me1=self.p.macd_fast,
            period_me2=self.p.macd_slow,
            period_signal=self.p.macd_signal
        )
        self.stoch = bt.indicators.Stochastic(period=self.p.stoch_period)
        
        # Historie
        self.price_history = []
        self.composite_history = []
        self.peaks = []
        self.troughs = []
        
    def normalize(self, value, min_val, max_val):
        """
        Normalisiert einen Wert zwischen -1 und 1.
        """
        if max_val == min_val:
            return 0
        return 2 * ((value - min_val) / (max_val - min_val)) - 1
        
    def find_extrema(self, data, lookback):
        """
        Findet lokale Maxima und Minima.
        """
        if len(data) < lookback:
            return None, None
            
        window = data[-lookback:]
        peaks = []
        troughs = []
        
        for i in range(1, len(window)-1):
            if window[i] > window[i-1] and window[i] > window[i+1]:
                peaks.append((i, window[i]))
            if window[i] < window[i-1] and window[i] < window[i+1]:
                troughs.append((i, window[i]))
                
        return peaks, troughs
        
    def detect_divergence(self):
        """
        Erkennt Divergenzen zwischen Preis und Indikator.
        """
        if len(self.price_history) < self.p.div_lookback:
            return 0
            
        price_peaks, price_troughs = self.find_extrema(
            self.price_history, self.p.div_lookback
        )
        comp_peaks, comp_troughs = self.find_extrema(
            self.composite_history, self.p.div_lookback
        )
        
        if not all([price_peaks, price_troughs, comp_peaks, comp_troughs]):
            return 0
            
        # Bullische Divergenz
        if (price_troughs and comp_troughs and
            price_troughs[-1][1] < price_troughs[0][1] and
            comp_troughs[-1][1] > comp_troughs[0][1]):
            return 1
            
        # Bärische Divergenz
        if (price_peaks and comp_peaks and
            price_peaks[-1][1] > price_peaks[0][1] and
            comp_peaks[-1][1] < comp_peaks[0][1]):
            return -1
            
        return 0
        
    def next(self):
        # Komponenten normalisieren
        rsi_norm = self.normalize(self.rsi[0], 0, 100)
        macd_norm = self.normalize(
            self.macd.macd[0],
            min(self.macd.macd.get(size=30)),
            max(self.macd.macd.get(size=30))
        )
        stoch_norm = self.normalize(self.stoch[0], 0, 100)
        
        # Komponenten speichern
        self.lines.rsi_component[0] = rsi_norm
        self.lines.macd_component[0] = macd_norm
        self.lines.stoch_component[0] = stoch_norm
        
        # Composite Index berechnen
        self.lines.composite[0] = (
            0.4 * rsi_norm +
            0.4 * macd_norm +
            0.2 * stoch_norm
        )
        
        # Historie aktualisieren
        self.price_history.append(self.data[0])
        self.composite_history.append(self.lines.composite[0])
        
        if len(self.price_history) > self.p.div_lookback:
            self.price_history.pop(0)
            self.composite_history.pop(0)
            
        # Divergenz erkennen
        self.lines.divergence[0] = self.detect_divergence()
        
        # Signal-Linie (geglätteter Composite)
        self.lines.signal[0] = bt.indicators.SMA(
            self.lines.composite, period=9
        )[0]
        
        # Signal-Generierung
        # Buy Signal
        if (self.lines.divergence[0] > 0 and
            self.lines.composite[0] < -0.5 and
            self.lines.composite[0] > self.lines.signal[0]):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.divergence[0] < 0 and
            self.lines.composite[0] > 0.5 and
            self.lines.composite[0] < self.lines.signal[0]):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'composite': {
                'value': self.lines.composite[0],
                'signal': self.lines.signal[0],
                'components': {
                    'rsi': self.lines.rsi_component[0],
                    'macd': self.lines.macd_component[0],
                    'stoch': self.lines.stoch_component[0]
                }
            },
            'divergence': {
                'current': self.lines.divergence[0],
                'type': (
                    'bullish' if self.lines.divergence[0] > 0
                    else 'bearish' if self.lines.divergence[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.divergence[0])
            },
            'momentum': {
                'direction': np.sign(self.lines.composite[0]),
                'strength': abs(self.lines.composite[0]),
                'acceleration': (
                    self.lines.composite[0] -
                    self.composite_history[-2]
                    if len(self.composite_history) > 1
                    else 0
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(self.lines.composite[0]),
                'reliability': (
                    abs(self.lines.divergence[0]) *
                    abs(self.lines.composite[0])
                )
            }
        }
