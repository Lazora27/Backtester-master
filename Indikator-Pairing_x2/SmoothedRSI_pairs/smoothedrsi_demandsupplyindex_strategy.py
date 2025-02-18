import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
