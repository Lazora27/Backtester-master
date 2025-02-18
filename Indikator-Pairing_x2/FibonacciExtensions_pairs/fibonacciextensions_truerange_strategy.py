import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und TrueRange
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'TrueRange': 1.0
        })
    )
