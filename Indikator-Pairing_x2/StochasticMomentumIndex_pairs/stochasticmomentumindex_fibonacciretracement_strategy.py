import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
