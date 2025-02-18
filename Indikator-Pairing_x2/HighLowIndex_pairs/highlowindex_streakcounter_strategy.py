import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und StreakCounter
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'StreakCounter': 1.0
        })
    )
