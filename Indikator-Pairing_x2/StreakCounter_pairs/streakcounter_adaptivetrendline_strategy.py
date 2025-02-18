import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
