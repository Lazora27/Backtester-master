import backtrader as bt
import numpy as np
from scipy import stats

class ForecastOscillator(bt.Indicator):
    """
    Forecast Oscillator
    
    Ein prädiktiver Momentum-Indikator, der lineare Regression
    verwendet, um zukünftige Preisbewegungen zu prognostizieren.
    
    Features:
    - Lineare Regression
    - Prognoseberechnung
    - Konfidenzintervalle
    - Trendstärke-Analyse
    - Signal-Validierung
    
    Parameter:
    - period (14): Basisperiode
    - forecast_period (5): Prognoseperiode
    - confidence_level (0.95): Konfidenzniveau
    - smooth_period (3): Glättungsperiode
    """
    
    lines = ('forecast', 'oscillator', 'upper_band',
             'lower_band', 'r_squared', 'confidence',
             'buy_signal', 'sell_signal')
             
    params = (
        ('period', 14),
        ('forecast_period', 5),
        ('confidence_level', 0.95),
        ('smooth_period', 3)
    )
    
    plotlines = dict(
        forecast=dict(color='blue', _name='Forecast'),
        oscillator=dict(color='green', _name='Oscillator'),
        upper_band=dict(color='red', _name='Upper Band'),
        lower_band=dict(color='red', _name='Lower Band'),
        r_squared=dict(color='gray', _name='R-Squared'),
        confidence=dict(color='purple', _name='Confidence'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(ForecastOscillator, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Glättung
        self.ema = bt.indicators.EMA(period=self.p.smooth_period)
        
        # Historie
        self.price_history = []
        self.forecast_history = []
        self.oscillator_history = []
        
    def linear_regression(self, y):
        """
        Führt eine lineare Regression durch.
        """
        if len(y) < 2:
            return 0, 0, 0, 0
            
        x = np.arange(len(y))
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        
        return slope, intercept, r_value**2, std_err
        
    def calculate_forecast(self, slope, intercept, std_err):
        """
        Berechnet die Prognose mit Konfidenzintervallen.
        """
        x_forecast = len(self.price_history) + self.p.forecast_period
        
        # Punktprognose
        forecast = slope * x_forecast + intercept
        
        # Konfidenzintervalle
        t_value = stats.t.ppf(
            (1 + self.p.confidence_level) / 2,
            len(self.price_history) - 2
        )
        margin = t_value * std_err
        
        upper = forecast + margin
        lower = forecast - margin
        
        return forecast, upper, lower
        
    def calculate_oscillator(self, current, forecast):
        """
        Berechnet den Oszillator-Wert.
        """
        if current == 0:
            return 0
            
        return ((forecast - current) / current) * 100
        
    def next(self):
        # Preisdaten aktualisieren
        self.price_history.append(self.data[0])
        if len(self.price_history) > self.p.period:
            self.price_history.pop(0)
            
        # Regression durchführen
        if len(self.price_history) >= self.p.period:
            slope, intercept, r_squared, std_err = self.linear_regression(
                self.price_history
            )
            
            # Prognose berechnen
            forecast, upper, lower = self.calculate_forecast(
                slope, intercept, std_err
            )
            
            # Oszillator berechnen
            oscillator = self.calculate_oscillator(
                self.data[0], forecast
            )
            
            # Werte speichern
            self.lines.forecast[0] = forecast
            self.lines.oscillator[0] = oscillator
            self.lines.upper_band[0] = upper
            self.lines.lower_band[0] = lower
            self.lines.r_squared[0] = r_squared
            self.lines.confidence[0] = (
                1 - (upper - lower) / self.data[0]
                if self.data[0] != 0 else 0
            )
        else:
            # Standardwerte
            self.lines.forecast[0] = self.data[0]
            self.lines.oscillator[0] = 0
            self.lines.upper_band[0] = self.data[0]
            self.lines.lower_band[0] = self.data[0]
            self.lines.r_squared[0] = 0
            self.lines.confidence[0] = 0
            
        # Historie aktualisieren
        self.forecast_history.append(self.lines.forecast[0])
        self.oscillator_history.append(self.lines.oscillator[0])
        
        if len(self.forecast_history) > self.p.period:
            self.forecast_history.pop(0)
            self.oscillator_history.pop(0)
            
        # Signal-Generierung
        # Buy Signal
        if (self.lines.oscillator[0] > 0 and
            self.lines.r_squared[0] > 0.7 and
            self.lines.confidence[0] > 0.8):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.oscillator[0] < 0 and
            self.lines.r_squared[0] > 0.7 and
            self.lines.confidence[0] > 0.8):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'forecast': {
                'value': self.lines.forecast[0],
                'current': self.data[0],
                'difference': self.lines.forecast[0] - self.data[0],
                'percent_change': (
                    (self.lines.forecast[0] - self.data[0]) /
                    self.data[0] * 100 if self.data[0] != 0 else 0
                )
            },
            'oscillator': {
                'value': self.lines.oscillator[0],
                'trend': (
                    'up' if self.lines.oscillator[0] > 0
                    else 'down'
                ),
                'strength': abs(self.lines.oscillator[0]),
                'momentum': (
                    self.lines.oscillator[0] -
                    self.oscillator_history[-2]
                    if len(self.oscillator_history) > 1
                    else 0
                )
            },
            'quality': {
                'r_squared': self.lines.r_squared[0],
                'confidence': self.lines.confidence[0],
                'forecast_stability': (
                    np.std(self.forecast_history)
                    if self.forecast_history else 0
                ),
                'oscillator_stability': (
                    np.std(self.oscillator_history)
                    if self.oscillator_history else 0
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(self.lines.oscillator[0]),
                'reliability': (
                    self.lines.r_squared[0] *
                    self.lines.confidence[0]
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'forecast_error': (
                    self.lines.upper_band[0] -
                    self.lines.lower_band[0]
                ),
                'prediction_risk': 1 - self.lines.confidence[0]
            }
        }
