import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und DemandIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'DemandIndex': 1.0
        })
    )
