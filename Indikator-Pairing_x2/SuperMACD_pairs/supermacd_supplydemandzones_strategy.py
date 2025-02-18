import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
