import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
