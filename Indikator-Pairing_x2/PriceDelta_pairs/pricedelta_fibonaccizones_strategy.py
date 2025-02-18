import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'FibonacciZones': 1.0
        })
    )
