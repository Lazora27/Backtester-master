import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
