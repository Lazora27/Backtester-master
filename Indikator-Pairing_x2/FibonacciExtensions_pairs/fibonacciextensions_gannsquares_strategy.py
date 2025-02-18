import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und GannSquares
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'GannSquares': 1.0
        })
    )
