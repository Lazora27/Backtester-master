import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
