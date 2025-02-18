import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
