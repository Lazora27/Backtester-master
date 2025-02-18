import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
