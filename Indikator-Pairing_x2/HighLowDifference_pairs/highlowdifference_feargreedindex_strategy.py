import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'FearGreedIndex': 1.0
        })
    )
