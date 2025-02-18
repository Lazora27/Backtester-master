import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandLiquidityMap_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandLiquidityMap und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'SupplyDemandLiquidityMap': {
                'class': SupplyDemandLiquidityMap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandLiquidityMap'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'SupplyDemandLiquidityMap': 1.0,
            'WeightedCycle': 1.0
        })
    )
