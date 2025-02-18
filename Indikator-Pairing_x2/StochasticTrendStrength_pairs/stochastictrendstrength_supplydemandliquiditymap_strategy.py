import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_SupplyDemandLiquidityMap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und SupplyDemandLiquidityMap
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'SupplyDemandLiquidityMap': {
                'class': SupplyDemandLiquidityMap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandLiquidityMap'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'SupplyDemandLiquidityMap': 1.0
        })
    )
