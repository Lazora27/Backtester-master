import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'UlcerIndex': 1.0
        })
    )
