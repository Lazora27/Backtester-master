import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
