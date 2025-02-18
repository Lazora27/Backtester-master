import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'ModifiedATR': 1.0
        })
    )
