import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'ModifiedATR': 1.0
        })
    )
