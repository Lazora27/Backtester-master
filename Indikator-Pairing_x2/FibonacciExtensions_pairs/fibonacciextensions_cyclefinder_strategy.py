import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und CycleFinder
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'CycleFinder': 1.0
        })
    )
