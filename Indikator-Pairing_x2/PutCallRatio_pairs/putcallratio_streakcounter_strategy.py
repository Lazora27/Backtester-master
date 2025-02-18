import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und StreakCounter
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'StreakCounter': 1.0
        })
    )
