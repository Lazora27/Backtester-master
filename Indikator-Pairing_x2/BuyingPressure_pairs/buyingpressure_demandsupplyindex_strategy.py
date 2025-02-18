import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
