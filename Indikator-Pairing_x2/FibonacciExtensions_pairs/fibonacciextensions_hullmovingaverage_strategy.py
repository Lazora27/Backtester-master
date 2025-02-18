import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'HullMovingAverage': 1.0
        })
    )
