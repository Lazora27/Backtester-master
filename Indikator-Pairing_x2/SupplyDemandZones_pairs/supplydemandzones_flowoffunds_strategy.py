import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'FlowOfFunds': 1.0
        })
    )
