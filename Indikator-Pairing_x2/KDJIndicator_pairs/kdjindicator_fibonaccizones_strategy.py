import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'FibonacciZones': 1.0
        })
    )
