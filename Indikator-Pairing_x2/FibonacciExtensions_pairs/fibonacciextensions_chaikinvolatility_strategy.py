import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
