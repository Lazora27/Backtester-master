import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'MomentumIndicator': 1.0
        })
    )
