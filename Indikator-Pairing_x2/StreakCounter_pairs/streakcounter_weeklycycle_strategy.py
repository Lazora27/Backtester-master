import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'WeeklyCycle': 1.0
        })
    )
