import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
