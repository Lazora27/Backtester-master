import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'AverageLogRange': 1.0
        })
    )
