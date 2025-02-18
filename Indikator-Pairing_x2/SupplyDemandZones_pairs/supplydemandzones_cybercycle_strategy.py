import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und CyberCycle
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'CyberCycle': 1.0
        })
    )
