import backtrader as bt
import numpy as np
from scipy import signal

class SmoothedCycle(bt.Indicator):
    """
    Smoothed Cycle Indicator
    
    Ein fortgeschrittener Indikator, der geglättete Zyklen
    identifiziert und analysiert.
    
    Features:
    - Mehrfache Glättungsstufen
    - Zyklusextraktion
    - Trendbereinigung
    - Signalgenerierung
    
    Parameter:
    - cycle_period (20): Zyklusperiode
    - smooth_period (10): Glättungsperiode
    - filter_cutoff (0.1): Filterschnittfrequenz
    """
    
    lines = ('cycle', 'smooth_cycle',
             'trend', 'cycle_quality',
             'signal')
             
    params = (
        ('cycle_period', 20),
        ('smooth_period', 10),
        ('filter_cutoff', 0.1)
    )
    
    plotlines = dict(
        cycle=dict(color='blue', _name='Cycle'),
        smooth_cycle=dict(color='red', _name='Smooth Cycle'),
        trend=dict(color='green', _name='Trend'),
        cycle_quality=dict(color='purple', _name='Cycle Quality'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(SmoothedCycle, self).__init__()
        
        # Historie
        self.price_history = []
        self.cycle_history = []
        self.smooth_history = []
        
        # Butterworth-Filter Design
        self.b, self.a = signal.butter(
            2,  # Filter-Ordnung
            self.p.filter_cutoff,
            btype='low'
        )
        
    def smooth_data(self, data):
        """
        Glättet die Daten mit Butterworth-Filter.
        """
        if len(data) < 4:
            return data
            
        return signal.filtfilt(
            self.b,
            self.a,
            data
        )
        
    def extract_cycle(self, data):
        """
        Extrahiert den Zyklus aus den Daten.
        """
        if len(data) < self.p.cycle_period:
            return data
            
        # Trend entfernen
        detrended = signal.detrend(data)
        
        # Zyklische Komponente extrahieren
        cycle = np.zeros_like(detrended)
        for i in range(len(detrended)):
            start = max(0, i - self.p.cycle_period)
            window = detrended[start:i+1]
            if len(window) >= 3:
                cycle[i] = np.mean(window)
                
        return cycle
        
    def calculate_quality(self):
        """
        Berechnet die Zyklusqualität.
        """
        if len(self.cycle_history) < self.p.cycle_period:
            return 0
            
        cycle = np.array(
            self.cycle_history[-self.p.cycle_period:]
        )
        
        # Autokorrelation
        corr = np.correlate(
            cycle,
            cycle,
            mode='full'
        )
        corr = corr[len(corr)//2:]
        
        # Qualität basierend auf Periodizität
        peaks = signal.find_peaks(corr)[0]
        if len(peaks) > 1:
            peak_spacing = np.diff(peaks)
            quality = 1 - np.std(peak_spacing) / np.mean(
                peak_spacing
            )
            return max(0, min(1, quality))
            
        return 0
        
    def next(self):
        # Preis speichern
        self.price_history.append(self.data.close[0])
        
        if len(self.price_history) >= self.p.cycle_period:
            # Daten glätten
            smooth_data = self.smooth_data(
                np.array(self.price_history)
            )
            
            # Zyklus extrahieren
            cycle = self.extract_cycle(smooth_data)
            
            # Trend berechnen
            trend = smooth_data - cycle
            
            # Geglätteten Zyklus berechnen
            if len(cycle) >= self.p.smooth_period:
                smooth_cycle = np.mean(
                    cycle[-self.p.smooth_period:]
                )
            else:
                smooth_cycle = cycle[-1]
                
            self.cycle_history.append(cycle[-1])
            self.smooth_history.append(smooth_cycle)
            
            # Qualität berechnen
            quality = self.calculate_quality()
            
            # Linien aktualisieren
            self.lines.cycle[0] = cycle[-1]
            self.lines.smooth_cycle[0] = smooth_cycle
            self.lines.trend[0] = trend[-1]
            self.lines.cycle_quality[0] = quality
            
            # Signal
            if len(self.smooth_history) >= 2:
                if (smooth_cycle > 0 and
                    self.smooth_history[-2] <= 0 and
                    quality > 0.6):
                    self.lines.signal[0] = 1  # Kaufsignal
                elif (smooth_cycle < 0 and
                      self.smooth_history[-2] >= 0 and
                      quality > 0.6):
                    self.lines.signal[0] = -1  # Verkaufssignal
                else:
                    self.lines.signal[0] = 0
            else:
                self.lines.signal[0] = 0
        else:
            # Standardwerte
            self.lines.cycle[0] = 0
            self.lines.smooth_cycle[0] = 0
            self.lines.trend[0] = self.data.close[0]
            self.lines.cycle_quality[0] = 0
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = max(
            self.p.cycle_period,
            self.p.smooth_period
        )
        for hist in [self.price_history,
                    self.cycle_history,
                    self.smooth_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'cycle': {
                'raw': self.lines.cycle[0],
                'smooth': self.lines.smooth_cycle[0],
                'trend': self.lines.trend[0],
                'quality': self.lines.cycle_quality[0]
            },
            'cycle_state': {
                'phase': (
                    'up'
                    if self.lines.smooth_cycle[0] > 0
                    else 'down'
                ),
                'strength': abs(
                    self.lines.smooth_cycle[0]
                ),
                'quality': (
                    'high'
                    if self.lines.cycle_quality[0] > 0.7
                    else 'medium'
                    if self.lines.cycle_quality[0] > 0.4
                    else 'low'
                )
            },
            'trend_analysis': {
                'direction': (
                    'up'
                    if len(self.price_history) >= 2 and
                       self.lines.trend[0] >
                       self.price_history[-2]
                    else 'down'
                ),
                'strength': (
                    abs(
                        self.lines.trend[0] -
                        self.data.close[0]
                    ) / self.data.close[0]
                ),
                'dominance': (
                    'trend'
                    if abs(self.lines.trend[0]) >
                       abs(self.lines.cycle[0])
                    else 'cycle'
                )
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'reliability': (
                    self.lines.cycle_quality[0] *
                    abs(self.lines.smooth_cycle[0])
                )
            },
            'market_conditions': {
                'cycle_quality': (
                    'optimal'
                    if self.lines.cycle_quality[0] > 0.6
                    else 'suboptimal'
                ),
                'trend_structure': (
                    'clear'
                    if abs(
                        self.lines.trend[0] -
                        self.data.close[0]
                    ) > 0.02 * self.data.close[0]
                    else 'unclear'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.cycle_quality[0] > 0.5 and
                        abs(self.lines.smooth_cycle[0]) > 0.01 *
                        self.data.close[0])
                    else 'unfavorable'
                )
            }
        }
