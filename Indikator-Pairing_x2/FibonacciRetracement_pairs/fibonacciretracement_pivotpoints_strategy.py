import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und PivotPoints
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'PivotPoints': 1.0
        })
    )
