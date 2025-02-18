import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'MurreyMathLines': 1.0
        })
    )
