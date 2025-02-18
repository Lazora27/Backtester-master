import backtrader as bt
import numpy as np
from datetime import datetime

class SeasonalStrength(bt.Indicator):
    """
    Seasonal Strength Indicator
    
    Ein fortgeschrittener Indikator zur Analyse saisonaler
    Marktstärke und -muster.
    
    Features:
    - Saisonale Mustererkennung
    - Stärkeanalyse
    - Trendqualitätsberechnung
    - Signalgenerierung
    
    Parameter:
    - lookback_years (5): Rückblickjahre
    - season_length (63): Saisonlänge in Tagen
    - strength_threshold (0.7): Stärkeschwelle
    """
    
    lines = ('seasonal_strength', 'pattern_quality',
             'trend_strength', 'cycle_position',
             'signal')
             
    params = (
        ('lookback_years', 5),
        ('season_length', 63),
        ('strength_threshold', 0.7)
    )
    
    plotlines = dict(
        seasonal_strength=dict(color='blue', _name='Seasonal Strength'),
        pattern_quality=dict(color='red', _name='Pattern Quality'),
        trend_strength=dict(color='green', _name='Trend Strength'),
        cycle_position=dict(color='purple', _name='Cycle Position'),
        signal=dict(_name='Signal', color='black', marker='o')
    )
    
    def __init__(self):
        super(SeasonalStrength, self).__init__()
        
        # Historie
        self.price_history = []
        self.seasonal_patterns = {}
        self.current_pattern = []
        
    def get_season_day(self, date):
        """
        Ermittelt den Tag innerhalb der Saison.
        """
        return date.timetuple().tm_yday % self.p.season_length
        
    def calculate_seasonal_pattern(self):
        """
        Berechnet das saisonale Muster.
        """
        if len(self.price_history) < self.p.season_length:
            return np.zeros(self.p.season_length)
            
        # Preise in Saisons aufteilen
        seasons = {}
        for i in range(len(self.price_history)):
            date = self.data.datetime.datetime(-i)
            season_day = self.get_season_day(date)
            year = date.year
            
            if year not in seasons:
                seasons[year] = {}
                
            seasons[year][season_day] = self.price_history[i]
            
        # Saisonale Renditen berechnen
        pattern = np.zeros(self.p.season_length)
        count = np.zeros(self.p.season_length)
        
        for year in seasons:
            if len(seasons[year]) >= self.p.season_length:
                year_pattern = np.zeros(self.p.season_length)
                for day in range(self.p.season_length):
                    if day in seasons[year]:
                        year_pattern[day] = seasons[year][day]
                        count[day] += 1
                        
                # Normalisieren
                year_pattern = (
                    year_pattern - np.mean(year_pattern)
                ) / np.std(year_pattern)
                pattern += year_pattern
                
        # Durchschnitt berechnen
        pattern = np.where(
            count > 0,
            pattern / count,
            0
        )
        
        return pattern
        
    def calculate_pattern_quality(self, pattern):
        """
        Berechnet die Qualität des saisonalen Musters.
        """
        if len(self.current_pattern) < self.p.season_length:
            return 0
            
        current = np.array(
            self.current_pattern[-self.p.season_length:]
        )
        current = (
            current - np.mean(current)
        ) / np.std(current)
        
        correlation = np.corrcoef(current, pattern)[0,1]
        return correlation if not np.isnan(correlation) else 0
        
    def calculate_trend_strength(self):
        """
        Berechnet die Trendstärke.
        """
        if len(self.price_history) < self.p.season_length:
            return 0
            
        prices = np.array(
            self.price_history[-self.p.season_length:]
        )
        trend = np.polyfit(
            range(len(prices)),
            prices,
            1
        )[0]
        
        return trend / np.mean(prices)
        
    def next(self):
        # Preis speichern
        self.price_history.append(self.data.close[0])
        self.current_pattern.append(self.data.close[0])
        
        # Saisonales Muster berechnen
        pattern = self.calculate_seasonal_pattern()
        
        # Aktuelle Position im Zyklus
        current_day = self.get_season_day(
            self.data.datetime.datetime(0)
        )
        
        # Musterqualität
        pattern_quality = self.calculate_pattern_quality(
            pattern
        )
        
        # Trendstärke
        trend_strength = self.calculate_trend_strength()
        
        # Saisonale Stärke
        seasonal_strength = pattern[current_day]
        
        # Linien aktualisieren
        self.lines.seasonal_strength[0] = seasonal_strength
        self.lines.pattern_quality[0] = pattern_quality
        self.lines.trend_strength[0] = trend_strength
        self.lines.cycle_position[0] = (
            current_day / self.p.season_length
        )
        
        # Signal
        if pattern_quality > self.p.strength_threshold:
            if seasonal_strength > 0:
                self.lines.signal[0] = 1  # Kaufsignal
            elif seasonal_strength < 0:
                self.lines.signal[0] = -1  # Verkaufssignal
            else:
                self.lines.signal[0] = 0
        else:
            self.lines.signal[0] = 0
            
        # Historie begrenzen
        max_period = (
            self.p.lookback_years * 365 +
            self.p.season_length
        )
        for hist in [self.price_history,
                    self.current_pattern]:
            if len(hist) > max_period:
                hist.pop(0)
                
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'seasonal': {
                'strength': self.lines.seasonal_strength[0],
                'quality': self.lines.pattern_quality[0],
                'trend': self.lines.trend_strength[0],
                'position': self.lines.cycle_position[0]
            },
            'pattern_state': {
                'quality': (
                    'high'
                    if self.lines.pattern_quality[0] >
                       self.p.strength_threshold
                    else 'low'
                ),
                'reliability': (
                    self.lines.pattern_quality[0] /
                    self.p.strength_threshold
                ),
                'consistency': (
                    'stable'
                    if self.lines.pattern_quality[0] >
                       self.p.strength_threshold * 0.8
                    else 'unstable'
                )
            },
            'cycle_analysis': {
                'position': (
                    'early'
                    if self.lines.cycle_position[0] < 0.33
                    else 'middle'
                    if self.lines.cycle_position[0] < 0.66
                    else 'late'
                ),
                'strength': abs(
                    self.lines.seasonal_strength[0]
                ),
                'trend_alignment': (
                    'aligned'
                    if (self.lines.seasonal_strength[0] *
                        self.lines.trend_strength[0] > 0)
                    else 'divergent'
                )
            },
            'signals': {
                'current': (
                    'buy' if self.lines.signal[0] > 0
                    else 'sell' if self.lines.signal[0] < 0
                    else 'none'
                ),
                'strength': abs(self.lines.signal[0]),
                'confidence': (
                    self.lines.pattern_quality[0] *
                    abs(self.lines.seasonal_strength[0])
                )
            },
            'market_conditions': {
                'seasonal_quality': (
                    'optimal'
                    if (self.lines.pattern_quality[0] >
                        self.p.strength_threshold and
                        abs(self.lines.seasonal_strength[0]) > 0.5)
                    else 'suboptimal'
                ),
                'trend_structure': (
                    'clear'
                    if abs(self.lines.trend_strength[0]) > 0.01
                    else 'unclear'
                ),
                'trading_environment': (
                    'favorable'
                    if (self.lines.pattern_quality[0] >
                        self.p.strength_threshold * 0.9 and
                        abs(self.lines.seasonal_strength[0]) > 0.4 and
                        abs(self.lines.trend_strength[0]) > 0.008)
                    else 'unfavorable'
                )
            }
        }
