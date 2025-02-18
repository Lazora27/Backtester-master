import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'FibonacciZones': 1.0
        })
    )
