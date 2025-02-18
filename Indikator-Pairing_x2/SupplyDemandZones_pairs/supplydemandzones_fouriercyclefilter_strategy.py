import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
