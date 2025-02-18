import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und GannFans
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'GannFans': 1.0
        })
    )
