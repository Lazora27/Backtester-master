import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
