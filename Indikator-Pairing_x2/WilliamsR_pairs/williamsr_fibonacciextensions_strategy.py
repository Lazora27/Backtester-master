import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
