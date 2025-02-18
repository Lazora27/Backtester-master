import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und OpenInterest
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'OpenInterest': 1.0
        })
    )
