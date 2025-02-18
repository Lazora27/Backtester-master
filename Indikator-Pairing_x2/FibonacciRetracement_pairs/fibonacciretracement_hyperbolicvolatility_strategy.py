import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
