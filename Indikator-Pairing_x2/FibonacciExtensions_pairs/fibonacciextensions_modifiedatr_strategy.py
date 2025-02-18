import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'ModifiedATR': 1.0
        })
    )
