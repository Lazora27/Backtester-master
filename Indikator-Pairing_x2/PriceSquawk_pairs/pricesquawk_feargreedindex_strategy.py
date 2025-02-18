import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'FearGreedIndex': 1.0
        })
    )
