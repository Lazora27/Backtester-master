import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
