import backtrader as bt
import numpy as np
from scipy import signal

class DetrendedPriceIndicator(bt.Indicator):
    """
    Detrended Price Indicator (DPI)
    
    Ein fortgeschrittener Indikator zur Identifizierung von Preiszyklen
    durch Entfernung des übergeordneten Trends.
    
    Features:
    - Klassische DPI Berechnung
    - Zyklus-Identifikation
    - Trend-Eliminierung
    - Signal-Generierung
    - Multi-Timeframe Analyse
    
    Parameter:
    - period (21): Basisperiode für Berechnung
    - ma_type ('sma'): Moving Average Typ ('sma', 'ema', 'wma')
    - cycle_period (10): Periode für Zyklus-Analyse
    - smooth_period (5): Glättungsperiode
    - threshold (0.5): Signal-Schwelle
    """
    
    lines = ('dpi', 'cycle', 'trend_removed',
             'oscillator', 'signal_line',
             'buy_signal', 'sell_signal',
             'cycle_high', 'cycle_low')
             
    params = (
        ('period', 21),
        ('ma_type', 'sma'),
        ('cycle_period', 10),
        ('smooth_period', 5),
        ('threshold', 0.5)
    )
    
    plotlines = dict(
        dpi=dict(color='blue', _name='DPI'),
        cycle=dict(color='green', _name='Cycle'),
        trend_removed=dict(color='red', _name='Detrended'),
        oscillator=dict(color='purple', _name='Oscillator'),
        signal_line=dict(color='orange', _name='Signal'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v'),
        cycle_high=dict(_name='Cycle High', color='gray', marker='o'),
        cycle_low=dict(_name='Cycle Low', color='gray', marker='o')
    )
    
    def __init__(self):
        super(DetrendedPriceIndicator, self).__init__()
        
        # Moving Average basierend auf Typ
        if self.p.ma_type == 'ema':
            self.ma = bt.indicators.EMA(period=self.p.period)
        elif self.p.ma_type == 'wma':
            self.ma = bt.indicators.WMA(period=self.p.period)
        else:  # default to SMA
            self.ma = bt.indicators.SMA(period=self.p.period)
            
        # Glättung
        self.smooth = bt.indicators.SMA(period=self.p.smooth_period)
        
        # Historie für Zyklus-Analyse
        self.price_history = []
        self.dpi_history = []
        self.cycle_history = []
        
    def detrend_price(self):
        """
        Entfernt den Trend aus der Preisreihe.
        """
        if len(self.price_history) < self.p.period:
            return 0
            
        # Trend mit MA
        trend = self.ma[0]
        
        # Trend entfernen
        detrended = self.data[0] - trend
        
        return detrended
        
    def identify_cycles(self):
        """
        Identifiziert Preiszyklen in den detrendeten Daten.
        """
        if len(self.dpi_history) < self.p.cycle_period:
            return 0
            
        # Fourier Transform für Zyklus-Analyse
        data = np.array(self.dpi_history[-self.p.cycle_period:])
        frequencies = np.fft.fftfreq(len(data))
        fft = np.fft.fft(data)
        
        # Dominante Frequenz finden
        dominant_freq = frequencies[np.argmax(np.abs(fft))]
        
        if dominant_freq != 0:
            cycle = 1 / abs(dominant_freq)
        else:
            cycle = 0
            
        return cycle
        
    def calculate_oscillator(self):
        """
        Berechnet einen Oszillator aus dem DPI.
        """
        if len(self.dpi_history) < 2:
            return 0
            
        # Momentum des DPI
        momentum = self.lines.dpi[0] - self.lines.dpi[-1]
        
        # Normalisierung
        if len(self.dpi_history) >= self.p.period:
            max_dpi = max(self.dpi_history[-self.p.period:])
            min_dpi = min(self.dpi_history[-self.p.period:])
            range_dpi = max_dpi - min_dpi
            
            if range_dpi != 0:
                normalized = ((self.lines.dpi[0] - min_dpi) /
                            range_dpi * 2 - 1)
            else:
                normalized = 0
        else:
            normalized = 0
            
        return normalized
        
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.data[0])
        if len(self.price_history) > self.p.period * 2:
            self.price_history.pop(0)
            
        # DPI berechnen
        self.lines.dpi[0] = self.detrend_price()
        self.dpi_history.append(self.lines.dpi[0])
        if len(self.dpi_history) > self.p.period * 2:
            self.dpi_history.pop(0)
            
        # Zyklus identifizieren
        self.lines.cycle[0] = self.identify_cycles()
        self.cycle_history.append(self.lines.cycle[0])
        if len(self.cycle_history) > self.p.cycle_period:
            self.cycle_history.pop(0)
            
        # Trend entfernen
        self.lines.trend_removed[0] = (
            self.data[0] - self.ma[0]
        )
        
        # Oszillator berechnen
        self.lines.oscillator[0] = self.calculate_oscillator()
        
        # Signal Line
        self.lines.signal_line[0] = self.smooth(
            self.lines.oscillator
        )[0]
        
        # Signal-Generierung
        # Buy Signal
        if (self.lines.oscillator[0] > self.lines.signal_line[0] and
            self.lines.oscillator[0] > self.p.threshold):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.oscillator[0] < self.lines.signal_line[0] and
            self.lines.oscillator[0] < -self.p.threshold):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
        # Zyklus Highs/Lows
        if len(self.dpi_history) >= 3:
            if (self.dpi_history[-2] > self.dpi_history[-3] and
                self.dpi_history[-2] > self.dpi_history[-1]):
                self.lines.cycle_high[0] = self.data.high[0]
            else:
                self.lines.cycle_high[0] = float('nan')
                
            if (self.dpi_history[-2] < self.dpi_history[-3] and
                self.dpi_history[-2] < self.dpi_history[-1]):
                self.lines.cycle_low[0] = self.data.low[0]
            else:
                self.lines.cycle_low[0] = float('nan')
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'detrended': {
                'value': self.lines.dpi[0],
                'trend_removed': self.lines.trend_removed[0],
                'oscillator': self.lines.oscillator[0]
            },
            'cycles': {
                'current': self.lines.cycle[0],
                'average': np.mean(self.cycle_history) if self.cycle_history else 0,
                'strength': abs(self.lines.oscillator[0])
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'cycle_high': self.lines.cycle_high[0] != float('nan'),
                'cycle_low': self.lines.cycle_low[0] != float('nan')
            },
            'market_state': {
                'trend_strength': abs(self.ma[0] - self.data[0]),
                'cycle_phase': ('peak' if self.lines.oscillator[0] > 0
                              else 'trough'),
                'momentum': (self.lines.oscillator[0] -
                           self.lines.signal_line[0])
            }
        }
