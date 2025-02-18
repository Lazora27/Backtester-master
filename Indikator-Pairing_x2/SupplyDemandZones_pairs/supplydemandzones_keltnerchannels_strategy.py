import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'KeltnerChannels': 1.0
        })
    )
