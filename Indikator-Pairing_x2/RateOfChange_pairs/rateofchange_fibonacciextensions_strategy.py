import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
