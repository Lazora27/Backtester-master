import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
