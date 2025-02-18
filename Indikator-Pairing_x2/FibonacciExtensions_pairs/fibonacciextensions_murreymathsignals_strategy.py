import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
