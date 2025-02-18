import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'FearGreedIndex': 1.0
        })
    )
