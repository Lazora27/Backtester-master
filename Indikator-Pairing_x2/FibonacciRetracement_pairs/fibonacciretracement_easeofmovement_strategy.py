import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'EaseOfMovement': 1.0
        })
    )
