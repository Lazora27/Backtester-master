import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
