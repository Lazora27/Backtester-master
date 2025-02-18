import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und PivotPoints
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'PivotPoints': 1.0
        })
    )
