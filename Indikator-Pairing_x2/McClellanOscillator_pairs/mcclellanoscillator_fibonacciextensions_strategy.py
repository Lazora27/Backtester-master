import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
