import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'VortexIndicator': 1.0
        })
    )
