import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'GannSquareReversal': 1.0
        })
    )
