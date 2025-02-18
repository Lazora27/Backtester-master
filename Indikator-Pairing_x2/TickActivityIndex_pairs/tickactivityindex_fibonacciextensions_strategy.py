import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
