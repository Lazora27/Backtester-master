import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
