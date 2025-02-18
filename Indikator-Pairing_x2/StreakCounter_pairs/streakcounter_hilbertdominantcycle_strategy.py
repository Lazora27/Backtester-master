import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
