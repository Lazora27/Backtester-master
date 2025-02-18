import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und Fisher
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'Fisher': 1.0
        })
    )
