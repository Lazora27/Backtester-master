import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'FearGreedIndex': 1.0
        })
    )
