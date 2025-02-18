import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'SmoothedCycle': 1.0
        })
    )
