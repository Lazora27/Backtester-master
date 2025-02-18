import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
