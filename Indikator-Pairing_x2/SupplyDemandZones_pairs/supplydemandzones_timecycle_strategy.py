import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und TimeCycle
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'TimeCycle': 1.0
        })
    )
