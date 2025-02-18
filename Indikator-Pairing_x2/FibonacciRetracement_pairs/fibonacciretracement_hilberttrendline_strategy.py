import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'HilbertTrendline': 1.0
        })
    )
