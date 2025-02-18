import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und TrueRange
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'TrueRange': 1.0
        })
    )
