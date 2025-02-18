import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
