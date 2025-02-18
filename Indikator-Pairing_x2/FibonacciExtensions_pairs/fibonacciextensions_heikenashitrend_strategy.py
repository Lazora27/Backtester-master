import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
