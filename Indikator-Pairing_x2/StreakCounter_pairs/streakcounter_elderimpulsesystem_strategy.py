import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
