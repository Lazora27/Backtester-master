import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'FearGreedIndex': 1.0
        })
    )
