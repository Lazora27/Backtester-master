import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
