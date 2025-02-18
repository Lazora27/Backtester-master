import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
