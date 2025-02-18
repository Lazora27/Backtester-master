import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'HilbertTrendline': 1.0
        })
    )
