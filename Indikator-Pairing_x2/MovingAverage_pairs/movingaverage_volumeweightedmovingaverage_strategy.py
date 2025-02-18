import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_VolumeWeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und VolumeWeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'VolumeWeightedMovingAverage': {
                'class': VolumeWeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedMovingAverage'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'VolumeWeightedMovingAverage': 1.0
        })
    )
