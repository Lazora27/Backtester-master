import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
