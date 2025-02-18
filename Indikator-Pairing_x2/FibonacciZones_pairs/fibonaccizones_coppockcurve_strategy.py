import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'CoppockCurve': 1.0
        })
    )
