import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
