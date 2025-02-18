import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
