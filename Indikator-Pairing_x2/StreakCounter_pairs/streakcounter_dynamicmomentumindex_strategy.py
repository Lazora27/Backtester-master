import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_DynamicMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und DynamicMomentumIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'DynamicMomentumIndex': 1.0
        })
    )
