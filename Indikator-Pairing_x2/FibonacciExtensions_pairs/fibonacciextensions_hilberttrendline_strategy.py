import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'HilbertTrendline': 1.0
        })
    )
