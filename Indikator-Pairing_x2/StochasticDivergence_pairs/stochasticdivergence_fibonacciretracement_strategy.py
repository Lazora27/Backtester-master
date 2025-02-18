import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
