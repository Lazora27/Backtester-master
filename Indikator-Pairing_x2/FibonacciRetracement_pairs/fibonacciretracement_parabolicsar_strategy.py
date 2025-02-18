import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'ParabolicSAR': 1.0
        })
    )
