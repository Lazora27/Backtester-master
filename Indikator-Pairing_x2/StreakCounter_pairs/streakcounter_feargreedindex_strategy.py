import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'FearGreedIndex': 1.0
        })
    )
