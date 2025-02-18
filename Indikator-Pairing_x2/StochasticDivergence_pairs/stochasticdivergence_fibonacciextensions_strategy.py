import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
