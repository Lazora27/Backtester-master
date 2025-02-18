import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und MovingAverage
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'MovingAverage': 1.0
        })
    )
