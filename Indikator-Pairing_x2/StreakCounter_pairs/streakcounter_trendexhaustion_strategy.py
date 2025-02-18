import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'TrendExhaustion': 1.0
        })
    )
