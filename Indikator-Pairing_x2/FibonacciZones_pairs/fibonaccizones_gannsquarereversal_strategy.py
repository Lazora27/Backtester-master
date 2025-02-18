import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'GannSquareReversal': 1.0
        })
    )
