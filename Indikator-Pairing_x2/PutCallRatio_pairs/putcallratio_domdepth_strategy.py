import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und DOMDepth
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'DOMDepth': 1.0
        })
    )
