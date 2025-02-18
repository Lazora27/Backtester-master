import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'ExtensionProjections': 1.0
        })
    )
