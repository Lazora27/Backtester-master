import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und MovingAverage
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'MovingAverage': 1.0
        })
    )
