import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'HilbertSinewave': 1.0
        })
    )
