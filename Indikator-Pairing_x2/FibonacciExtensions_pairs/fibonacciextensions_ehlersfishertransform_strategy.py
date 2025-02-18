import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
