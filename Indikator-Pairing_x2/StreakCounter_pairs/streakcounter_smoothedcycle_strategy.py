import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'SmoothedCycle': 1.0
        })
    )
