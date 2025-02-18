import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
