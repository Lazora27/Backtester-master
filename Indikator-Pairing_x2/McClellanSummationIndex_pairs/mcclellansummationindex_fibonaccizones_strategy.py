import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'FibonacciZones': 1.0
        })
    )
