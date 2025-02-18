import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'FibonacciZones': 1.0
        })
    )
