import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'WeightedCycle': 1.0
        })
    )
