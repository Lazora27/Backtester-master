import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
