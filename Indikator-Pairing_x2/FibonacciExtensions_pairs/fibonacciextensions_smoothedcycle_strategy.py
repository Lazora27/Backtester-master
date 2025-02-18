import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'SmoothedCycle': 1.0
        })
    )
