import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_ZigZagFibonacciIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und ZigZagFibonacciIndicator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'ZigZagFibonacciIndicator': {
                'class': ZigZagFibonacciIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagFibonacciIndicator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'ZigZagFibonacciIndicator': 1.0
        })
    )
