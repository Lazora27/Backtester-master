import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'FibonacciZones': 1.0
        })
    )
