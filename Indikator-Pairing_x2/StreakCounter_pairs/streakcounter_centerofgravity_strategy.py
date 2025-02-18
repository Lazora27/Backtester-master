import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'CenterOfGravity': 1.0
        })
    )
