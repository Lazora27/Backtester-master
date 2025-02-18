import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und PivotPoints
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'PivotPoints': 1.0
        })
    )
