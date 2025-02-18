import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
