import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
