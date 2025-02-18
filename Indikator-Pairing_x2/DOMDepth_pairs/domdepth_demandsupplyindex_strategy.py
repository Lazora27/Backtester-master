import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
