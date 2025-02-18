import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und VWAPBands
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'VWAPBands': 1.0
        })
    )
