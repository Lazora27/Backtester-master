import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LaggingVolatilityIndex_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LaggingVolatilityIndex und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'LaggingVolatilityIndex': {
                'class': LaggingVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LaggingVolatilityIndex'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'LaggingVolatilityIndex': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
