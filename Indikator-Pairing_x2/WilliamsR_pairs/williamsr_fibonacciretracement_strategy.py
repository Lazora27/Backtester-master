import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
