import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'VolumeDelta': 1.0
        })
    )
