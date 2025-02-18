import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'DonchianVolatility': 1.0
        })
    )
