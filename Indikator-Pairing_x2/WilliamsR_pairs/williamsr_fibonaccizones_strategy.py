import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'FibonacciZones': 1.0
        })
    )
