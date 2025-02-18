import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'AutoFibonacci': 1.0
        })
    )
