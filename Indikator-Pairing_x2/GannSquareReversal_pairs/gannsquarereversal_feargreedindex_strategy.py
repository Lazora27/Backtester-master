import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'FearGreedIndex': 1.0
        })
    )
