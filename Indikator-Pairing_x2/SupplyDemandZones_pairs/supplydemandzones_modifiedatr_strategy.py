import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'ModifiedATR': 1.0
        })
    )
