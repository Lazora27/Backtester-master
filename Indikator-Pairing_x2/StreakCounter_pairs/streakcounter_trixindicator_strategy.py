import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'TRIXIndicator': 1.0
        })
    )
