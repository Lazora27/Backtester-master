import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'WeeklyCycle': 1.0
        })
    )
