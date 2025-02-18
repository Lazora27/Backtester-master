import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'HilbertSinewave': 1.0
        })
    )
