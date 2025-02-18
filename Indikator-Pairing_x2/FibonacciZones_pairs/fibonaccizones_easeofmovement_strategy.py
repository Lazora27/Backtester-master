import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'EaseOfMovement': 1.0
        })
    )
