import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
