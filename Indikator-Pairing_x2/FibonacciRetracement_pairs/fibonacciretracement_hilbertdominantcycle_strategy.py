import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
