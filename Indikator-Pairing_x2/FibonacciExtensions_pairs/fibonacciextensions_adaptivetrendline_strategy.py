import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
