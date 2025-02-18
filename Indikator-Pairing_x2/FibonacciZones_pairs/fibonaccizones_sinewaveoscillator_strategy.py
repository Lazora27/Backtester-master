import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
