import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
