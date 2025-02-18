import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
