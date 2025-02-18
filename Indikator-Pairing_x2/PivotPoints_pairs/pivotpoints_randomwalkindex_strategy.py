import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
