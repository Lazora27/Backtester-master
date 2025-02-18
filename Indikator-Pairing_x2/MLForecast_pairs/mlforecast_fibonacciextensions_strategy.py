import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
