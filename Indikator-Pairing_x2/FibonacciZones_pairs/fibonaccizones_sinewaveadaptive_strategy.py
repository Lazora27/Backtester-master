import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
