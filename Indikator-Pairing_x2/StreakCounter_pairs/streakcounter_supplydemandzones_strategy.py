import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
