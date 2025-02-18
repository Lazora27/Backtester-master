import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
