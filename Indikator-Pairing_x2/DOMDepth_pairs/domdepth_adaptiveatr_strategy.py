import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'AdaptiveATR': 1.0
        })
    )
