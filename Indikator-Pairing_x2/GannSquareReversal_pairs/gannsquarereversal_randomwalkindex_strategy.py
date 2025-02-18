import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
