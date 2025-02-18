import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
