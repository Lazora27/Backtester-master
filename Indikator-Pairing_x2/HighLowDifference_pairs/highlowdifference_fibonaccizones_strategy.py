import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'FibonacciZones': 1.0
        })
    )
