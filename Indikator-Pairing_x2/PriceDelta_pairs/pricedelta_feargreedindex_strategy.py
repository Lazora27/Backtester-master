import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'FearGreedIndex': 1.0
        })
    )
