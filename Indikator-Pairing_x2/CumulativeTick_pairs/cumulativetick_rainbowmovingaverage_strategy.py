import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
