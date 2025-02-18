import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'HullMovingAverage': 1.0
        })
    )
