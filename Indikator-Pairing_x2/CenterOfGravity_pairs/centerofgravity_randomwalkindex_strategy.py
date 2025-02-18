import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
