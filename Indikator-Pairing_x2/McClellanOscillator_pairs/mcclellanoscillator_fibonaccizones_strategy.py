import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'FibonacciZones': 1.0
        })
    )
