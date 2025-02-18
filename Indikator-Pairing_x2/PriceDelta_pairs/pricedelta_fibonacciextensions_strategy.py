import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
