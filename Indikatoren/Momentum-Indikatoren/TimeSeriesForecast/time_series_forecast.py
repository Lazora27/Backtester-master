import backtrader as bt
import numpy as np
from scipy import stats

class TimeSeriesForecast(bt.Indicator):
    """
    Time Series Forecast Indicator
    
    Ein fortgeschrittener Indikator, der lineare Regression
    und Zeitreihenanalyse verwendet, um Preisbewegungen
    vorherzusagen.
    
    Features:
    - Lineare Regression
    - Konfidenzintervalle
    - Trendstärke-Analyse
    - Prognosegenauigkeit
    - Signal-Validierung
    
    Parameter:
    - period (14): Regressionsperiode
    - forecast_period (5): Vorhersageperiode
    - confidence_level (0.95): Konfidenzniveau
    """
    
    lines = ('forecast', 'upper_band', 'lower_band',
             'trend_strength', 'accuracy',
             'buy_signal', 'sell_signal')
             
    params = (
        ('period', 14),
        ('forecast_period', 5),
        ('confidence_level', 0.95),
        ('min_slope', 0.1)
    )
    
    plotlines = dict(
        forecast=dict(color='blue', _name='Forecast'),
        upper_band=dict(color='gray', _name='Upper Band'),
        lower_band=dict(color='gray', _name='Lower Band'),
        trend_strength=dict(color='purple', _name='Trend Strength'),
        accuracy=dict(color='orange', _name='Accuracy'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(TimeSeriesForecast, self).__init__()
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Historie
        self.price_history = []
        self.forecast_history = []
        self.error_history = []
        
    def calculate_forecast(self):
        """
        Berechnet die Preisprognose mittels linearer Regression.
        """
        if len(self.price_history) < self.p.period:
            return self.data[0], 0, 0, 0
            
        # X und Y Daten für Regression
        x = np.arange(self.p.period)
        y = np.array(self.price_history[-self.p.period:])
        
        # Lineare Regression
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        
        # Prognose
        next_x = self.p.period + self.p.forecast_period - 1
        forecast = slope * next_x + intercept
        
        # Konfidenzintervalle
        confidence = stats.t.ppf(
            (1 + self.p.confidence_level) / 2,
            self.p.period - 2
        )
        
        std_dev = np.sqrt(
            np.sum((y - (slope * x + intercept)) ** 2) /
            (self.p.period - 2)
        )
        
        margin = confidence * std_dev * np.sqrt(
            1 / self.p.period +
            (next_x - np.mean(x)) ** 2 /
            np.sum((x - np.mean(x)) ** 2)
        )
        
        return forecast, forecast + margin, forecast - margin, abs(slope)
        
    def calculate_accuracy(self):
        """
        Berechnet die Prognosegenauigkeit.
        """
        if len(self.error_history) < self.p.period:
            return 0
            
        # Mittlerer absoluter prozentualer Fehler (MAPE)
        mape = np.mean([
            abs(e) for e in self.error_history[-self.p.period:]
        ])
        
        return max(0, 1 - mape)
        
    def next(self):
        # Historie aktualisieren
        self.price_history.append(self.data[0])
        
        # Prognose berechnen
        forecast, upper, lower, slope = self.calculate_forecast()
        
        self.lines.forecast[0] = forecast
        self.lines.upper_band[0] = upper
        self.lines.lower_band[0] = lower
        
        # Trendstärke
        self.lines.trend_strength[0] = min(1.0, slope)
        
        # Prognosegenauigkeit
        if len(self.forecast_history) > 0:
            error = (
                (self.data[0] - self.forecast_history[-1]) /
                self.forecast_history[-1]
                if self.forecast_history[-1] != 0
                else 0
            )
            self.error_history.append(error)
            
        self.lines.accuracy[0] = self.calculate_accuracy()
        
        # Forecast Historie aktualisieren
        self.forecast_history.append(forecast)
        
        # Historie begrenzen
        max_period = max(self.p.period, self.p.forecast_period)
        for hist in [self.price_history, self.forecast_history, self.error_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.forecast[0] > self.data[0] * (1 + self.p.min_slope) and
            self.lines.trend_strength[0] > self.p.min_slope and
            self.lines.accuracy[0] > 0.7):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.forecast[0] < self.data[0] * (1 - self.p.min_slope) and
            self.lines.trend_strength[0] > self.p.min_slope and
            self.lines.accuracy[0] > 0.7):
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
                'upper_band': self.lines.upper_band[0],
                'lower_band': self.lines.lower_band[0],
                'confidence_width': (
                    self.lines.upper_band[0] -
                    self.lines.lower_band[0]
                )
            },
            'trend': {
                'direction': np.sign(
                    self.lines.forecast[0] - self.data[0]
                ),
                'strength': self.lines.trend_strength[0],
                'momentum': (
                    self.lines.forecast[0] -
                    self.forecast_history[-2]
                    if len(self.forecast_history) > 1
                    else 0
                )
            },
            'accuracy': {
                'current': self.lines.accuracy[0],
                'mean_error': (
                    np.mean(self.error_history)
                    if len(self.error_history) > 0
                    else 0
                ),
                'std_error': (
                    np.std(self.error_history)
                    if len(self.error_history) > 1
                    else 0
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': self.lines.trend_strength[0],
                'reliability': (
                    self.lines.trend_strength[0] *
                    self.lines.accuracy[0]
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'forecast_stability': (
                    np.std(self.forecast_history)
                    if len(self.forecast_history) > 1
                    else 0
                ),
                'confidence_level': self.p.confidence_level
            }
        }
