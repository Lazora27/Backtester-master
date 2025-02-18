import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
