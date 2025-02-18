import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'UlcerIndex': 1.0
        })
    )
