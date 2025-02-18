import backtrader as bt
import numpy as np

class WilliamsVIXFix(bt.Indicator):
    """
    Williams VIX Fix
    
    Ein Indikator, der Volatilitätsextreme und
    potenzielle Marktwendepunkte identifiziert.
    
    Features:
    - Volatilitätsanalyse
    - Marktwendepunkt-Erkennung
    - Adaptiver Lookback
    - Volatilitätsnormalisierung
    - Signal-Validierung
    
    Parameter:
    - period (22): Basisperiode
    - smooth_period (3): Glättungsperiode
    - high_low_period (10): High/Low Lookback
    """
    
    lines = ('vix_fix', 'smoothed_vix',
             'volatility_ratio', 'market_phase',
             'buy_signal', 'sell_signal',
             'upper', 'lower')
             
    params = (
        ('period', 22),
        ('smooth_period', 3),
        ('high_low_period', 10),
        ('upper_threshold', 80),
        ('lower_threshold', 20)
    )
    
    plotlines = dict(
        vix_fix=dict(color='blue', _name='VIX Fix'),
        smoothed_vix=dict(color='red', _name='Smoothed VIX'),
        volatility_ratio=dict(color='purple', _name='Volatility Ratio'),
        market_phase=dict(color='orange', _name='Market Phase'),
        upper=dict(color='gray', _name='Upper'),
        lower=dict(color='gray', _name='Lower'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(WilliamsVIXFix, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Historie
        self.vix_history = []
        self.price_history = []
        self.phase_history = []
        
    def calculate_vix_fix(self):
        """
        Berechnet den VIX Fix Wert.
        """
        if len(self.price_history) < self.p.period:
            return 0
            
        # Höchster Hochkurs
        highest_high = max(
            self.data.high.get(ago=-i, size=1)[0]
            for i in range(self.p.high_low_period)
        )
        
        # Niedrigster Tiefkurs
        lowest_low = min(
            self.data.low.get(ago=-i, size=1)[0]
            for i in range(self.p.high_low_period)
        )
        
        # Close-to-Close Volatilität
        close_vol = np.std([
            self.data.close.get(ago=-i, size=1)[0]
            for i in range(self.p.period)
        ])
        
        # High-Low Volatilität
        hl_vol = highest_high - lowest_low
        
        # VIX Fix Berechnung
        if hl_vol == 0:
            return 0
            
        vix_fix = (close_vol / hl_vol) * 100
        return min(100, max(0, vix_fix))
        
    def calculate_volatility_ratio(self):
        """
        Berechnet das Volatilitätsverhältnis.
        """
        if len(self.vix_history) < 2:
            return 0
            
        current_vol = self.vix_history[-1]
        prev_vol = self.vix_history[-2]
        
        if prev_vol == 0:
            return 0
            
        return current_vol / prev_vol
        
    def identify_market_phase(self):
        """
        Identifiziert die Marktphase.
        """
        if len(self.vix_history) < self.p.smooth_period:
            return 0
            
        # Durchschnittlicher VIX Fix
        avg_vix = np.mean(self.vix_history[-self.p.smooth_period:])
        
        # Marktphasen-Identifikation
        if avg_vix > self.p.upper_threshold:
            return 1  # Hohe Volatilität
        elif avg_vix < self.p.lower_threshold:
            return -1  # Niedrige Volatilität
        else:
            return 0  # Normale Volatilität
            
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.data[0])
        
        # VIX Fix berechnen
        self.lines.vix_fix[0] = self.calculate_vix_fix()
        self.vix_history.append(self.lines.vix_fix[0])
        
        # Geglätteter VIX Fix
        self.lines.smoothed_vix[0] = bt.indicators.EMA(
            self.lines.vix_fix, period=self.p.smooth_period
        )[0]
        
        # Volatilitätsverhältnis
        self.lines.volatility_ratio[0] = self.calculate_volatility_ratio()
        
        # Marktphase
        self.lines.market_phase[0] = self.identify_market_phase()
        self.phase_history.append(self.lines.market_phase[0])
        
        # Bänder
        self.lines.upper[0] = self.p.upper_threshold
        self.lines.lower[0] = self.p.lower_threshold
        
        # Historie begrenzen
        max_period = max(self.p.period, self.p.smooth_period)
        for hist in [self.vix_history, self.price_history, self.phase_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal (Volatilitätsextrem nach oben)
        if (self.lines.smoothed_vix[0] > self.p.upper_threshold and
            self.lines.volatility_ratio[0] < 1 and
            self.lines.market_phase[0] > 0):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal (Volatilitätsextrem nach unten)
        if (self.lines.smoothed_vix[0] < self.p.lower_threshold and
            self.lines.volatility_ratio[0] > 1 and
            self.lines.market_phase[0] < 0):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'volatility': {
                'vix_fix': self.lines.vix_fix[0],
                'smoothed': self.lines.smoothed_vix[0],
                'ratio': self.lines.volatility_ratio[0],
                'phase': (
                    'high' if self.lines.market_phase[0] > 0
                    else 'low' if self.lines.market_phase[0] < 0
                    else 'normal'
                )
            },
            'trend': {
                'direction': np.sign(
                    self.lines.smoothed_vix[0] -
                    self.lines.smoothed_vix[-1]
                ),
                'strength': abs(
                    self.lines.smoothed_vix[0] -
                    self.lines.smoothed_vix[-1]
                ),
                'persistence': (
                    np.mean([
                        1 if p == self.lines.market_phase[0]
                        else 0
                        for p in self.phase_history[-5:]
                    ]) if len(self.phase_history) >= 5
                    else 0
                )
            },
            'extremes': {
                'upper_distance': (
                    self.p.upper_threshold -
                    self.lines.smoothed_vix[0]
                ),
                'lower_distance': (
                    self.lines.smoothed_vix[0] -
                    self.p.lower_threshold
                ),
                'relative_position': (
                    (self.lines.smoothed_vix[0] -
                     self.p.lower_threshold) /
                    (self.p.upper_threshold -
                     self.p.lower_threshold)
                    if self.p.upper_threshold != self.p.lower_threshold
                    else 0
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(self.lines.market_phase[0]),
                'reliability': (
                    abs(self.lines.market_phase[0]) *
                    abs(1 - self.lines.volatility_ratio[0])
                )
            },
            'risk': {
                'current_volatility': self.vol[0],
                'vix_stability': (
                    np.std(self.vix_history)
                    if len(self.vix_history) > 1
                    else 0
                ),
                'phase_changes': (
                    sum(
                        1 if self.phase_history[i] != self.phase_history[i-1]
                        else 0
                        for i in range(1, len(self.phase_history))
                    ) if len(self.phase_history) > 1
                    else 0
                )
            }
        }
