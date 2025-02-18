import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'GannSquareReversal': 1.0
        })
    )
