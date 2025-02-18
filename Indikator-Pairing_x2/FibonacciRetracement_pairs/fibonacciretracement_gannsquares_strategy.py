import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und GannSquares
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'GannSquares': 1.0
        })
    )
