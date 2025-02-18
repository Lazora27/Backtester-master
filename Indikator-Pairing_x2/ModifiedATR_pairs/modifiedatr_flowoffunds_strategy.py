import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'FlowOfFunds': 1.0
        })
    )
