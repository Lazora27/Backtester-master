import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
