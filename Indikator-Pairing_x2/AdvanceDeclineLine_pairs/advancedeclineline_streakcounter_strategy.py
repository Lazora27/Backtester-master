import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und StreakCounter
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'StreakCounter': 1.0
        })
    )
