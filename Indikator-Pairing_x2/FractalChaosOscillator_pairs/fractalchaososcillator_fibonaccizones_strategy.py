import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'FibonacciZones': 1.0
        })
    )
