import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
