import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
