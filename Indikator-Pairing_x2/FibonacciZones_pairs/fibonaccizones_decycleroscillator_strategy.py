import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
