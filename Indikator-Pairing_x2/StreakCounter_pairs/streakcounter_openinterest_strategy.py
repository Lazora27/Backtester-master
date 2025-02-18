import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und OpenInterest
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'OpenInterest': 1.0
        })
    )
