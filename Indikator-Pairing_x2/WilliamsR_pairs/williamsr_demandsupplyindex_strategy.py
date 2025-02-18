import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
