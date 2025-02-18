import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
