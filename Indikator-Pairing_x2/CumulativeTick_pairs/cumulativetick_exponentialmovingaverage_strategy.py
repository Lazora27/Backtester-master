import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
