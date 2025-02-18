import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und CycleFinder
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'CycleFinder': 1.0
        })
    )
