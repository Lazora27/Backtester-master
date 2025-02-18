import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und GannFans
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'GannFans': 1.0
        })
    )
