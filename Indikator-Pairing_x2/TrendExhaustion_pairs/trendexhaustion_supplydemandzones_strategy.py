import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
