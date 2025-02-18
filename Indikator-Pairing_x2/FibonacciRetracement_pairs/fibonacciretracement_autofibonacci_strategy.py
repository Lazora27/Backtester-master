import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'AutoFibonacci': 1.0
        })
    )
