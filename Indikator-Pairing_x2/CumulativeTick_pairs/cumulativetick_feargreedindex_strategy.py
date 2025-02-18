import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'FearGreedIndex': 1.0
        })
    )
