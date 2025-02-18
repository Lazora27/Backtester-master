import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'EldersForceIndex': 1.0
        })
    )
