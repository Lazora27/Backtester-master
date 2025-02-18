import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'FibonacciZones': 1.0
        })
    )
