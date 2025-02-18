import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und SuperTrend
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'SuperTrend': 1.0
        })
    )
