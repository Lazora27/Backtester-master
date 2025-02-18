import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
