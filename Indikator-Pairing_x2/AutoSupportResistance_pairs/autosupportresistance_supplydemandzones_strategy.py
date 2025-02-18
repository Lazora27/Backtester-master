import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
