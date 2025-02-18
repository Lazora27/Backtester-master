import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
