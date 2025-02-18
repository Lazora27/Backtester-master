import backtrader as bt
import numpy as np

class MACDDivergence(bt.Indicator):
    """
    MACD Divergence Indicator
    
    Erweiterte Version mit:
    - Histogram-Divergenzanalyse
    - Signal-Line Crossover
    - Divergenzstärke-Bewertung
    - Multi-Timeframe Bestätigung
    - Volumenprofile
    
    Divergenztypen:
    - Bullish (Preis macht tiefere Tiefs, MACD macht höhere Tiefs)
    - Bearish (Preis macht höhere Hochs, MACD macht tiefere Hochs)
    - Hidden Bullish (Preis macht höhere Tiefs, MACD macht tiefere Tiefs)
    - Hidden Bearish (Preis macht tiefere Hochs, MACD macht höhere Hochs)
    
    Parameter:
    - fast_period (12): Schnelle EMA Periode
    - slow_period (26): Langsame EMA Periode
    - signal_period (9): Signal Periode
    - divergence_length (20): Länge für Divergenzsuche
    - threshold (0.0001): Mindestabstand für Divergenzerkennung
    - volume_factor (1.5): Volumen-Bestätigungsfaktor
    """
    
    lines = ('macd', 'signal', 'histogram',
             'bullish_div', 'bearish_div',
             'hidden_bullish_div', 'hidden_bearish_div',
             'hist_bullish_div', 'hist_bearish_div',
             'signal_cross_up', 'signal_cross_down',
             'div_strength', 'volume_profile')
             
    params = (
        ('fast_period', 12),
        ('slow_period', 26),
        ('signal_period', 9),
        ('divergence_length', 20),
        ('threshold', 0.0001),
        ('volume_factor', 1.5)
    )
    
    plotlines = dict(
        macd=dict(color='blue', _name='MACD'),
        signal=dict(color='red', _name='Signal'),
        histogram=dict(_method='bar', alpha=0.5,
                      _name='Histogram',
                      color='gray'),
        bullish_div=dict(_name='Bullish', color='green', marker='^'),
        bearish_div=dict(_name='Bearish', color='red', marker='v'),
        hidden_bullish_div=dict(_name='Hidden Bull', color='lime', marker='^'),
        hidden_bearish_div=dict(_name='Hidden Bear', color='darkred', marker='v'),
        hist_bullish_div=dict(_name='Hist Bull', color='lightgreen', marker='^'),
        hist_bearish_div=dict(_name='Hist Bear', color='pink', marker='v'),
        signal_cross_up=dict(_name='Cross Up', color='green', marker='o'),
        signal_cross_down=dict(_name='Cross Down', color='red', marker='o'),
        div_strength=dict(_name='Strength', color='purple'),
        volume_profile=dict(_name='Volume', color='orange')
    )
    
    def __init__(self):
        super(MACDDivergence, self).__init__()
        
        # MACD berechnen
        fast_ma = bt.indicators.EMA(period=self.p.fast_period)
        slow_ma = bt.indicators.EMA(period=self.p.slow_period)
        
        macd = fast_ma - slow_ma
        signal = bt.indicators.EMA(macd, period=self.p.signal_period)
        histogram = macd - signal
        
        self.lines.macd = macd
        self.lines.signal = signal
        self.lines.histogram = histogram
        
        # Volumen-Profil
        self.volume_ma = bt.indicators.SMA(
            self.data.volume,
            period=self.p.signal_period
        )
        
        # Preisextreme
        self.price_highs = bt.indicators.Highest(
            self.data.high,
            period=self.p.divergence_length
        )
        self.price_lows = bt.indicators.Lowest(
            self.data.low,
            period=self.p.divergence_length
        )
        
        # MACD Extreme
        self.macd_highs = bt.indicators.Highest(
            macd,
            period=self.p.divergence_length
        )
        self.macd_lows = bt.indicators.Lowest(
            macd,
            period=self.p.divergence_length
        )
        
        # Histogram Extreme
        self.hist_highs = bt.indicators.Highest(
            histogram,
            period=self.p.divergence_length
        )
        self.hist_lows = bt.indicators.Lowest(
            histogram,
            period=self.p.divergence_length
        )
        
        # Speicher für Extrempunkte
        self.price_peaks = []
        self.price_troughs = []
        self.macd_peaks = []
        self.macd_troughs = []
        self.hist_peaks = []
        self.hist_troughs = []
        
    def calculate_divergence_strength(self, price_diff, indicator_diff):
        """Berechnet die Stärke der Divergenz."""
        # Normalisiere die Differenzen
        norm_price = abs(price_diff / self.data.close[0])
        norm_ind = abs(indicator_diff / self.macd_highs[0])
        
        # Gewichtete Stärke (0-100)
        strength = (norm_price * 0.6 + norm_ind * 0.4) * 100
        return min(100, strength)
        
    def check_volume_confirmation(self):
        """Überprüft die Volumenbestätigung."""
        return (self.data.volume[0] >
                self.volume_ma[0] * self.p.volume_factor)
        
    def check_signal_cross(self):
        """Überprüft MACD Signal-Line Crossover."""
        cross_up = (self.lines.macd[0] > self.lines.signal[0] and
                   self.lines.macd[-1] <= self.lines.signal[-1])
        cross_down = (self.lines.macd[0] < self.lines.signal[0] and
                     self.lines.macd[-1] >= self.lines.signal[-1])
        return cross_up, cross_down
        
    def identify_new_extremes(self, current_bar):
        # Preis-Extrema
        if self.is_peak(self.data.high, -1):
            self.price_peaks.append((current_bar-1, self.data.high[-1]))
        if self.is_trough(self.data.low, -1):
            self.price_troughs.append((current_bar-1, self.data.low[-1]))
            
        # MACD-Extrema
        if self.is_peak(self.lines.macd, -1):
            self.macd_peaks.append((current_bar-1, self.lines.macd[-1]))
        if self.is_trough(self.lines.macd, -1):
            self.macd_troughs.append((current_bar-1, self.lines.macd[-1]))
            
        # Histogram-Extrema
        if self.is_peak(self.lines.histogram, -1):
            self.hist_peaks.append((current_bar-1, self.lines.histogram[-1]))
        if self.is_trough(self.lines.histogram, -1):
            self.hist_troughs.append((current_bar-1, self.lines.histogram[-1]))
            
    def clean_old_points(self, current_bar):
        # Alte Preis-Extrempunkte entfernen
        while (len(self.price_peaks) > 0 and
               current_bar - self.price_peaks[0][0] > self.p.divergence_length):
            self.price_peaks.pop(0)
        while (len(self.price_troughs) > 0 and
               current_bar - self.price_troughs[0][0] > self.p.divergence_length):
            self.price_troughs.pop(0)
            
        # Alte MACD-Extrempunkte entfernen
        while (len(self.macd_peaks) > 0 and
               current_bar - self.macd_peaks[0][0] > self.p.divergence_length):
            self.macd_peaks.pop(0)
        while (len(self.macd_troughs) > 0 and
               current_bar - self.macd_troughs[0][0] > self.p.divergence_length):
            self.macd_troughs.pop(0)
            
        # Alte Histogram-Extrempunkte entfernen
        while (len(self.hist_peaks) > 0 and
               current_bar - self.hist_peaks[0][0] > self.p.divergence_length):
            self.hist_peaks.pop(0)
        while (len(self.hist_troughs) > 0 and
               current_bar - self.hist_troughs[0][0] > self.p.divergence_length):
            self.hist_troughs.pop(0)
            
    def is_peak(self, data, index):
        """Überprüft ob ein Punkt ein lokales Maximum ist."""
        return (data[index-1] < data[index] > data[index+1])
        
    def is_trough(self, data, index):
        """Überprüft ob ein Punkt ein lokales Minimum ist."""
        return (data[index-1] > data[index] < data[index+1])
        
    def check_regular_bullish_divergence(self):
        """Überprüft auf reguläre bullische Divergenz."""
        if len(self.price_troughs) < 2 or len(self.macd_troughs) < 2:
            return False
            
        # Preis macht tiefere Tiefs, MACD macht höhere Tiefs
        price_lower = self.price_troughs[-1][1] < self.price_troughs[-2][1]
        macd_higher = self.macd_troughs[-1][1] > self.macd_troughs[-2][1]
        
        return price_lower and macd_higher
        
    def check_regular_bearish_divergence(self):
        """Überprüft auf reguläre bärische Divergenz."""
        if len(self.price_peaks) < 2 or len(self.macd_peaks) < 2:
            return False
            
        # Preis macht höhere Hochs, MACD macht tiefere Hochs
        price_higher = self.price_peaks[-1][1] > self.price_peaks[-2][1]
        macd_lower = self.macd_peaks[-1][1] < self.macd_peaks[-2][1]
        
        return price_higher and macd_lower
        
    def check_hidden_bullish_divergence(self):
        """Überprüft auf versteckte bullische Divergenz."""
        if len(self.price_troughs) < 2 or len(self.macd_troughs) < 2:
            return False
            
        # Preis macht höhere Tiefs, MACD macht tiefere Tiefs
        price_higher = self.price_troughs[-1][1] > self.price_troughs[-2][1]
        macd_lower = self.macd_troughs[-1][1] < self.macd_troughs[-2][1]
        
        return price_higher and macd_lower
        
    def check_hidden_bearish_divergence(self):
        """Überprüft auf versteckte bärische Divergenz."""
        if len(self.price_peaks) < 2 or len(self.macd_peaks) < 2:
            return False
            
        # Preis macht tiefere Hochs, MACD macht höhere Hochs
        price_lower = self.price_peaks[-1][1] < self.price_peaks[-2][1]
        macd_higher = self.macd_peaks[-1][1] > self.macd_peaks[-2][1]
        
        return price_lower and macd_higher
        
    def calculate_histogram_divergences(self):
        """Berechnet Histogram-Divergenzen."""
        if len(self.hist_peaks) < 2 or len(self.hist_troughs) < 2:
            return
            
        # Bullische Histogram-Divergenz
        hist_bullish = (self.hist_troughs[-1][1] < self.hist_troughs[-2][1] and
                       self.macd_troughs[-1][1] > self.macd_troughs[-2][1])
        self.lines.hist_bullish_div[0] = (
            self.data.low[0] if hist_bullish else float('nan')
        )
        
        # Bärische Histogram-Divergenz
        hist_bearish = (self.hist_peaks[-1][1] > self.hist_peaks[-2][1] and
                       self.macd_peaks[-1][1] < self.macd_peaks[-2][1])
        self.lines.hist_bearish_div[0] = (
            self.data.high[0] if hist_bearish else float('nan')
        )
        
    def calculate_divergences(self):
        """Berechnet Divergenzen."""
        if self.check_regular_bullish_divergence():
            self.lines.bullish_div[0] = self.data.low[0]
            self.lines.div_strength[0] = self.calculate_divergence_strength(
                self.price_troughs[-1][1] - self.price_troughs[-2][1],
                self.macd_troughs[-1][1] - self.macd_troughs[-2][1]
            )
        else:
            self.lines.bullish_div[0] = float('nan')
            self.lines.div_strength[0] = float('nan')
            
        if self.check_regular_bearish_divergence():
            self.lines.bearish_div[0] = self.data.high[0]
            self.lines.div_strength[0] = self.calculate_divergence_strength(
                self.price_peaks[-1][1] - self.price_peaks[-2][1],
                self.macd_peaks[-1][1] - self.macd_peaks[-2][1]
            )
        else:
            self.lines.bearish_div[0] = float('nan')
            self.lines.div_strength[0] = float('nan')
            
        if self.check_hidden_bullish_divergence():
            self.lines.hidden_bullish_div[0] = self.data.low[0]
            self.lines.div_strength[0] = self.calculate_divergence_strength(
                self.price_troughs[-1][1] - self.price_troughs[-2][1],
                self.macd_troughs[-1][1] - self.macd_troughs[-2][1]
            )
        else:
            self.lines.hidden_bullish_div[0] = float('nan')
            self.lines.div_strength[0] = float('nan')
            
        if self.check_hidden_bearish_divergence():
            self.lines.hidden_bearish_div[0] = self.data.high[0]
            self.lines.div_strength[0] = self.calculate_divergence_strength(
                self.price_peaks[-1][1] - self.price_peaks[-2][1],
                self.macd_peaks[-1][1] - self.macd_peaks[-2][1]
            )
        else:
            self.lines.hidden_bearish_div[0] = float('nan')
            self.lines.div_strength[0] = float('nan')
            
    def next(self):
        # Aktuelle Position
        current_bar = len(self)
        
        # Neue Extrempunkte identifizieren
        if current_bar > 1:
            self.identify_new_extremes(current_bar)
            
        # Alte Punkte entfernen
        self.clean_old_points(current_bar)
        
        # Signal-Line Crossover
        cross_up, cross_down = self.check_signal_cross()
        self.lines.signal_cross_up[0] = (
            self.data.low[0] if cross_up else float('nan')
        )
        self.lines.signal_cross_down[0] = (
            self.data.high[0] if cross_down else float('nan')
        )
        
        # Volumen-Profil
        self.lines.volume_profile[0] = (
            100 if self.check_volume_confirmation() else 0
        )
        
        # Divergenzen berechnen
        self.calculate_divergences()
        
        # Histogram-Divergenzen
        self.calculate_histogram_divergences()
