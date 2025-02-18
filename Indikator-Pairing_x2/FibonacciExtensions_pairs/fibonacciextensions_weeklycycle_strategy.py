import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'WeeklyCycle': 1.0
        })
    )
