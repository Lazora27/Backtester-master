import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und SuperTrend
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'SuperTrend': 1.0
        })
    )
