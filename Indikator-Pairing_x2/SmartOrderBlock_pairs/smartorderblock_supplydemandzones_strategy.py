import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
