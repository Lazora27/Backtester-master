import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
