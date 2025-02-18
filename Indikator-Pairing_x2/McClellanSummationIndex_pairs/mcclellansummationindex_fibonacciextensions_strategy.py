import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
