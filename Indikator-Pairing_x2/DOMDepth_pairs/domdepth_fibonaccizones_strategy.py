import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'FibonacciZones': 1.0
        })
    )
