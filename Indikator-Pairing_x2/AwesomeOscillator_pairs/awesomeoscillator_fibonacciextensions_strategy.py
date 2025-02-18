import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
