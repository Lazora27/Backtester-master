import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'FearGreedIndex': 1.0
        })
    )
