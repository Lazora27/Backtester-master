import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'HullMovingAverage': 1.0
        })
    )
