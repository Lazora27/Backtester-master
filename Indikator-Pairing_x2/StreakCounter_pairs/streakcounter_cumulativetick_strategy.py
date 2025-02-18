import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'CumulativeTick': 1.0
        })
    )
