import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
