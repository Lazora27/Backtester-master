import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
