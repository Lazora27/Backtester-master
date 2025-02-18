import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
