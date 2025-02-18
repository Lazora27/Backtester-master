import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
