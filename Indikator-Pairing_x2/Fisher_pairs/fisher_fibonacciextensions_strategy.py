import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
