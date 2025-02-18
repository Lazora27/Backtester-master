import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und SuperMACD
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'SuperMACD': 1.0
        })
    )
