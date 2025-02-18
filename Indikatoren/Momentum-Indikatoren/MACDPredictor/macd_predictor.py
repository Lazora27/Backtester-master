import backtrader as bt
import numpy as np
from scipy import stats

class MACDPredictor(bt.Indicator):
    """
    MACD Predictor Indicator
    
    Ein prädiktiver MACD-Indikator, der Regressionsanalyse und
    Zeitreihenprognose verwendet.
    
    Features:
    - MACD-Prognose
    - Trend-Extrapolation
    - Konfidenzintervalle
    - Mustervorhersage
    - Signal-Validierung
    
    Parameter:
    - fast_period (12): Schnelle EMA Periode
    - slow_period (26): Langsame EMA Periode
    - signal_period (9): Signal EMA Periode
    - forecast_period (5): Prognoseperiode
    - confidence_level (0.95): Konfidenzniveau
    """
    
    lines = ('macd', 'signal', 'forecast',
             'upper_band', 'lower_band',
             'prediction_error', 'confidence',
             'buy_signal', 'sell_signal')
             
    params = (
        ('fast_period', 12),
        ('slow_period', 26),
        ('signal_period', 9),
        ('forecast_period', 5),
        ('confidence_level', 0.95)
    )
    
    plotlines = dict(
        macd=dict(color='blue', _name='MACD'),
        signal=dict(color='red', _name='Signal'),
        forecast=dict(color='green', _name='Forecast'),
        upper_band=dict(color='gray', _name='Upper Band'),
        lower_band=dict(color='gray', _name='Lower Band'),
        prediction_error=dict(color='purple', _name='Pred Error'),
        confidence=dict(color='orange', _name='Confidence'),
        buy_signal=dict(_name='Buy', color='green', marker='^'),
        sell_signal=dict(_name='Sell', color='red', marker='v')
    )
    
    def __init__(self):
        super(MACDPredictor, self).__init__()
        
        # MACD-Komponenten
        self.fast_ma = bt.indicators.EMA(period=self.p.fast_period)
        self.slow_ma = bt.indicators.EMA(period=self.p.slow_period)
        
        # Technische Indikatoren
        self.atr = bt.indicators.ATR(period=14)
        self.vol = bt.indicators.StdDev(period=20)
        
        # Historie
        self.macd_history = []
        self.forecast_history = []
        self.error_history = []
        
    def linear_regression_forecast(self, data, periods):
        """
        Führt eine lineare Regression durch und prognostiziert zukünftige Werte.
        """
        if len(data) < 2:
            return 0, 0, 0, 0
            
        x = np.arange(len(data))
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, data)
        
        # Prognose
        forecast = slope * (len(data) + periods) + intercept
        
        # Konfidenzintervalle
        conf = stats.t.ppf(
            (1 + self.p.confidence_level) / 2,
            len(data) - 2
        )
        margin = conf * std_err
        
        upper = forecast + margin
        lower = forecast - margin
        
        return forecast, upper, lower, r_value**2
        
    def calculate_prediction_error(self):
        """
        Berechnet den Prognosefehler.
        """
        if len(self.macd_history) < self.p.forecast_period + 1 or len(self.forecast_history) < 1:
            return 0
            
        actual = self.macd_history[-1]
        forecast = self.forecast_history[-1]
        
        if actual == 0:
            return 0
            
        return abs((actual - forecast) / actual)
        
    def exponential_smoothing(self, data, alpha=0.2):
        """
        Führt eine exponentielle Glättung durch.
        """
        if len(data) < 2:
            return data[-1] if data else 0
            
        result = data[0]
        for n in range(1, len(data)):
            result = alpha * data[n] + (1 - alpha) * result
            
        return result
        
    def next(self):
        # MACD berechnen
        self.lines.macd[0] = self.fast_ma[0] - self.slow_ma[0]
        
        # Signal-Linie
        self.lines.signal[0] = bt.indicators.EMA(
            self.lines.macd, period=self.p.signal_period
        )[0]
        
        # Historie aktualisieren
        self.macd_history.append(self.lines.macd[0])
        
        # Prognose
        if len(self.macd_history) >= self.p.signal_period:
            forecast, upper, lower, r_squared = self.linear_regression_forecast(
                self.macd_history[-self.p.signal_period:],
                self.p.forecast_period
            )
            
            # Geglättete Prognose
            smoothed_forecast = self.exponential_smoothing(
                self.forecast_history + [forecast]
                if self.forecast_history
                else [forecast]
            )
            
            self.lines.forecast[0] = smoothed_forecast
            self.lines.upper_band[0] = upper
            self.lines.lower_band[0] = lower
            
            # Prognosefehler
            error = self.calculate_prediction_error()
            self.lines.prediction_error[0] = error
            self.error_history.append(error)
            
            # Konfidenz
            self.lines.confidence[0] = (
                (1 - error) * r_squared
                if error <= 1
                else 0
            )
            
            # Prognose speichern
            self.forecast_history.append(smoothed_forecast)
        else:
            self.lines.forecast[0] = self.lines.macd[0]
            self.lines.upper_band[0] = self.lines.macd[0]
            self.lines.lower_band[0] = self.lines.macd[0]
            self.lines.prediction_error[0] = 0
            self.lines.confidence[0] = 0
            
        # Historie begrenzen
        max_period = max(self.p.slow_period, self.p.signal_period)
        for hist in [self.macd_history, self.forecast_history, self.error_history]:
            if len(hist) > max_period:
                hist.pop(0)
                
        # Signal-Generierung
        # Buy Signal
        if (self.lines.forecast[0] > self.lines.macd[0] and
            self.lines.confidence[0] > 0.7 and
            self.lines.prediction_error[0] < 0.2):
            self.lines.buy_signal[0] = self.data.low[0]
        else:
            self.lines.buy_signal[0] = float('nan')
            
        # Sell Signal
        if (self.lines.forecast[0] < self.lines.macd[0] and
            self.lines.confidence[0] > 0.7 and
            self.lines.prediction_error[0] < 0.2):
            self.lines.sell_signal[0] = self.data.high[0]
        else:
            self.lines.sell_signal[0] = float('nan')
            
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        return {
            'current': {
                'macd': self.lines.macd[0],
                'signal': self.lines.signal[0],
                'forecast': self.lines.forecast[0],
                'error': self.lines.prediction_error[0],
                'confidence': self.lines.confidence[0]
            },
            'prediction': {
                'direction': np.sign(
                    self.lines.forecast[0] - self.lines.macd[0]
                ),
                'magnitude': abs(
                    self.lines.forecast[0] - self.lines.macd[0]
                ),
                'reliability': (
                    self.lines.confidence[0] *
                    (1 - self.lines.prediction_error[0])
                )
            },
            'trend': {
                'current': (
                    'bullish' if self.lines.macd[0] > self.lines.signal[0]
                    else 'bearish'
                ),
                'predicted': (
                    'bullish' if self.lines.forecast[0] > self.lines.macd[0]
                    else 'bearish'
                ),
                'strength': abs(
                    self.lines.macd[0] - self.lines.signal[0]
                )
            },
            'signals': {
                'buy': self.lines.buy_signal[0] != float('nan'),
                'sell': self.lines.sell_signal[0] != float('nan'),
                'strength': abs(
                    self.lines.forecast[0] - self.lines.macd[0]
                ),
                'reliability': (
                    self.lines.confidence[0] *
                    (1 - self.lines.prediction_error[0])
                )
            },
            'risk': {
                'volatility': self.vol[0] / self.data[0] if self.data[0] != 0 else 0,
                'prediction_error': self.lines.prediction_error[0],
                'forecast_stability': (
                    np.std(self.forecast_history)
                    if len(self.forecast_history) > 1
                    else 0
                )
            }
        }
