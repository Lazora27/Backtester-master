import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
