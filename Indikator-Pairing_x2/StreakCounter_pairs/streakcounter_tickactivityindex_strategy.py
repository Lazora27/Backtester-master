import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'TickActivityIndex': 1.0
        })
    )
