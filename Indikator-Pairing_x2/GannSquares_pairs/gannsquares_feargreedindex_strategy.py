import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'FearGreedIndex': 1.0
        })
    )
