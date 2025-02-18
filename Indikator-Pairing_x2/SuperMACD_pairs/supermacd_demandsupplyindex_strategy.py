import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
