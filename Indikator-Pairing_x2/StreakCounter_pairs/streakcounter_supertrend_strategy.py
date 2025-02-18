import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und SuperTrend
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'SuperTrend': 1.0
        })
    )
