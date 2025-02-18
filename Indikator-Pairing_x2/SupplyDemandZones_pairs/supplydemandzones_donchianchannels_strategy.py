import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'DonchianChannels': 1.0
        })
    )
