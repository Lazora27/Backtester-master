import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
