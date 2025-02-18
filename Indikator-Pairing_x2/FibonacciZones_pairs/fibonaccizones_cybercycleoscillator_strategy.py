import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
