import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandLiquidityMap_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandLiquidityMap und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'SupplyDemandLiquidityMap': {
                'class': SupplyDemandLiquidityMap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandLiquidityMap'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'SupplyDemandLiquidityMap': 1.0,
            'TRIXIndicator': 1.0
        })
    )
