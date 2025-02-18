import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
