import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'SmoothedRSI': 1.0
        })
    )
