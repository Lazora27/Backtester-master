import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
