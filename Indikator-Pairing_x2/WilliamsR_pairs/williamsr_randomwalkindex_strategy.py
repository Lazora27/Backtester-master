import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
