import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'HilbertSinewave': 1.0
        })
    )
