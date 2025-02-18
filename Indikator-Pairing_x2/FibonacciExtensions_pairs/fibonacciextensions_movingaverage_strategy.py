import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und MovingAverage
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'MovingAverage': 1.0
        })
    )
