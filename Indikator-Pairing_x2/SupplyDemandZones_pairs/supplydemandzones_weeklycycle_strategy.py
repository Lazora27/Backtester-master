import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'WeeklyCycle': 1.0
        })
    )
