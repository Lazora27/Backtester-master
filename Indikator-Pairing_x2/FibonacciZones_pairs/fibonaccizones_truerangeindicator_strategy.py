import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
