import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
