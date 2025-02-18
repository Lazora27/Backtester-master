import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'HilbertSinewave': 1.0
        })
    )
