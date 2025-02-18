import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_SupplyDemandLiquidityMap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und SupplyDemandLiquidityMap
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'SupplyDemandLiquidityMap': {
                'class': SupplyDemandLiquidityMap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandLiquidityMap'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'SupplyDemandLiquidityMap': 1.0
        })
    )
