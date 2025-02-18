import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
