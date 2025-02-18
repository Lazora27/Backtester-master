import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
