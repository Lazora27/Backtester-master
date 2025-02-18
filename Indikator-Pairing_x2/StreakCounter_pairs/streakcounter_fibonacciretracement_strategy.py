import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
