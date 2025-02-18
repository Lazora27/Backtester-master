import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
