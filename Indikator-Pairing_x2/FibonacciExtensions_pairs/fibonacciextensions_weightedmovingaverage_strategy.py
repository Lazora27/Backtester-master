import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
