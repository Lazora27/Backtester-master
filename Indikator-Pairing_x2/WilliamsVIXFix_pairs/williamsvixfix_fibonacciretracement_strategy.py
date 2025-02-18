import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
