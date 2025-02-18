import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'FibonacciZones': 1.0
        })
    )
