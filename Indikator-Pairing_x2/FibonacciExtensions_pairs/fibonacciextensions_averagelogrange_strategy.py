import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'AverageLogRange': 1.0
        })
    )
