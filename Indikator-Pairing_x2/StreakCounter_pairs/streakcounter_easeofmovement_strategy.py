import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'EaseOfMovement': 1.0
        })
    )
