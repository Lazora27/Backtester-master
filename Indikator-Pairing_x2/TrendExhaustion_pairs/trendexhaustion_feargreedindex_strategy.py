import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'FearGreedIndex': 1.0
        })
    )
