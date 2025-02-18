import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'TRIXIndicator': 1.0
        })
    )
