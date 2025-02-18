import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'AdaptiveATR': 1.0
        })
    )
