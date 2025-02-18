import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
