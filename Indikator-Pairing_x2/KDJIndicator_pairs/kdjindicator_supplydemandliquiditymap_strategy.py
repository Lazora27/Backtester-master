import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_SupplyDemandLiquidityMap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und SupplyDemandLiquidityMap
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'SupplyDemandLiquidityMap': {
                'class': SupplyDemandLiquidityMap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandLiquidityMap'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'SupplyDemandLiquidityMap': 1.0
        })
    )
