import backtrader as bt
import numpy as np

class FractalChaosOscillator(bt.Indicator):
    """
    Fractal Chaos Oscillator
    
    Ein fortgeschrittener Momentum-Indikator, der Fraktale und
    Chaos-Theorie verwendet, um Marktbewegungen zu analysieren.
    
    Features:
    - Fraktal-Erkennung
    - Chaos-Band-Berechnung
    - Momentum-Analyse
    - Adaptiver Oszillator
    - Signal-Validierung
    
    Parameter:
    - fractal_period (5): Fraktalperiode
    - chaos_period (20): Chaosperiode
    - smooth_period (10): Glättungsperiode
    - threshold (0.5): Signalschwelle
    """
    
    lines = ('oscillator', 'chaos_bands',
             'fractal_high', 'fractal_low',
             'entropy', 'signal',
             'buy_signal', 'sell_signal')
             
    params = (
        ('fractal_period', 5),
        ('chaos_period', 20),
        ('smooth_period', 10),
        ('threshold', 0.5)
    )
    
    plotlines = dict(
        oscillator=dict(color='blue', _name='Oscillator'),
        chaos_bands=dict(color='gray', _name='Chaos Bands'),
        fractal_high=dict(color='green', _name='Fractal High'),
        fractal_low=dict(color='red', _name='Fractal Low'),
        entropy=dict(color='purple', _name='Entropy'),
        signal=dict(color='orange', _name='Signal'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(FractalChaosOscillator, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Glättung
        self.ema = bt.indicators.EMA(period=self.p.smooth_period)
        
        # Historie
        self.price_history = []
        self.fractal_history = []
        self.chaos_history = []
        
    def is_fractal_high(self, data):
        """
        Erkennt Fraktal-Hochs.
        """
        if len(data) < self.p.fractal_period:
            return False
            
        mid = len(data) // 2
        return all(data[mid] > x for i, x in enumerate(data) if i != mid)
        
    def is_fractal_low(self, data):
        """
        Erkennt Fraktal-Tiefs.
        """
        if len(data) < self.p.fractal_period:
            return False
            
        mid = len(data) // 2
        return all(data[mid] < x for i, x in enumerate(data) if i != mid)
        
    def calculate_entropy(self, data):
        """
        Berechnet die Entropie der Preisbewegung.
        """
        if len(data) < 2:
            return 0
            
        # Preisänderungen
        changes = np.diff(data)
        
        # Normalisierung
        if np.std(changes) == 0:
            return 0
            
        changes = (changes - np.mean(changes)) / np.std(changes)
        
        # Entropie berechnen
        hist, _ = np.histogram(changes, bins='auto', density=True)
        hist = hist[hist > 0]
        return -np.sum(hist * np.log(hist))
        
    def calculate_chaos_bands(self):
        """
        Berechnet die Chaos-Bänder.
        """
        if len(self.price_history) < self.p.chaos_period:
            return 0
            
        # Lyapunov-Exponent schätzen
        changes = np.diff(self.price_history)
        if len(changes) < 2:
            return 0
            
        lyap = np.mean(np.log(np.abs(changes[1:] / changes[:-1])))
        
        return lyap
        
    def next(self):
        # Preisdaten aktualisieren
        self.price_history.append(self.data[0])
        if len(self.price_history) > self.p.chaos_period:
            self.price_history.pop(0)
            
        # Fraktale erkennen
        if len(self.price_history) >= self.p.fractal_period:
            window = self.price_history[-self.p.fractal_period:]
            
            # Fraktal-Hochs und -Tiefs
            self.lines.fractal_high[0] = (
                self.data.high[0] if self.is_fractal_high(window) else float('nan')
            )
            self.lines.fractal_low[0] = (
                self.data.low[0] if self.is_fractal_low(window) else float('nan')
            )
            
            # Fraktal-Historie aktualisieren
            self.fractal_history.append(
                1 if self.is_fractal_high(window)
                else -1 if self.is_fractal_low(window)
                else 0
            )
        else:
            self.lines.fractal_high[0] = float('nan')
            self.lines.fractal_low[0] = float('nan')
            
        # Chaos-Bänder
        self.lines.chaos_bands[0] = self.calculate_chaos_bands()
        
        # Entropie
        self.lines.entropy[0] = self.calculate_entropy(self.price_history)
        
        # Oszillator berechnen
        if len(self.fractal_history) > 0:
            # Fraktal-Momentum
            fractal_momentum = sum(self.fractal_history[-self.p.fractal_period:])
            
            # Chaos-Komponente
            chaos_component = self.lines.chaos_bands[0]
            
            # Entropie-Gewichtung
            entropy_weight = 1 - min(1, self.lines.entropy[0])
            
            # Oszillator
            self.lines.oscillator[0] = (
                fractal_momentum * entropy_weight +
                chaos_component * (1 - entropy_weight)
            )
        else:
            self.lines.oscillator[0] = 0
            
        # Signal-Linie
        self.lines.signal[0] = self.ema(self.lines.oscillator)
        
        # Historie begrenzen
        if len(self.fractal_history) > self.p.chaos_period:
            self.fractal_history.pop(0)
            
        # Signal-Generierung
        # Buy Signal
        if (self.lines.oscillator[0] > self.lines.signal[0] and
            self.lines.entropy[0] < self.p.threshold and
            not np.isnan(self.lines.fractal_low[0])):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.oscillator[0] < self.lines.signal[0] and
            self.lines.entropy[0] < self.p.threshold and
            not np.isnan(self.lines.fractal_high[0])):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'oscillator': {
                'value': self.lines.oscillator[0],
                'signal': self.lines.signal[0],
                'direction': np.sign(
                    self.lines.oscillator[0] - self.lines.signal[0]
                ),
                'strength': abs(
                    self.lines.oscillator[0] - self.lines.signal[0]
                )
            },
            'fractals': {
                'high': not np.isnan(self.lines.fractal_high[0]),
                'low': not np.isnan(self.lines.fractal_low[0]),
                'pattern': (
                    'bullish' if len(self.fractal_history) > 0 and
                    sum(self.fractal_history[-self.p.fractal_period:]) > 0
                    else 'bearish' if len(self.fractal_history) > 0 and
                    sum(self.fractal_history[-self.p.fractal_period:]) < 0
                    else 'neutral'
                )
            },
            'chaos': {
                'bands': self.lines.chaos_bands[0],
                'entropy': self.lines.entropy[0],
                'stability': (
                    'high' if self.lines.entropy[0] < 0.3
                    else 'medium' if self.lines.entropy[0] < 0.7
                    else 'low'
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(self.lines.oscillator[0]),
                'reliability': (
                    (1 - self.lines.entropy[0]) *
                    abs(self.lines.oscillator[0] - self.lines.signal[0])
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'chaos_risk': self.lines.entropy[0],
                'fractal_stability': (
                    np.std(self.fractal_history)
                    if len(self.fractal_history) > 1 else 0
                )
            }
        }
