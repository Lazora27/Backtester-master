import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
