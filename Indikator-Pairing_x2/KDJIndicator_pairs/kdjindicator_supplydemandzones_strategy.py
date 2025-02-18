import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
