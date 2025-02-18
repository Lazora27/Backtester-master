import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'FibonacciZones': 1.0
        })
    )
