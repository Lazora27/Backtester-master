import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'BuyingPressure': 1.0
        })
    )
