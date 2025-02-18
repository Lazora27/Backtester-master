import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
