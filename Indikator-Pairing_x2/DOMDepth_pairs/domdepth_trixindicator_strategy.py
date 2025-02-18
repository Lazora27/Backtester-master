import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'TRIXIndicator': 1.0
        })
    )
