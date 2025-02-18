import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
