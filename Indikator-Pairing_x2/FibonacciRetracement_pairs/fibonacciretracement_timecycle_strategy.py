import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und TimeCycle
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'TimeCycle': 1.0
        })
    )
