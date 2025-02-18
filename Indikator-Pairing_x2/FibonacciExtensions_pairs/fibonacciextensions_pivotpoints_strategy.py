import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und PivotPoints
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'PivotPoints': 1.0
        })
    )
