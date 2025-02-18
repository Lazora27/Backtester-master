import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und StreakCounter
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'StreakCounter': 1.0
        })
    )
