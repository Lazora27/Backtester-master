import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und DOMDepth
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'DOMDepth': 1.0
        })
    )
