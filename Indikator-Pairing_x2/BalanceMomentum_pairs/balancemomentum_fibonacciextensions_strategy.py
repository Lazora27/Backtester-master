import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
