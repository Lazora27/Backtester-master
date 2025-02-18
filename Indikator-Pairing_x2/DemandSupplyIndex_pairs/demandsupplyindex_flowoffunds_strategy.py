import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
