import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und WilliamsR
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'WilliamsR': 1.0
        })
    )
