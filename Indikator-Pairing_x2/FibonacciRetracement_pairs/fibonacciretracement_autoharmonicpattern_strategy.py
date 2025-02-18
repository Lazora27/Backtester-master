import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
