import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'WeightedCycle': 1.0
        })
    )
