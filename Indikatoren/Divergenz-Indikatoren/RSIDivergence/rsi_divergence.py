import backtrader as bt
import numpy as np

class RSIDivergence(bt.Indicator):
    """
    RSI Divergence Indicator
    
    Erweiterte Version mit:
    - A/D Bestätigungssignale
    - Divergenzstärke-Bewertung
    - Multi-Timeframe Analyse
    - Trendfilter
    - Volumenbestätigung
    
    Divergenztypen:
    - Bullish (Preis macht tiefere Tiefs, RSI macht höhere Tiefs)
    - Bearish (Preis macht höhere Hochs, RSI macht tiefere Hochs)
    - Hidden Bullish (Preis macht höhere Tiefs, RSI macht tiefere Tiefs)
    - Hidden Bearish (Preis macht tiefere Hochs, RSI macht höhere Hochs)
    
    Parameter:
    - period (14): RSI Periode
    - divergence_length (20): Länge für Divergenzsuche
    - threshold (2.0): Mindestabstand für Divergenzerkennung
    - trend_period (50): Periode für Trendfilter
    - volume_threshold (1.5): Volumen-Bestätigungsschwelle
    """
    
    lines = ('rsi', 'bullish_div', 'bearish_div',
             'hidden_bullish_div', 'hidden_bearish_div',
             'div_strength', 'trend_filter', 'volume_confirm',
             'strong_bullish', 'strong_bearish')
             
    params = (
        ('period', 14),
        ('divergence_length', 20),
        ('threshold', 2.0),
        ('trend_period', 50),
        ('volume_threshold', 1.5)
    )
    
    plotlines = dict(
        rsi=dict(color='blue', _name='RSI'),
        bullish_div=dict(_name='Bullish', color='green', marker='^'),
        bearish_div=dict(_name='Bearish', color='red', marker='v'),
        hidden_bullish_div=dict(_name='Hidden Bull', color='lime', marker='^'),
        hidden_bearish_div=dict(_name='Hidden Bear', color='darkred', marker='v'),
        div_strength=dict(_name='Strength', color='gray'),
        trend_filter=dict(_name='Trend', color='purple'),
        volume_confirm=dict(_name='Volume', color='orange'),
        strong_bullish=dict(_name='Strong Bull', color='darkgreen', marker='^'),
        strong_bearish=dict(_name='Strong Bear', color='darkred', marker='v')
    )
    
    def __init__(self):
        super(RSIDivergence, self).__init__()
        
        # RSI berechnen
        self.rsi = bt.indicators.RSI(
            self.data,
            period=self.p.period
        )
        
        # Trendfilter
        self.sma = bt.indicators.SMA(
            self.data,
            period=self.p.trend_period
        )
        
        # Volumen-Bestätigung
        self.volume_ma = bt.indicators.SMA(
            self.data.volume,
            period=self.p.period
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
        
        # RSI Extreme
        self.rsi_highs = bt.indicators.Highest(
            self.rsi,
            period=self.p.divergence_length
        )
        self.rsi_lows = bt.indicators.Lowest(
            self.rsi,
            period=self.p.divergence_length
        )
        
        # Speicher für Extrempunkte
        self.price_peaks = []
        self.price_troughs = []
        self.rsi_peaks = []
        self.rsi_troughs = []
        
    def is_peak(self, data, index):
        """Überprüft ob ein Punkt ein lokales Maximum ist."""
        return (data[index-1] < data[index] > data[index+1])
        
    def is_trough(self, data, index):
        """Überprüft ob ein Punkt ein lokales Minimum ist."""
        return (data[index-1] > data[index] < data[index+1])
        
    def calculate_divergence_strength(self, price_diff, rsi_diff):
        """Berechnet die Stärke der Divergenz."""
        # Normalisiere die Differenzen
        norm_price = abs(price_diff / self.data.close[0])
        norm_rsi = abs(rsi_diff / 100)
        
        # Gewichtete Stärke (0-100)
        strength = (norm_price * 0.6 + norm_rsi * 0.4) * 100
        return min(100, strength)
        
    def check_volume_confirmation(self):
        """Überprüft die Volumenbestätigung."""
        return (self.data.volume[0] >
                self.volume_ma[0] * self.p.volume_threshold)
        
    def check_trend_confirmation(self, bullish=True):
        """Überprüft die Trendbestätigung."""
        if bullish:
            return self.data.close[0] > self.sma[0]
        return self.data.close[0] < self.sma[0]
        
    def clean_old_points(self, current_bar):
        """Entfernt alte Extrempunkte."""
        while (len(self.price_peaks) > 0 and
               current_bar - self.price_peaks[0][0] > self.p.divergence_length):
            self.price_peaks.pop(0)
        while (len(self.price_troughs) > 0 and
               current_bar - self.price_troughs[0][0] > self.p.divergence_length):
            self.price_troughs.pop(0)
        while (len(self.rsi_peaks) > 0 and
               current_bar - self.rsi_peaks[0][0] > self.p.divergence_length):
            self.rsi_peaks.pop(0)
        while (len(self.rsi_troughs) > 0 and
               current_bar - self.rsi_troughs[0][0] > self.p.divergence_length):
            self.rsi_troughs.pop(0)
            
    def check_regular_bullish_divergence(self):
        """Überprüft auf reguläre bullische Divergenz."""
        if len(self.price_troughs) < 2 or len(self.rsi_troughs) < 2:
            return False
            
        # Preis macht tiefere Tiefs, RSI macht höhere Tiefs
        price_lower = self.price_troughs[-1][1] < self.price_troughs[-2][1]
        rsi_higher = self.rsi_troughs[-1][1] > self.rsi_troughs[-2][1]
        
        return price_lower and rsi_higher
        
    def check_regular_bearish_divergence(self):
        """Überprüft auf reguläre bärische Divergenz."""
        if len(self.price_peaks) < 2 or len(self.rsi_peaks) < 2:
            return False
            
        # Preis macht höhere Hochs, RSI macht tiefere Hochs
        price_higher = self.price_peaks[-1][1] > self.price_peaks[-2][1]
        rsi_lower = self.rsi_peaks[-1][1] < self.rsi_peaks[-2][1]
        
        return price_higher and rsi_lower
        
    def check_hidden_bullish_divergence(self):
        """Überprüft auf versteckte bullische Divergenz."""
        if len(self.price_troughs) < 2 or len(self.rsi_troughs) < 2:
            return False
            
        # Preis macht höhere Tiefs, RSI macht tiefere Tiefs
        price_higher = self.price_troughs[-1][1] > self.price_troughs[-2][1]
        rsi_lower = self.rsi_troughs[-1][1] < self.rsi_troughs[-2][1]
        
        return price_higher and rsi_lower
        
    def check_hidden_bearish_divergence(self):
        """Überprüft auf versteckte bärische Divergenz."""
        if len(self.price_peaks) < 2 or len(self.rsi_peaks) < 2:
            return False
            
        # Preis macht tiefere Hochs, RSI macht höhere Hochs
        price_lower = self.price_peaks[-1][1] < self.price_peaks[-2][1]
        rsi_higher = self.rsi_peaks[-1][1] > self.rsi_peaks[-2][1]
        
        return price_lower and rsi_higher
        
    def calculate_divergences(self):
        """Berechnet die Divergenzen."""
        if self.check_regular_bullish_divergence():
            self.lines.bullish_div[0] = self.data.low[0]
            self.lines.div_strength[0] = self.calculate_divergence_strength(
                self.price_troughs[-1][1] - self.price_troughs[-2][1],
                self.rsi_troughs[-1][1] - self.rsi_troughs[-2][1]
            )
            if self.check_volume_confirmation() and self.check_trend_confirmation():
                self.lines.strong_bullish[0] = self.data.low[0]
            else:
                self.lines.strong_bullish[0] = float('nan')
        else:
            self.lines.bullish_div[0] = float('nan')
            self.lines.div_strength[0] = float('nan')
            self.lines.strong_bullish[0] = float('nan')
            
        if self.check_regular_bearish_divergence():
            self.lines.bearish_div[0] = self.data.high[0]
            self.lines.div_strength[0] = self.calculate_divergence_strength(
                self.price_peaks[-1][1] - self.price_peaks[-2][1],
                self.rsi_peaks[-1][1] - self.rsi_peaks[-2][1]
            )
            if self.check_volume_confirmation() and not self.check_trend_confirmation():
                self.lines.strong_bearish[0] = self.data.high[0]
            else:
                self.lines.strong_bearish[0] = float('nan')
        else:
            self.lines.bearish_div[0] = float('nan')
            self.lines.div_strength[0] = float('nan')
            self.lines.strong_bearish[0] = float('nan')
            
        if self.check_hidden_bullish_divergence():
            self.lines.hidden_bullish_div[0] = self.data.low[0]
        else:
            self.lines.hidden_bullish_div[0] = float('nan')
            
        if self.check_hidden_bearish_divergence():
            self.lines.hidden_bearish_div[0] = self.data.high[0]
        else:
            self.lines.hidden_bearish_div[0] = float('nan')
            
    def next(self):
        # RSI-Wert
        self.lines.rsi[0] = self.rsi[0]
        
        # Aktuelle Position
        current_bar = len(self)
        
        # Neue Extrempunkte identifizieren
        if current_bar > 1:
            # Preis-Extrema
            if self.is_peak(self.data.high, -1):
                self.price_peaks.append((current_bar-1, self.data.high[-1]))
            if self.is_trough(self.data.low, -1):
                self.price_troughs.append((current_bar-1, self.data.low[-1]))
                
            # RSI-Extrema
            if self.is_peak(self.rsi, -1):
                self.rsi_peaks.append((current_bar-1, self.rsi[-1]))
            if self.is_trough(self.rsi, -1):
                self.rsi_troughs.append((current_bar-1, self.rsi[-1]))
                
        # Alte Punkte entfernen
        self.clean_old_points(current_bar)
        
        # Divergenzen und Signale berechnen
        self.calculate_divergences()
        
        # Trendfilter
        self.lines.trend_filter[0] = 100 if self.check_trend_confirmation() else 0
        
        # Volumenbestätigung
        self.lines.volume_confirm[0] = (
            100 if self.check_volume_confirmation() else 0
        )
