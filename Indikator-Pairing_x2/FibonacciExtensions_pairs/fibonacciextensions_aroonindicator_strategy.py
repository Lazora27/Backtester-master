import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'AroonIndicator': 1.0
        })
    )
