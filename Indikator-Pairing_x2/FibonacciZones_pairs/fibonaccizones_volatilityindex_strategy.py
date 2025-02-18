import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'VolatilityIndex': 1.0
        })
    )
