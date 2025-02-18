import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
