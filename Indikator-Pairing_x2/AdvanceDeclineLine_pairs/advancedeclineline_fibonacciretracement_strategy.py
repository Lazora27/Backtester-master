import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
