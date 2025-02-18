import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
