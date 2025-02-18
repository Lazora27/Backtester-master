import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_SupplyDemandLiquidityMap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und SupplyDemandLiquidityMap
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'SupplyDemandLiquidityMap': {
                'class': SupplyDemandLiquidityMap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandLiquidityMap'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'SupplyDemandLiquidityMap': 1.0
        })
    )
