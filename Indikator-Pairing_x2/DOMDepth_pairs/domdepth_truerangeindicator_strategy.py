import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
