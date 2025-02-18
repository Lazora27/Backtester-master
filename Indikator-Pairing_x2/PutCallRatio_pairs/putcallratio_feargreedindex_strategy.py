import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'FearGreedIndex': 1.0
        })
    )
