import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und StreakCounter
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'StreakCounter': 1.0
        })
    )
