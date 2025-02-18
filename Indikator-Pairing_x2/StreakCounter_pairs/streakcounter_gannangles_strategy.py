import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und GannAngles
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'GannAngles': 1.0
        })
    )
