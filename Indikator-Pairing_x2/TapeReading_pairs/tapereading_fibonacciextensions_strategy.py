import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
