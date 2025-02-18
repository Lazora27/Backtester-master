import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
