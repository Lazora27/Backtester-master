import backtrader as bt
import numpy as np

class StochasticDivergence(bt.Indicator):
    """
    Stochastic Divergence Indicator
    
    Erweiterte Version mit:
    - Doppelte Stochastik
    - Momentum-Bestätigung
    - Divergenzstärke-Bewertung
    - Overbought/Oversold Integration
    - Multi-Timeframe Analyse
    
    Divergenztypen:
    - Bullish (Preis macht tiefere Tiefs, Stochastik macht höhere Tiefs)
    - Bearish (Preis macht höhere Hochs, Stochastik macht tiefere Hochs)
    - Hidden Bullish (Preis macht höhere Tiefs, Stochastik macht tiefere Tiefs)
    - Hidden Bearish (Preis macht tiefere Hochs, Stochastik macht höhere Hochs)
    
    Parameter:
    - period (14): Stochastik Periode
    - period_dfast (3): Schnelle %D Periode
    - period_dslow (3): Langsame %D Periode
    - divergence_length (20): Länge für Divergenzsuche
    - threshold (2.0): Mindestabstand für Divergenzerkennung
    - overbought (80): Überkauft-Level
    - oversold (20): Überverkauft-Level
    """
    
    lines = ('fastk', 'fastd', 'slowd',
             'double_stoch', 'double_stoch_signal',
             'bullish_div', 'bearish_div',
             'hidden_bullish_div', 'hidden_bearish_div',
             'overbought_signal', 'oversold_signal',
             'div_strength', 'momentum_confirm')
             
    params = (
        ('period', 14),
        ('period_dfast', 3),
        ('period_dslow', 3),
        ('divergence_length', 20),
        ('threshold', 2.0),
        ('overbought', 80),
        ('oversold', 20)
    )
    
    plotlines = dict(
        fastk=dict(color='blue', _name='%K'),
        fastd=dict(color='red', _name='%D Fast'),
        slowd=dict(color='green', _name='%D Slow'),
        double_stoch=dict(color='purple', _name='Double Stoch'),
        double_stoch_signal=dict(color='orange', _name='Double Signal'),
        bullish_div=dict(_name='Bullish', color='green', marker='^'),
        bearish_div=dict(_name='Bearish', color='red', marker='v'),
        hidden_bullish_div=dict(_name='Hidden Bull', color='lime', marker='^'),
        hidden_bearish_div=dict(_name='Hidden Bear', color='darkred', marker='v'),
        overbought_signal=dict(_name='Overbought', color='darkred'),
        oversold_signal=dict(_name='Oversold', color='darkgreen'),
        div_strength=dict(_name='Strength', color='gray'),
        momentum_confirm=dict(_name='Momentum', color='blue')
    )
    
    def __init__(self):
        super(StochasticDivergence, self).__init__()
        
        # Stochastik berechnen
        self.k = bt.indicators.StochasticFast(
            self.data,
            period=self.p.period,
            period_dfast=self.p.period_dfast
        )
        
        # Linien zuweisen
        self.lines.fastk = self.k.lines.percK
        self.lines.fastd = self.k.lines.percD
        
        # Langsame Stochastik
        self.lines.slowd = bt.indicators.SMA(
            self.lines.fastd,
            period=self.p.period_dslow
        )
        
        # Doppelte Stochastik
        self.double_stoch = bt.indicators.StochasticFast(
            self.k.lines.percK,
            period=self.p.period,
            period_dfast=self.p.period_dfast
        )
        self.lines.double_stoch = self.double_stoch.lines.percK
        self.lines.double_stoch_signal = self.double_stoch.lines.percD
        
        # Momentum-Bestätigung
        self.momentum = bt.indicators.ROC(
            self.data,
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
        
        # Stochastik Extreme
        self.stoch_highs = bt.indicators.Highest(
            self.lines.slowd,
            period=self.p.divergence_length
        )
        self.stoch_lows = bt.indicators.Lowest(
            self.lines.slowd,
            period=self.p.divergence_length
        )
        
        # Speicher für Extrempunkte
        self.price_peaks = []
        self.price_troughs = []
        self.stoch_peaks = []
        self.stoch_troughs = []
        
    def calculate_divergence_strength(self, price_diff, stoch_diff):
        """Berechnet die Stärke der Divergenz."""
        # Normalisiere die Differenzen
        norm_price = abs(price_diff / self.data.close[0])
        norm_stoch = abs(stoch_diff / 100)
        
        # Gewichtete Stärke (0-100)
        strength = (norm_price * 0.6 + norm_stoch * 0.4) * 100
        return min(100, strength)
        
    def check_momentum_confirmation(self, bullish=True):
        """Überprüft die Momentum-Bestätigung."""
        if bullish:
            return self.momentum[0] > 0
        return self.momentum[0] < 0
        
    def check_overbought_oversold(self):
        """Überprüft Überkauft/Überverkauft Bedingungen."""
        overbought = self.lines.slowd[0] > self.p.overbought
        oversold = self.lines.slowd[0] < self.p.oversold
        return overbought, oversold
        
    def identify_new_extremes(self, current_bar):
        """Identifiziert neue Extrempunkte."""
        # Preis-Extrema
        if self.is_peak(self.data.high, -1):
            self.price_peaks.append((current_bar-1, self.data.high[-1]))
        if self.is_trough(self.data.low, -1):
            self.price_troughs.append((current_bar-1, self.data.low[-1]))
            
        # Stochastic-Extrema
        if self.is_peak(self.lines.slowd, -1):
            self.stoch_peaks.append((current_bar-1, self.lines.slowd[-1]))
        if self.is_trough(self.lines.slowd, -1):
            self.stoch_troughs.append((current_bar-1, self.lines.slowd[-1]))
            
    def clean_old_points(self, current_bar):
        """Entfernt alte Punkte."""
        while (len(self.price_peaks) > 0 and
               current_bar - self.price_peaks[0][0] > self.p.divergence_length):
            self.price_peaks.pop(0)
        while (len(self.price_troughs) > 0 and
               current_bar - self.price_troughs[0][0] > self.p.divergence_length):
            self.price_troughs.pop(0)
        while (len(self.stoch_peaks) > 0 and
               current_bar - self.stoch_peaks[0][0] > self.p.divergence_length):
            self.stoch_peaks.pop(0)
        while (len(self.stoch_troughs) > 0 and
               current_bar - self.stoch_troughs[0][0] > self.p.divergence_length):
            self.stoch_troughs.pop(0)
            
    def is_peak(self, data, index):
        """Überprüft ob ein Punkt ein lokales Maximum ist."""
        return (data[index-1] < data[index] > data[index+1])
        
    def is_trough(self, data, index):
        """Überprüft ob ein Punkt ein lokales Minimum ist."""
        return (data[index-1] > data[index] < data[index+1])
        
    def calculate_divergences(self):
        """Berechnet die Divergenzen."""
        # Reguläre Bullish Divergenz
        if len(self.price_troughs) < 2 or len(self.stoch_troughs) < 2:
            self.lines.bullish_div[0] = float('nan')
        else:
            price_lower = self.price_troughs[-1][1] < self.price_troughs[-2][1]
            stoch_higher = self.stoch_troughs[-1][1] > self.stoch_troughs[-2][1]
            overbought = self.lines.slowd[0] > self.p.overbought
            if price_lower and stoch_higher and overbought:
                self.lines.bullish_div[0] = self.data.low[0]
            else:
                self.lines.bullish_div[0] = float('nan')
                
        # Reguläre Bearish Divergenz
        if len(self.price_peaks) < 2 or len(self.stoch_peaks) < 2:
            self.lines.bearish_div[0] = float('nan')
        else:
            price_higher = self.price_peaks[-1][1] > self.price_peaks[-2][1]
            stoch_lower = self.stoch_peaks[-1][1] < self.stoch_peaks[-2][1]
            oversold = self.lines.slowd[0] < self.p.oversold
            if price_higher and stoch_lower and oversold:
                self.lines.bearish_div[0] = self.data.high[0]
            else:
                self.lines.bearish_div[0] = float('nan')
                
        # Versteckte Bullish Divergenz
        if len(self.price_troughs) < 2 or len(self.stoch_troughs) < 2:
            self.lines.hidden_bullish_div[0] = float('nan')
        else:
            price_higher = self.price_troughs[-1][1] > self.price_troughs[-2][1]
            stoch_lower = self.stoch_troughs[-1][1] < self.stoch_troughs[-2][1]
            overbought = self.lines.slowd[0] > self.p.overbought
            if price_higher and stoch_lower and overbought:
                self.lines.hidden_bullish_div[0] = self.data.low[0]
            else:
                self.lines.hidden_bullish_div[0] = float('nan')
                
        # Versteckte Bearish Divergenz
        if len(self.price_peaks) < 2 or len(self.stoch_peaks) < 2:
            self.lines.hidden_bearish_div[0] = float('nan')
        else:
            price_lower = self.price_peaks[-1][1] < self.price_peaks[-2][1]
            stoch_higher = self.stoch_peaks[-1][1] > self.stoch_peaks[-2][1]
            oversold = self.lines.slowd[0] < self.p.oversold
            if price_lower and stoch_higher and oversold:
                self.lines.hidden_bearish_div[0] = self.data.high[0]
            else:
                self.lines.hidden_bearish_div[0] = float('nan')
                
        # Divergenzstärke
        if self.lines.bullish_div[0] != float('nan'):
            price_diff = self.price_troughs[-1][1] - self.price_troughs[-2][1]
            stoch_diff = self.stoch_troughs[-1][1] - self.stoch_troughs[-2][1]
            self.lines.div_strength[0] = self.calculate_divergence_strength(price_diff, stoch_diff)
        elif self.lines.bearish_div[0] != float('nan'):
            price_diff = self.price_peaks[-1][1] - self.price_peaks[-2][1]
            stoch_diff = self.stoch_peaks[-1][1] - self.stoch_peaks[-2][1]
            self.lines.div_strength[0] = self.calculate_divergence_strength(price_diff, stoch_diff)
        else:
            self.lines.div_strength[0] = float('nan')
            
    def next(self):
        # Aktuelle Position
        current_bar = len(self)
        
        # Neue Extrempunkte identifizieren
        if current_bar > 1:
            self.identify_new_extremes(current_bar)
            
        # Alte Punkte entfernen
        self.clean_old_points(current_bar)
        
        # Überkauft/Überverkauft Signale
        overbought, oversold = self.check_overbought_oversold()
        self.lines.overbought_signal[0] = (
            100 if overbought else float('nan')
        )
        self.lines.oversold_signal[0] = (
            0 if oversold else float('nan')
        )
        
        # Momentum-Bestätigung
        self.lines.momentum_confirm[0] = (
            100 if self.check_momentum_confirmation() else 0
        )
        
        # Divergenzen berechnen
        self.calculate_divergences()
