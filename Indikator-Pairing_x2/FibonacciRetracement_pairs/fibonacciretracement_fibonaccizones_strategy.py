import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'FibonacciZones': 1.0
        })
    )
