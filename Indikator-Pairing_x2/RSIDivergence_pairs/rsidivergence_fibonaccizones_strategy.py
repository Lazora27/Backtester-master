import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'FibonacciZones': 1.0
        })
    )
