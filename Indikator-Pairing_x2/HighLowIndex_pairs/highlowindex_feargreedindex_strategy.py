import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'FearGreedIndex': 1.0
        })
    )
