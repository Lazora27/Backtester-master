import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'FibonacciZones': 1.0
        })
    )
