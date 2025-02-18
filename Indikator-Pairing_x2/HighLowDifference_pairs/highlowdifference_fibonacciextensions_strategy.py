import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
