import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'AdaptiveATR': 1.0
        })
    )
