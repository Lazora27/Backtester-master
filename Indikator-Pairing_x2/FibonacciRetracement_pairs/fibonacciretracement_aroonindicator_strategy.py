import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'AroonIndicator': 1.0
        })
    )
