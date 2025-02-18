import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
