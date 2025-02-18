import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und TrueRange
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'TrueRange': 1.0
        })
    )
