import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'TickActivityIndex': 1.0
        })
    )
