import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
