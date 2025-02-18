import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
