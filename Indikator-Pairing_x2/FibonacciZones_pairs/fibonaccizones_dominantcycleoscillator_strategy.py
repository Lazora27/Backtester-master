import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
