import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'FibonacciZones': 1.0
        })
    )
