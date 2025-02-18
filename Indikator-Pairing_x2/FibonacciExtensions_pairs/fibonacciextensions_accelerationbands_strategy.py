import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'AccelerationBands': 1.0
        })
    )
