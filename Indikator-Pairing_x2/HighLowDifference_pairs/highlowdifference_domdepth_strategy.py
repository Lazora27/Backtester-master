import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und DOMDepth
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'DOMDepth': 1.0
        })
    )
