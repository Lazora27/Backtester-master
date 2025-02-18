import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
