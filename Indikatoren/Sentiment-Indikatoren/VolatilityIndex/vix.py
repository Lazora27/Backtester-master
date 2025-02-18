import backtrader as bt
import numpy as np
from datetime import datetime, timedelta

class VolatilityIndex(bt.Indicator):
    """
    VIX-Style Volatility Index
    
    Erweiterte Version mit:
    - Implizierte Volatilität
    - Term-Struktur Analyse
    - Volatilitäts-Skew
    - Regime Detection
    - Multi-Timeframe Integration
    
    Features:
    - Historische Volatilität
    - Implizierte Volatilität (simuliert)
    - Volatilitäts-Term-Struktur
    - Volatilitäts-Regime
    - Extremwert-Erkennung
    
    Parameter:
    - period (20): Basisperiode für Berechnungen
    - fast_period (10): Schnelle Periode
    - slow_period (30): Langsame Periode
    - regime_period (50): Periode für Regime-Erkennung
    - extreme_threshold (2.0): Schwelle für Extreme
    """
    
    lines = ('hist_vol', 'impl_vol',
             'term_structure', 'vol_regime',
             'vol_skew', 'composite_vix',
             'regime_state', 'extreme_signal',
             'term_signal', 'skew_signal')
             
    params = (
        ('period', 20),
        ('fast_period', 10),
        ('slow_period', 30),
        ('regime_period', 50),
        ('extreme_threshold', 2.0)
    )
    
    plotlines = dict(
        hist_vol=dict(color='blue', _name='Historical Vol'),
        impl_vol=dict(color='red', _name='Implied Vol'),
        term_structure=dict(color='green', _name='Term Structure'),
        vol_regime=dict(color='purple', _name='Volatility Regime'),
        vol_skew=dict(color='orange', _name='Volatility Skew'),
        composite_vix=dict(color='black', _name='Composite VIX'),
        regime_state=dict(_name='Regime', color='gray'),
        extreme_signal=dict(_name='Extreme', color='red', marker='o'),
        term_signal=dict(_name='Term', color='green', marker='^'),
        skew_signal=dict(_name='Skew', color='blue', marker='v')
    )
    
    def __init__(self):
        super(VolatilityIndex, self).__init__()
        
        # Historische Volatilität
        self.hist_vol_fast = bt.indicators.StandardDeviation(
            self.data,
            period=self.p.fast_period
        )
        self.hist_vol_slow = bt.indicators.StandardDeviation(
            self.data,
            period=self.p.slow_period
        )
        
        # Gleitende Durchschnitte
        self.sma_fast = bt.indicators.SMA(
            self.data,
            period=self.p.fast_period
        )
        self.sma_slow = bt.indicators.SMA(
            self.data,
            period=self.p.slow_period
        )
        
        # ATR für Volatilitäts-Regime
        self.atr = bt.indicators.ATR(
            period=self.p.regime_period
        )
        
        # Speicher für historische Werte
        self.vol_history = []
        self.regime_history = []
        
    def simulate_implied_volatility(self):
        """
        Simuliert die implizierte Volatilität basierend auf
        historischer Volatilität und Marktbedingungen.
        """
        hist_vol = self.hist_vol_fast[0] * 100  # In Prozent
        
        # Marktbedingungen simulieren
        market_condition = np.sin(len(self) / 20) * 10
        
        # Basis IV = HV +/- Marktbedingungen
        impl_vol = hist_vol + market_condition
        
        # Volatilitäts-Risk-Premium
        vol_premium = max(0, (impl_vol - hist_vol) * 0.5)
        
        return max(1, impl_vol + vol_premium)
        
    def calculate_term_structure(self):
        """
        Berechnet die Volatilitäts-Term-Struktur.
        Positiv = Contango, Negativ = Backwardation
        """
        if self.hist_vol_slow[0] != 0:
            term = (
                (self.hist_vol_fast[0] / self.hist_vol_slow[0] - 1) * 100
            )
        else:
            term = 0
            
        return max(-100, min(100, term))
        
    def calculate_volatility_skew(self):
        """
        Berechnet den Volatilitäts-Skew basierend auf
        Preis- und Volumenbewegungen.
        """
        # Preisbewegung analysieren
        price_range = (
            self.data.high[0] - self.data.low[0]
        ) / self.data.close[0]
        
        # Volumen-gewichtete Preisbewegung
        vol_price = price_range * (
            self.data.volume[0] / bt.indicators.SMA(
                self.data.volume, period=20
            )[0]
        )
        
        # Skew berechnen (-100 bis +100)
        skew = (vol_price - np.mean(self.vol_history[-20:])) * 1000
        return max(-100, min(100, skew))
        
    def detect_volatility_regime(self):
        """
        Erkennt das aktuelle Volatilitäts-Regime.
        Returns:
        - 0: Niedrige Volatilität
        - 50: Normale Volatilität
        - 100: Hohe Volatilität
        """
        current_vol = self.hist_vol_fast[0]
        
        if len(self.vol_history) < 20:
            return 50
            
        vol_mean = np.mean(self.vol_history)
        vol_std = np.std(self.vol_history)
        
        if current_vol > vol_mean + vol_std:
            return 100  # Hohe Volatilität
        elif current_vol < vol_mean - vol_std:
            return 0   # Niedrige Volatilität
        else:
            return 50  # Normale Volatilität
            
    def next(self):
        # Historische Volatilität (annualisiert)
        hist_vol = self.hist_vol_fast[0] * np.sqrt(252) * 100
        self.lines.hist_vol[0] = hist_vol
        
        # Implizierte Volatilität
        self.lines.impl_vol[0] = self.simulate_implied_volatility()
        
        # Term-Struktur
        self.lines.term_structure[0] = self.calculate_term_structure()
        
        # Volatilitäts-Skew
        self.lines.vol_skew[0] = self.calculate_volatility_skew()
        
        # Historie aktualisieren
        self.vol_history.append(hist_vol)
        if len(self.vol_history) > self.p.regime_period:
            self.vol_history.pop(0)
            
        # Volatilitäts-Regime
        regime = self.detect_volatility_regime()
        self.lines.vol_regime[0] = regime
        self.regime_history.append(regime)
        if len(self.regime_history) > self.p.regime_period:
            self.regime_history.pop(0)
            
        # Composite VIX (gewichteter Durchschnitt)
        self.lines.composite_vix[0] = (
            self.lines.hist_vol[0] * 0.3 +
            self.lines.impl_vol[0] * 0.3 +
            self.lines.term_structure[0] * 0.2 +
            self.lines.vol_skew[0] * 0.2
        )
        
        # Regime State
        self.lines.regime_state[0] = regime
        
        # Signale
        # Extremes Signal
        if abs(self.lines.composite_vix[0]) > self.p.extreme_threshold * np.std(
            self.vol_history
        ):
            self.lines.extreme_signal[0] = self.lines.composite_vix[0]
        else:
            self.lines.extreme_signal[0] = float('nan')
            
        # Term Structure Signal
        if abs(self.lines.term_structure[0]) > 20:  # 20% Schwelle
            self.lines.term_signal[0] = self.data.close[0]
        else:
            self.lines.term_signal[0] = float('nan')
            
        # Skew Signal
        if abs(self.lines.vol_skew[0]) > 30:  # 30% Schwelle
            self.lines.skew_signal[0] = self.data.close[0]
        else:
            self.lines.skew_signal[0] = float('nan')
