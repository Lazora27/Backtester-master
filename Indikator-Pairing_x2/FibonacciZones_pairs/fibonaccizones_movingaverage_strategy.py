import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und MovingAverage
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'MovingAverage': 1.0
        })
    )
