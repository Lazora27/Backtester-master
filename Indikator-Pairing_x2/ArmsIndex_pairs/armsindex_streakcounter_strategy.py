import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und StreakCounter
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'StreakCounter': 1.0
        })
    )
