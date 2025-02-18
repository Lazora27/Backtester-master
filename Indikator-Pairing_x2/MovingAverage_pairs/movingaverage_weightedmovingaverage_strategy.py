import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
