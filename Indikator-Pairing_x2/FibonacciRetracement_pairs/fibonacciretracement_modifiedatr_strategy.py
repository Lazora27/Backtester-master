import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'ModifiedATR': 1.0
        })
    )
