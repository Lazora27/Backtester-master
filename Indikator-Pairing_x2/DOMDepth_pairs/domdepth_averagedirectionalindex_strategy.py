import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
