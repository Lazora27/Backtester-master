import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und DOMDepth
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'DOMDepth': 1.0
        })
    )
