import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
