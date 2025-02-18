import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
