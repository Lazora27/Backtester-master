import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
