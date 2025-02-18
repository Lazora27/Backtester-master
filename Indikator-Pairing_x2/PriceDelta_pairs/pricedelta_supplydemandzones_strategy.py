import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
