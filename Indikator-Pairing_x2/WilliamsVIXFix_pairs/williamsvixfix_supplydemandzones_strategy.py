import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
