import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'SmoothedCycle': 1.0
        })
    )
