import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und DemandIndex
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'DemandIndex': 1.0
        })
    )
