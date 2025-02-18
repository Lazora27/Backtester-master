import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
