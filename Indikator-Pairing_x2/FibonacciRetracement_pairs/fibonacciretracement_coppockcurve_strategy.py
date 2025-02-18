import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'CoppockCurve': 1.0
        })
    )
