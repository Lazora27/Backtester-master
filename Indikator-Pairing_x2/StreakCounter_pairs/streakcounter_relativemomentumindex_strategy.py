import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
