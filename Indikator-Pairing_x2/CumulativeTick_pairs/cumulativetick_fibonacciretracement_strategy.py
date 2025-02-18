import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
