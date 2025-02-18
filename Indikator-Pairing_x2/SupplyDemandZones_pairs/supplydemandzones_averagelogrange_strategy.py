import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'AverageLogRange': 1.0
        })
    )
