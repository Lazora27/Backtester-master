import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
