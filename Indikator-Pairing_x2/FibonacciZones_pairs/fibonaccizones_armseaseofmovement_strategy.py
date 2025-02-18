import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_ArmsEaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und ArmsEaseOfMovement
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'ArmsEaseOfMovement': {
                'class': ArmsEaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsEaseOfMovement'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'ArmsEaseOfMovement': 1.0
        })
    )
