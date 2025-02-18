import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und DOMDepth
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'DOMDepth': 1.0
        })
    )
