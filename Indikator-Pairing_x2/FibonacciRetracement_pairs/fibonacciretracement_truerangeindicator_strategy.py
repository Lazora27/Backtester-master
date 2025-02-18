import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
