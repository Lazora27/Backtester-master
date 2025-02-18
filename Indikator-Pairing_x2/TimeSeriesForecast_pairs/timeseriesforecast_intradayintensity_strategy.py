import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'IntradayIntensity': 1.0
        })
    )
