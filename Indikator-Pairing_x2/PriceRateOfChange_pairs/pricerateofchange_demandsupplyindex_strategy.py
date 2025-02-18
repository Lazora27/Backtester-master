import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
