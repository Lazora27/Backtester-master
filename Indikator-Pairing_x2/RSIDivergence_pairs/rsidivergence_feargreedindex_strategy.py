import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'FearGreedIndex': 1.0
        })
    )
