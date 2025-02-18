import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und StreakCounter
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'StreakCounter': 1.0
        })
    )
