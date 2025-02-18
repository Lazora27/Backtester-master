import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
