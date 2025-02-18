import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
