import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
