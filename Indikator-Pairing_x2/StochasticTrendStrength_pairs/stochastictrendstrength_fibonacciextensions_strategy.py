import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
