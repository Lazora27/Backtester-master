import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
