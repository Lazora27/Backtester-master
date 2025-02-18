import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
