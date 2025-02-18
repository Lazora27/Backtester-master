import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
