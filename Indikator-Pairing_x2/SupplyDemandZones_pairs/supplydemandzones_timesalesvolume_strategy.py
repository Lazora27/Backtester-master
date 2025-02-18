import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
