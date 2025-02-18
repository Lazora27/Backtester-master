import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_KDJIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und KDJIndicator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'KDJIndicator': 1.0
        })
    )
