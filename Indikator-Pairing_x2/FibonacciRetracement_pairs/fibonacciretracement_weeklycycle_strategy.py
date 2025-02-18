import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'WeeklyCycle': 1.0
        })
    )
