import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
