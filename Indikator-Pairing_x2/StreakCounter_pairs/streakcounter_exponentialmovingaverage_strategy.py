import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
