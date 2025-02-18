import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
