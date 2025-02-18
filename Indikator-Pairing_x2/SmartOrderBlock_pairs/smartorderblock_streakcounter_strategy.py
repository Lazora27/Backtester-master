import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und StreakCounter
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'StreakCounter': 1.0
        })
    )
