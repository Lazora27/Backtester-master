import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'FibonacciZones': 1.0
        })
    )
