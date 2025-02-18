import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'HullMovingAverage': 1.0
        })
    )
