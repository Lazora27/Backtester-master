import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'SmoothedCycle': 1.0
        })
    )
