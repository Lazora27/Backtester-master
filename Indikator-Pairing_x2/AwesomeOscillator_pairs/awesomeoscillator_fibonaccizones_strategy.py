import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'FibonacciZones': 1.0
        })
    )
