import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandLiquidityMap_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandLiquidityMap und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'SupplyDemandLiquidityMap': {
                'class': SupplyDemandLiquidityMap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandLiquidityMap'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'SupplyDemandLiquidityMap': 1.0,
            'IntradayIntensity': 1.0
        })
    )
