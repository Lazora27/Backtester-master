import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und TimeCycle
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'TimeCycle': 1.0
        })
    )
