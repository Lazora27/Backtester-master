import backtrader as bt
import numpy as np
from scipy import stats

class LinearRegressionTrend(bt.Indicator):
    """
    Linear Regression Trend Indicator
    
    Ein fortgeschrittener Trendfolge-Indikator basierend auf linearer
    Regression mit zusätzlichen statistischen Analysen.
    
    Features:
    - Lineare Regression Berechnung
    - R-Quadrat Analyse
    - Standardfehler Berechnung
    - Konfidenzintervalle
    - Trend-Projektion
    
    Parameter:
    - period (20): Basisperiode für Regression
    - confidence (0.95): Konfidenzintervall
    - forecast_period (5): Prognoseperiode
    - min_r_squared (0.7): Minimales R² für valide Trends
    """
    
    lines = ('regression', 'upper_band', 'lower_band',
             'forecast', 'r_squared', 'slope',
             'standard_error', 'trend_strength',
             'buy_signal', 'sell_signal')
             
    params = (
        ('period', 20),
        ('confidence', 0.95),
        ('forecast_period', 5),
        ('min_r_squared', 0.7)
    )
    
    plotlines = dict(
        regression=dict(color='blue', _name='Regression'),
        upper_band=dict(color='gray', _name='Upper Band'),
        lower_band=dict(color='gray', _name='Lower Band'),
        forecast=dict(color='green', _name='Forecast'),
        r_squared=dict(color='purple', _name='R²'),
        slope=dict(color='orange', _name='Slope'),
        standard_error=dict(color='red', _name='Std Error'),
        trend_strength=dict(color='brown', _name='Trend Strength'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(LinearRegressionTrend, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.volume_sma = bt.indicators.SMA(
            self.data.volume, period=self.p.period
        )
        
        # Historie
        self.price_history = []
        self.slope_history = []
        self.error_history = []
        
    def calculate_regression(self):
        """
        Berechnet die lineare Regression und statistische Metriken.
        """
        if len(self.price_history) < self.p.period:
            return None
            
        # Daten vorbereiten
        y = np.array(self.price_history[-self.p.period:])
        x = np.arange(len(y))
        
        # Regression berechnen
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        
        # Regressionslinie
        line = slope * x + intercept
        
        # R-Quadrat
        r_squared = r_value ** 2
        
        # Standardfehler der Regression
        residuals = y - line
        std_error = np.sqrt(np.sum(residuals**2) / (len(y)-2))
        
        # Konfidenzintervalle
        confidence = stats.t.ppf(self.p.confidence, len(y)-2)
        margin = confidence * std_error
        
        upper_band = line + margin
        lower_band = line - margin
        
        # Prognose
        forecast_x = np.arange(len(y), len(y) + self.p.forecast_period)
        forecast = slope * forecast_x + intercept
        
        return {
            'line': line[-1],
            'upper': upper_band[-1],
            'lower': lower_band[-1],
            'forecast': forecast[0],
            'r_squared': r_squared,
            'slope': slope,
            'std_error': std_error
        }
        
    def calculate_trend_strength(self, regression_results):
        """
        Berechnet die Trendstärke basierend auf mehreren Faktoren.
        """
        if regression_results is None:
            return 0
            
        # R-Quadrat Gewichtung
        r_squared_weight = regression_results['r_squared']
        
        # Steigung Gewichtung
        slope_weight = min(abs(regression_results['slope']), 1.0)
        
        # Fehler Gewichtung
        error_weight = max(0, 1 - regression_results['std_error'])
        
        # Kombinierte Trendstärke (0-1)
        strength = (r_squared_weight + slope_weight + error_weight) / 3
        
        return strength
        
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.data[0])
        if len(self.price_history) > self.p.period * 2:
            self.price_history.pop(0)
            
        # Regression berechnen
        results = self.calculate_regression()
        
        if results is not None:
            # Linien aktualisieren
            self.lines.regression[0] = results['line']
            self.lines.upper_band[0] = results['upper']
            self.lines.lower_band[0] = results['lower']
            self.lines.forecast[0] = results['forecast']
            self.lines.r_squared[0] = results['r_squared']
            self.lines.slope[0] = results['slope']
            self.lines.standard_error[0] = results['std_error']
            
            # Trendstärke
            strength = self.calculate_trend_strength(results)
            self.lines.trend_strength[0] = strength
            
            # Historie aktualisieren
            self.slope_history.append(results['slope'])
            self.error_history.append(results['std_error'])
            if len(self.slope_history) > self.p.period:
                self.slope_history.pop(0)
                self.error_history.pop(0)
                
            # Signal-Generierung
            current_price = self.data[0]
            
            # Buy Signal
            if (results['r_squared'] > self.p.min_r_squared and
                results['slope'] > 0 and
                strength > 0.7 and
                current_price > results['line']):
                self.lines.buy_signal[0] = self.data.low[0]
            else:
                self.lines.buy_signal[0] = float('nan')
                
            # Sell Signal
            if (results['r_squared'] > self.p.min_r_squared and
                results['slope'] < 0 and
                strength > 0.7 and
                current_price < results['line']):
                self.lines.sell_signal[0] = self.data.high[0]
            else:
                self.lines.sell_signal[0] = float('nan')
        else:
            # Standardwerte wenn keine Regression möglich
            self.lines.regression[0] = self.data[0]
            self.lines.upper_band[0] = self.data[0]
            self.lines.lower_band[0] = self.data[0]
            self.lines.forecast[0] = self.data[0]
            self.lines.r_squared[0] = 0
            self.lines.slope[0] = 0
            self.lines.standard_error[0] = 0
            self.lines.trend_strength[0] = 0
            self.lines.buy_signal[0] = float('nan')
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'regression': {
                'current': self.lines.regression[0],
                'forecast': self.lines.forecast[0],
                'r_squared': self.lines.r_squared[0],
                'slope': self.lines.slope[0],
                'std_error': self.lines.standard_error[0]
            },
            'bands': {
                'upper': self.lines.upper_band[0],
                'lower': self.lines.lower_band[0],
                'width': (
                    self.lines.upper_band[0] -
                    self.lines.lower_band[0]
                )
            },
            'trend': {
                'strength': self.lines.trend_strength[0],
                'direction': ('up' if self.lines.slope[0] > 0
                            else 'down'),
                'quality': ('high' if self.lines.r_squared[0] > self.p.min_r_squared
                          else 'low'),
                'stability': np.std(self.slope_history) if self.slope_history else 0
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'confidence': self.p.confidence,
                'forecast_reliability': (
                    self.lines.r_squared[0] *
                    (1 - self.lines.standard_error[0])
                )
            },
            'risk': {
                'atr': self.atr[0],
                'volatility': self.lines.standard_error[0],
                'forecast_error': np.mean(self.error_history) if self.error_history else 0
            }
        }
