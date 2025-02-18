import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und TrueRange
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'TrueRange': 1.0
        })
    )
