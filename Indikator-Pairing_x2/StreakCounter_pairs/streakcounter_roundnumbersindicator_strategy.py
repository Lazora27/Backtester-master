import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
