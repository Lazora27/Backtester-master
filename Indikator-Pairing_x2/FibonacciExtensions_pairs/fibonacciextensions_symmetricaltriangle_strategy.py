import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
