import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
