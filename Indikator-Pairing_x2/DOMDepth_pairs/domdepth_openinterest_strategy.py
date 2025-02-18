import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und OpenInterest
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'OpenInterest': 1.0
        })
    )
