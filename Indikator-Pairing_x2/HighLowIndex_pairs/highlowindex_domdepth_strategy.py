import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und DOMDepth
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'DOMDepth': 1.0
        })
    )
