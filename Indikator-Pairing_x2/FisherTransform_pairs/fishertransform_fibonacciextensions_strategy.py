import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
