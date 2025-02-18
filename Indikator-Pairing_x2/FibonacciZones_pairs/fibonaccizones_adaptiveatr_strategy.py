import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'AdaptiveATR': 1.0
        })
    )
