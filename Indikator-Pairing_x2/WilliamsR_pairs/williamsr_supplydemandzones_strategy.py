import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
