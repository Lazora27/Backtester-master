import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'ParabolicSAR': 1.0
        })
    )
