import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
