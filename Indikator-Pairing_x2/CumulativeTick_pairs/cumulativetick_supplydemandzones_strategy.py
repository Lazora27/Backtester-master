import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
