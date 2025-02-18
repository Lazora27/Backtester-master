import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
