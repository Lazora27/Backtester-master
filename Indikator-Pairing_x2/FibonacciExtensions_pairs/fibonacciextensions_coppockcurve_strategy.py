import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'CoppockCurve': 1.0
        })
    )
