import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
