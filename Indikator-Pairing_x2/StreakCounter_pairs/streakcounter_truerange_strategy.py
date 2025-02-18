import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und TrueRange
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'TrueRange': 1.0
        })
    )
