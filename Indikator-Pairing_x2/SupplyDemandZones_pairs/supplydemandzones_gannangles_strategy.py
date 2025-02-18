import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und GannAngles
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'GannAngles': 1.0
        })
    )
