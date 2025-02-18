import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
