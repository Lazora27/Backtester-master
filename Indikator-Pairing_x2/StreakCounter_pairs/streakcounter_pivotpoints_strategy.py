import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und PivotPoints
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'PivotPoints': 1.0
        })
    )
