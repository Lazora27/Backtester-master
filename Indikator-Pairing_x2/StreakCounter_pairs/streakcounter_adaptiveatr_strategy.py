import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'AdaptiveATR': 1.0
        })
    )
