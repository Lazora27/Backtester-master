import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandLiquidityMap_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandLiquidityMap und TimeCycle
    """
    
    params = (
        ('indicators', {
            'SupplyDemandLiquidityMap': {
                'class': SupplyDemandLiquidityMap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandLiquidityMap'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'SupplyDemandLiquidityMap': 1.0,
            'TimeCycle': 1.0
        })
    )
