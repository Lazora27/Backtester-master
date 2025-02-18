import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und GannSquares
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'GannSquares': 1.0
        })
    )
