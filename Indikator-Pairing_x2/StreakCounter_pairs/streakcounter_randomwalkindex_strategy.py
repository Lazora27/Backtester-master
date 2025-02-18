import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
