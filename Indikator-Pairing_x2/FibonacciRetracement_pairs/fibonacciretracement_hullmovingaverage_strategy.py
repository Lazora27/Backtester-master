import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'HullMovingAverage': 1.0
        })
    )
