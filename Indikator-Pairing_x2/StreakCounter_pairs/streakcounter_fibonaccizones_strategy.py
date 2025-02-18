import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'FibonacciZones': 1.0
        })
    )
