import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
