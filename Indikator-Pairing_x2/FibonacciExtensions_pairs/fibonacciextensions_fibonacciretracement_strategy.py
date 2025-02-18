import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
