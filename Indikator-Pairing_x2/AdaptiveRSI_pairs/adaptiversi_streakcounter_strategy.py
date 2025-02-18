import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und StreakCounter
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'StreakCounter': 1.0
        })
    )
