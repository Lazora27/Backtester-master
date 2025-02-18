import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'ModifiedRSI': 1.0
        })
    )
