import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
