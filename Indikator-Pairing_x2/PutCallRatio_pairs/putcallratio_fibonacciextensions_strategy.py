import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
