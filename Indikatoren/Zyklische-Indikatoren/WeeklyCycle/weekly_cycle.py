import backtrader as bt
import numpy as np
from datetime import datetime, timedelta

class WeeklyCycle(bt.Indicator):
    """
    Weekly Cycle Indicator
    
    Ein fortgeschrittener Indikator zur Analyse von
    wöchentlichen Marktzyklen.
    
    Features:
    - Wöchentliche Zyklusanalyse
    - Saisonale Mustererkennung
    - Tagesbasierte Stärkeberechnung
    - Signalgenerierung
    
    Parameter:
    - lookback_weeks (12): Rückblickwochen
    - strength_threshold (0.6): Stärkeschwelle
    - pattern_length (5): Musterlänge in Tagen
    """
    
    lines = ('cycle', 'day_strength',
             'pattern_quality', 'seasonality',
             'signal')
             
    params = (
        ('lookback_weeks', 12),
        ('strength_threshold', 0.6),
        ('pattern_length', 5)
    )
    
    plotlines = dict(
        cycle=dict(color='blue', _name='Cycle'),
        day_strength=dict(color='red', _name='Day Strength'),
        pattern_quality=dict(color='green', _name='Pattern Quality'),
        seasonality=dict(color='purple', _name='Seasonality'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(WeeklyCycle, self).__init__()
        
        # Historie
        self.price_history = []
        self.day_history = []
        self.week_patterns = []
        
    def get_day_of_week(self, date):
        """
        Ermittelt den Wochentag (0-4, Montag-Freitag).
        """
        return date.weekday()
        
    def calculate_day_strength(self, day):
        """
        Berechnet die Stärke eines bestimmten Wochentags.
        """
        if len(self.price_history) < self.p.pattern_length:
            return 0
            
        # Preise für den spezifischen Tag sammeln
        day_prices = []
        for i, (price, d) in enumerate(
            zip(self.price_history, self.day_history)
        ):
            if d == day:
                day_prices.append(price)
                
        if len(day_prices) < 2:
            return 0
            
        # Durchschnittliche Rendite berechnen
        returns = np.diff(day_prices) / day_prices[:-1]
        return np.mean(returns)
        
    def calculate_pattern_quality(self):
        """
        Berechnet die Qualität des Wochenmusters.
        """
        if len(self.week_patterns) < 2:
            return 0
            
        # Korrelation zwischen aufeinanderfolgenden Wochen
        pattern1 = self.week_patterns[-1]
        pattern2 = self.week_patterns[-2]
        
        if len(pattern1) == len(pattern2):
            correlation = np.corrcoef(pattern1, pattern2)[0,1]
            return correlation if not np.isnan(correlation) else 0
            
        return 0
        
    def calculate_seasonality(self):
        """
        Berechnet die saisonale Stärke.
        """
        if len(self.week_patterns) < self.p.lookback_weeks:
            return 0
            
        # Wochenmuster vergleichen
        patterns = np.array(
            self.week_patterns[-self.p.lookback_weeks:]
        )
        
        if patterns.shape[0] >= 2:
            # Standardabweichung der Tagesmuster
            daily_std = np.std(patterns, axis=0)
            return 1 - np.mean(daily_std)
            
        return 0
        
    def next(self):
        # Datum und Preis speichern
        current_date = self.data.datetime.datetime(0)
        current_day = self.get_day_of_week(current_date)
        
        self.price_history.append(self.data.close[0])
        self.day_history.append(current_day)
        
        # Wochenmuster aktualisieren
        if len(self.price_history) >= self.p.pattern_length:
            if current_day == 4:  # Freitag
                # Neue Woche komplett
                week_prices = self.price_history[
                    -self.p.pattern_length:
                ]
                self.week_patterns.append(week_prices)
                
        # Tagesstärke
        day_strength = self.calculate_day_strength(
            current_day
        )
        
        # Musterqualität
        pattern_quality = self.calculate_pattern_quality()
        
        # Saisonalität
        seasonality = self.calculate_seasonality()
        
        # Zykluswert
        cycle = day_strength * pattern_quality
        
        # Linien aktualisieren
        self.lines.cycle[0] = cycle
        self.lines.day_strength[0] = day_strength
        self.lines.pattern_quality[0] = pattern_quality
        self.lines.seasonality[0] = seasonality
        
        # Signal
        if pattern_quality > self.p.strength_threshold:
            if day_strength > 0:
                self.lines.signal[0] = 1  # Kaufsignal
            elif day_strength < 0:
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_length = (
            self.p.lookback_weeks *
            self.p.pattern_length
        )
        for hist in [self.price_history,
                    self.day_history]:
            if len(hist) > max_length:
                hist.pop(0)
                
        if len(self.week_patterns) > self.p.lookback_weeks:
            self.week_patterns.pop(0)
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'cycle': {
                'value': self.lines.cycle[0],
                'day_strength': self.lines.day_strength[0],
                'quality': self.lines.pattern_quality[0],
                'seasonality': self.lines.seasonality[0]
            },
            'pattern_analysis': {
                'current_day': (
                    self.day_history[-1]
                    if self.day_history
                    else None
                ),
                'strength': (
                    'strong'
                    if abs(self.lines.day_strength[0]) > 0.01
                    else 'weak'
                ),
                'quality': (
                    'high'
                    if self.lines.pattern_quality[0] >
                       self.p.strength_threshold
                    else 'low'
                )
            },
            'seasonality': {
                'strength': (
                    'strong'
                    if self.lines.seasonality[0] > 0.7
                    else 'weak'
                ),
                'reliability': (
                    'reliable'
                    if len(self.week_patterns) >=
                       self.p.lookback_weeks
                    else 'developing'
                ),
                'consistency': (
                    'consistent'
                    if self.lines.pattern_quality[0] >
                       self.p.strength_threshold
                    else 'inconsistent'
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
                    self.lines.pattern_quality[0] *
                    abs(self.lines.day_strength[0])
                )
            },
            'market_conditions': {
                'pattern_quality': (
                    'optimal'
                    if (self.lines.pattern_quality[0] >
                        self.p.strength_threshold and
                        self.lines.seasonality[0] > 0.6)
                    else 'suboptimal'
                ),
                'day_bias': (
                    'favorable'
                    if abs(self.lines.day_strength[0]) > 0.008
                    else 'neutral'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.pattern_quality[0] >
                        self.p.strength_threshold * 0.9 and
                        abs(self.lines.day_strength[0]) > 0.005)
                    else 'unfavorable'
                )
            }
        }
