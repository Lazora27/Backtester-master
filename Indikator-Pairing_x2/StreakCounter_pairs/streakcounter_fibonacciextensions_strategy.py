import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
